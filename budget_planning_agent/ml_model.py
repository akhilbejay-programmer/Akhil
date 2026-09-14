# ==========================================================
# AKHIL'S MONTHLY BUDGET PLANNER
# MACHINE LEARNING MODEL
# ==========================================================

from sklearn.linear_model import LinearRegression


# ==========================================================
# TRAINING DATA
# ==========================================================

salary = [
    10000,
    20000,
    30000,
    40000,
    50000,
    60000,
    70000,
    80000,
    90000,
    100000
]


house_rent = [
    2000,
    4000,
    6000,
    8000,
    10000,
    12000,
    14000,
    16000,
    18000,
    20000
]


emi = [
    1000,
    2000,
    3000,
    4000,
    5000,
    6000,
    7000,
    8000,
    9000,
    10000
]


food_grocery = [
    700,
    1400,
    2100,
    2800,
    3500,
    4200,
    4900,
    5600,
    6300,
    7000
]


transportation = [
    500,
    1000,
    1500,
    2000,
    2500,
    3000,
    3500,
    4000,
    4500,
    5000
]


shopping = [
    1000,
    2000,
    3000,
    4000,
    5000,
    6000,
    7000,
    8000,
    9000,
    10000
]


entertainment = [
    500,
    1000,
    1500,
    2000,
    2500,
    3000,
    3500,
    4000,
    4500,
    5000
]


healthcare = [
    1000,
    2000,
    3000,
    4000,
    5000,
    6000,
    7000,
    8000,
    9000,
    10000
]


savings = [
    3000,
    6000,
    9000,
    12000,
    15000,
    18000,
    21000,
    24000,
    27000,
    30000
]


other_expenses = [
    300,
    600,
    900,
    1200,
    1500,
    1800,
    2100,
    2400,
    2700,
    3000
]


# ==========================================================
# PREPARE INPUT DATA
# ==========================================================

X = [
    [value]
    for value in salary
]


# ==========================================================
# PREPARE OUTPUT DATA
# ==========================================================

Y = []

for i in range(len(salary)):

    Y.append([
        house_rent[i],
        emi[i],
        food_grocery[i],
        transportation[i],
        shopping[i],
        entertainment[i],
        healthcare[i],
        savings[i],
        other_expenses[i]
    ])


# ==========================================================
# TRAIN MODEL
# ==========================================================

model = LinearRegression()

model.fit(X, Y)


# ==========================================================
# BUDGET CATEGORY NAMES
# ==========================================================

CATEGORY_NAMES = [
    "house_rent",
    "emi",
    "food_grocery",
    "transportation",
    "shopping",
    "entertainment",
    "healthcare",
    "savings",
    "other_expenses"
]


# ==========================================================
# PREDICTION FUNCTION
# ==========================================================

def predict_budget(income):

    """
    Predict monthly budget based on monthly income.

    Parameters
    ----------
    income : float
        User's monthly income.

    Returns
    -------
    dict
        Predicted budget for all categories.
    """

    # ----------------------------------------------
    # Validate income
    # ----------------------------------------------

    if income is None:
        raise ValueError("Income is required.")

    try:
        income = float(income)

    except (ValueError, TypeError):
        raise ValueError("Income must be a valid number.")


    # ----------------------------------------------
    # Check positive income
    # ----------------------------------------------

    if income <= 0:
        raise ValueError("Income must be greater than zero.")


    # ----------------------------------------------
    # ML Prediction
    # ----------------------------------------------

    prediction = model.predict([[income]])


    # ----------------------------------------------
    # Convert prediction into dictionary
    # ----------------------------------------------

    predicted_values = prediction[0]


    budget = {

        "house_rent":
            round(float(predicted_values[0]), 2),

        "emi":
            round(float(predicted_values[1]), 2),

        "food_grocery":
            round(float(predicted_values[2]), 2),

        "transportation":
            round(float(predicted_values[3]), 2),

        "shopping":
            round(float(predicted_values[4]), 2),

        "entertainment":
            round(float(predicted_values[5]), 2),

        "healthcare":
            round(float(predicted_values[6]), 2),

        "savings":
            round(float(predicted_values[7]), 2),

        "other_expenses":
            round(float(predicted_values[8]), 2)

    }


    return budget


# ==========================================================
# TOTAL EXPENSE CALCULATION
# ==========================================================

def calculate_total_expenses(budget):

    """
    Calculate total expenses excluding savings.
    """

    total = (

        budget["house_rent"]

        + budget["emi"]

        + budget["food_grocery"]

        + budget["transportation"]

        + budget["shopping"]

        + budget["entertainment"]

        + budget["healthcare"]

        + budget["other_expenses"]

    )

    return round(total, 2)


# ==========================================================
# TOTAL BUDGET CALCULATION
# ==========================================================

def calculate_total_budget(budget):

    """
    Calculate all predicted categories including savings.
    """

    total = (

        budget["house_rent"]

        + budget["emi"]

        + budget["food_grocery"]

        + budget["transportation"]

        + budget["shopping"]

        + budget["entertainment"]

        + budget["healthcare"]

        + budget["savings"]

        + budget["other_expenses"]

    )

    return round(total, 2)


# ==========================================================
# COMPLETE BUDGET ANALYSIS
# ==========================================================

def get_budget_analysis(income):

    """
    Generate complete budget prediction and analysis.
    """

    income = float(income)

    budget = predict_budget(income)

    total_expenses = calculate_total_expenses(budget)

    total_budget = calculate_total_budget(budget)


    # Remaining amount after all predicted categories

    remaining = income - total_budget


    # Percentage calculation

    percentages = {}

    for category in CATEGORY_NAMES:

        percentages[category] = round(
            (budget[category] / income) * 100,
            2
        )


    return {

        "income": round(income, 2),

        "budget": budget,

        "total_expenses":
            total_expenses,

        "total_budget":
            total_budget,

        "remaining":
            round(remaining, 2),

        "percentages":
            percentages

    }


# ==========================================================
# TEST MODEL
# ==========================================================

if __name__ == "__main__":

    print("=" * 55)

    print("Akhil's Monthly Budget Planner")

    print("Machine Learning Model")

    print("=" * 55)


    test_income = 50000


    result = get_budget_analysis(test_income)


    print()

    print(
        f"Monthly Income: ₹{result['income']:,.2f}"
    )

    print()


    for category, amount in result["budget"].items():

        display_name = category.replace(
            "_",
            " "
        ).title()

        print(
            f"{display_name}: ₹{amount:,.2f}"
        )


    print()

    print(
        f"Total Expenses: "
        f"₹{result['total_expenses']:,.2f}"
    )

    print(
        f"Total Budget: "
        f"₹{result['total_budget']:,.2f}"
    )

    print(
        f"Remaining: "
        f"₹{result['remaining']:,.2f}"
    )

    print()

    print("=" * 55)