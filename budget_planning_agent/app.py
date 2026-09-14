# ==========================================================
# AKHIL'S MONTHLY BUDGET PLANNER
# FLASK WEB APPLICATION
# ==========================================================

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

import sqlite3
from datetime import datetime

from ml_model import (
    predict_budget,
    get_budget_analysis
)


# ==========================================================
# FLASK APPLICATION
# ==========================================================

app = Flask(__name__)

app.secret_key = "akki_budget_planner_secret_key"


# ==========================================================
# DATABASE CONFIGURATION
# ==========================================================

DATABASE = "budget.db"


# ==========================================================
# DATABASE CONNECTION
# ==========================================================

def get_db_connection():

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    return connection


# ==========================================================
# CREATE DATABASE TABLE
# ==========================================================

def init_database():

    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS budget_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            income REAL NOT NULL,

            house_rent REAL NOT NULL,

            emi REAL NOT NULL,

            food_grocery REAL NOT NULL,

            transportation REAL NOT NULL,

            shopping REAL NOT NULL,

            entertainment REAL NOT NULL,

            healthcare REAL NOT NULL,

            savings REAL NOT NULL,

            other_expenses REAL NOT NULL,

            total_expenses REAL NOT NULL,

            total_budget REAL NOT NULL,

            remaining REAL NOT NULL,

            created_at TEXT NOT NULL

        )
    """)

    connection.commit()

    connection.close()


# ==========================================================
# HOME PAGE
# ==========================================================

@app.route("/")
def index():

    return render_template(
        "index.html"
    )


# ==========================================================
# BUDGET PLANNER
# ==========================================================

@app.route(
    "/planner",
    methods=["GET", "POST"]
)
def planner():

    # ------------------------------------------------------
    # GET REQUEST
    # ------------------------------------------------------

    if request.method == "GET":

        return render_template(
            "planner.html"
        )


    # ------------------------------------------------------
    # POST REQUEST
    # ------------------------------------------------------

    name = request.form.get(
        "name",
        ""
    ).strip()

    income_value = request.form.get(
        "income",
        ""
    ).strip()


    # ------------------------------------------------------
    # NAME VALIDATION
    # ------------------------------------------------------

    if not name:

        flash(
            "Please enter your name.",
            "error"
        )

        return render_template(
            "planner.html",
            name=name,
            income=income_value
        )


    # Only alphabetic characters and spaces

    if not name or not all(part.isalpha() for part in name.split()):

        flash(
            "Please enter a valid name.",
            "error"
        )

        return render_template(
            "planner.html",
            name=name,
            income=income_value
        )


    # ------------------------------------------------------
    # INCOME VALIDATION
    # ------------------------------------------------------

    if not income_value:

        flash(
            "Please enter your monthly income.",
            "error"
        )

        return render_template(
            "planner.html",
            name=name
        )


    try:

        income = float(
            income_value
        )

    except ValueError:

        flash(
            "Please enter a valid income.",
            "error"
        )

        return render_template(
            "planner.html",
            name=name,
            income=income_value
        )


    if income <= 0:

        flash(
            "Income must be greater than zero.",
            "error"
        )

        return render_template(
            "planner.html",
            name=name,
            income=income_value
        )


    # ------------------------------------------------------
    # ML PREDICTION
    # ------------------------------------------------------

    try:

        budget = predict_budget(
            income
        )

    except Exception as error:

        print(
            "ML Prediction Error:",
            error
        )

        flash(
            "Unable to generate budget. Please try again.",
            "error"
        )

        return render_template(
            "planner.html",
            name=name,
            income=income_value
        )


    # ------------------------------------------------------
    # CALCULATE ANALYSIS
    # ------------------------------------------------------

    analysis = get_budget_analysis(
        income
    )


    # ------------------------------------------------------
    # SAVE DATA TO SESSION
    # ------------------------------------------------------

    session["name"] = name

    session["income"] = income

    session["budget"] = budget

    session["total_expenses"] = (
        analysis["total_expenses"]
    )

    session["total_budget"] = (
        analysis["total_budget"]
    )

    session["remaining"] = (
        analysis["remaining"]
    )

    session["percentages"] = (
        analysis["percentages"]
    )


    # ------------------------------------------------------
    # SAVE TO DATABASE
    # ------------------------------------------------------

    connection = get_db_connection()

    connection.execute(
        """
        INSERT INTO budget_history (

            name,
            income,

            house_rent,
            emi,
            food_grocery,
            transportation,
            shopping,
            entertainment,
            healthcare,
            savings,
            other_expenses,

            total_expenses,
            total_budget,
            remaining,

            created_at

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,

        (

            name,
            income,

            budget["house_rent"],
            budget["emi"],
            budget["food_grocery"],
            budget["transportation"],
            budget["shopping"],
            budget["entertainment"],
            budget["healthcare"],
            budget["savings"],
            budget["other_expenses"],

            analysis["total_expenses"],
            analysis["total_budget"],
            analysis["remaining"],

            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        )
    )

    connection.commit()

    connection.close()


    flash(
        "Your budget has been generated successfully!",
        "success"
    )


    return redirect(
        url_for("result")
    )


# ==========================================================
# RESULT PAGE
# ==========================================================

@app.route("/result")
def result():

    # ------------------------------------------------------
    # CHECK SESSION
    # ------------------------------------------------------

    if "budget" not in session:

        flash(
            "Please create a budget plan first.",
            "error"
        )

        return redirect(
            url_for("planner")
        )


    # ------------------------------------------------------
    # GET SESSION DATA
    # ------------------------------------------------------

    name = session.get(
        "name"
    )

    income = session.get(
        "income"
    )

    budget = session.get(
        "budget"
    )

    # ------------------------------------------------------
    # DISPLAY RESULT
    # ------------------------------------------------------

    return render_template(

        "result.html",

        name=name,

        income=income,

        budget=budget

    )


# ==========================================================
# ANALYSIS PAGE
# ==========================================================

@app.route("/analysis")
def analysis():

    # ------------------------------------------------------
    # CHECK SESSION
    # ------------------------------------------------------

    if "budget" not in session:

        flash(
            "Please create a budget plan first.",
            "error"
        )

        return redirect(
            url_for("planner")
        )


    # ------------------------------------------------------
    # GET DATA
    # ------------------------------------------------------

    name = session.get(
        "name"
    )

    income = session.get(
        "income"
    )

    budget = session.get(
        "budget"
    )

    total_expenses = session.get(
        "total_expenses"
    )

    total_budget = session.get(
        "total_budget"
    )

    remaining = session.get(
        "remaining"
    )
    
    # ------------------------------------------------------
    # ANALYSIS
    # ------------------------------------------------------

    return render_template(

        "analysis.html",

        name=name,

        income=income,

        budget=budget,

        total_expenses=total_expenses,

        total_budget=total_budget,

        remaining=remaining

    )


# ==========================================================
# HISTORY PAGE
# ==========================================================

@app.route("/history")
def history():

    connection = get_db_connection()

    history_data = connection.execute(
        """
        SELECT *

        FROM budget_history

        ORDER BY id DESC
        """
    ).fetchall()

    connection.close()


    return render_template(

        "history.html",

        history=history_data

    )


# ==========================================================
# VIEW HISTORY RESULT
# ==========================================================

@app.route("/result/<int:history_id>")
def history_result(
    history_id
):

    connection = get_db_connection()

    record = connection.execute(
        """
        SELECT *

        FROM budget_history

        WHERE id = ?
        """,

        (history_id,)

    ).fetchone()

    connection.close()


    # ------------------------------------------------------
    # RECORD NOT FOUND
    # ------------------------------------------------------

    if record is None:

        flash(
            "Budget record not found.",
            "error"
        )

        return redirect(
            url_for("history")
        )


    # ------------------------------------------------------
    # CREATE BUDGET DICTIONARY
    # ------------------------------------------------------

    budget = {

        "house_rent":
            record["house_rent"],

        "emi":
            record["emi"],

        "food_grocery":
            record["food_grocery"],

        "transportation":
            record["transportation"],

        "shopping":
            record["shopping"],

        "entertainment":
            record["entertainment"],

        "healthcare":
            record["healthcare"],

        "savings":
            record["savings"],

        "other_expenses":
            record["other_expenses"]

    }


    # ------------------------------------------------------
    # DISPLAY RESULT
    # ------------------------------------------------------

    return render_template(

        "result.html",

        name=record["name"],

        income=record["income"],

        budget=budget

    )


# ==========================================================
# DELETE HISTORY RECORD
# ==========================================================

@app.route(
    "/history/delete/<int:history_id>",
    methods=["POST"]
)
def delete_history(
    history_id
):

    connection = get_db_connection()

    connection.execute(
        """
        DELETE FROM budget_history

        WHERE id = ?
        """,

        (history_id,)

    )

    connection.commit()

    connection.close()


    flash(
        "Budget history deleted successfully.",
        "success"
    )


    return redirect(
        url_for("history")
    )


# ==========================================================
# CLEAR ALL HISTORY
# ==========================================================

@app.route(
    "/history/clear",
    methods=["POST"]
)
def clear_history():

    connection = get_db_connection()

    connection.execute(
        """
        DELETE FROM budget_history
        """
    )

    connection.commit()

    connection.close()


    flash(
        "All budget history has been cleared.",
        "success"
    )


    return redirect(
        url_for("history")
    )


# ==========================================================
# ABOUT PAGE
# ==========================================================

@app.route("/about")
def about():

    return render_template(
        "about.html"
    )


# ==========================================================
# RESET CURRENT PLAN
# ==========================================================

@app.route("/reset")
def reset():

    session.clear()

    flash(
        "Current budget plan has been cleared.",
        "success"
    )

    return redirect(
        url_for("planner")
    )


# ==========================================================
# ERROR HANDLERS
# ==========================================================

@app.errorhandler(404)
def page_not_found(error):

    return """

    <h1>404 - Page Not Found</h1>

    <p>
        The page you are looking for does not exist.
    </p>

    <a href="/">
        Go back to Home
    </a>

    """, 404


@app.errorhandler(500)
def internal_server_error(error):

    return """

    <h1>500 - Internal Server Error</h1>

    <p>
        Something went wrong on the server.
    </p>

    <a href="/">
        Go back to Home
    </a>

    """, 500


# ==========================================================
# INITIALIZE DATABASE
# ==========================================================

init_database()


# ==========================================================
# RUN APPLICATION
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True)