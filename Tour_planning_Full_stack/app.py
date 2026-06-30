from flask import Flask, render_template, request

app = Flask(__name__)

# Import your India dictionary
from tour_data import india


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/tourist_places", methods=["GET", "POST"])
def tourist_places():
    if request.method == "POST":
        state = request.form["state"].strip()

        for s, places in india.items():
            if state.lower() == s.lower():
                total_budget = sum(places.values())

                return render_template(
                    "tourist_places.html",
                    state=s,
                    places=places,
                    total_budget=total_budget
                )

        return render_template(
            "tourist_places.html",
            error="No matching Indian state found."
        )

    return render_template("tourist_places.html")


@app.route("/make_plan", methods=["GET", "POST"])
def make_plan():

    if request.method == "POST":

        state = request.form["state"].strip()

        try:
            budget = int(request.form["budget"])
        except:
            return render_template(
                "make_plan.html",
                error="Please enter a valid budget."
            )

        for s, places in india.items():

            if state.lower() == s.lower():

                minimum = min(places.values())

                if budget < minimum:
                    return render_template(
                        "make_plan.html",
                        error=f"Minimum budget required is ₹{minimum}"
                    )

                remaining = budget

                selected_places = []

                for place, cost in sorted(
                        places.items(),
                        key=lambda x: (x[1], x[0])):

                    if cost <= remaining:
                        selected_places.append((place, cost))
                        remaining -= cost

                return render_template(
                    "result.html",
                    state=s,
                    budget=budget,
                    remaining=remaining,
                    selected_places=selected_places
                )

        return render_template(
            "make_plan.html",
            error="No matching Indian state found."
        )

    return render_template("make_plan.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)