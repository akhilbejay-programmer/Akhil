from flask import (
    Flask,
    render_template,
    request,
    session,
    redirect,
    url_for,
    flash
)

import random


# ==========================================================
# FLASK APPLICATION
# ==========================================================

app = Flask(__name__)

app.secret_key = "akki_vvm_secret_key"


# ==========================================================
# VEGETABLE DATA
# ==========================================================

vegetables = {

    1: {
        "name": "tomato",
        "price": 50 / 1000,
        "emoji": "🍅"
    },

    2: {
        "name": "potato",
        "price": 30 / 1000,
        "emoji": "🥔"
    },

    3: {
        "name": "onion",
        "price": 40 / 1000,
        "emoji": "🧅"
    },

    4: {
        "name": "carrot",
        "price": 60 / 1000,
        "emoji": "🥕"
    },

    5: {
        "name": "cabbage",
        "price": 45 / 1000,
        "emoji": "🥬"
    },

    6: {
        "name": "beetroot",
        "price": 70 / 1000,
        "emoji": "🫜"
    },

    7: {
        "name": "cauliflower",
        "price": 80 / 1000,
        "emoji": "🥦"
    },

    8: {
        "name": "brinjal",
        "price": 90 / 1000,
        "emoji": "🍆"
    },

    9: {
        "name": "capsicum",
        "price": 120 / 1000,
        "emoji": "🫑"
    },

    10: {
        "name": "spinach",
        "price": 20 / 1000,
        "emoji": "🌿"
    }
}


# ==========================================================
# BARGAINING MESSAGES
# ==========================================================

bargain_messages = {

    1: {
        "title": "That's a little too low! 😅",
        "reason": "Akki cannot accept such a low offer."
    },

    2: {
        "title": "Let's meet somewhere in the middle! 🤝",
        "reason": "Akki has reduced the price for you."
    },

    3: {
        "title": "One more special offer! 🎉",
        "reason": "Akki has reduced the price again."
    },

    4: {
        "title": "This is my final offer! 💰",
        "reason": "Akki has reached the final bargaining price."
    }
}


# ==========================================================
# CART FUNCTIONS
# ==========================================================

def get_cart():

    return session.get(
        "cart",
        []
    )


def save_cart(cart):

    session["cart"] = cart

    session.modified = True


def calculate_cart_total(cart):

    total = 0

    for item in cart:

        total += float(
            item.get(
                "total",
                0
            )
        )

    return round(
        total,
        2
    )


# ==========================================================
# CART COUNT
# ==========================================================

@app.context_processor
def inject_cart_count():

    cart = session.get(
        "cart",
        []
    )

    cart_count = sum(
        item.get(
            "quantity",
            0
        )
        for item in cart
    )

    return {
        "cart_count": cart_count
    }


# ==========================================================
# RANDOM AGENT PRICE
# ==========================================================
#
# IMPORTANT LOGIC
#
# FIRST VALUE:
#
#     95% <= agent price <= 100%
#
# NEXT VALUES:
#
#     95% <= next price < previous agent price
#
# Therefore the agent price can NEVER increase.
#
# Example:
#
# Original = ₹50
#
# Agent 1 = ₹49.20
# Agent 2 = ₹48.60
# Agent 3 = ₹48.10
# Agent 4 = ₹47.50
#
# ==========================================================

def generate_agent_price(
    original_total,
    previous_price=None,
    user_offer=None
):

    original_total = round(
        float(original_total),
        2
    )

    # ------------------------------------------------------
    # Minimum allowed agent price = 95%
    # ------------------------------------------------------

    minimum_price = round(
        original_total * 0.95,
        2
    )

    # ------------------------------------------------------
    # FIRST AGENT PRICE
    #
    # Random between 95% and 100%.
    # ------------------------------------------------------

    if previous_price is None:

        lower_cents = int(
            round(
                minimum_price * 100
            )
        )

        upper_cents = int(
            round(
                original_total * 100
            )
        )

    # ------------------------------------------------------
    # NEXT AGENT PRICE
    #
    # MUST BE LOWER THAN PREVIOUS VALUE.
    # ------------------------------------------------------

    else:

        previous_price = round(
            float(previous_price),
            2
        )

        lower_cents = int(
            round(
                minimum_price * 100
            )
        )

        # IMPORTANT:
        #
        # previous_price - 1 paise
        #
        # This guarantees:
        #
        # next_price < previous_price
        #

        upper_cents = int(
            round(
                previous_price * 100
            )
        ) - 1

    # ------------------------------------------------------
    # No valid range
    # ------------------------------------------------------

    if upper_cents < lower_cents:

        return round(
            minimum_price,
            2
        )

    # ------------------------------------------------------
    # Build valid values
    # ------------------------------------------------------

    possible_values = []

    for cents in range(
        lower_cents,
        upper_cents + 1
    ):

        value = round(
            cents / 100,
            2
        )

        # --------------------------------------------------
        # Don't match user offer
        # --------------------------------------------------

        if user_offer is not None:

            if value == round(
                float(user_offer),
                2
            ):

                continue

        # --------------------------------------------------
        # Don't match previous value
        # --------------------------------------------------

        if previous_price is not None:

            if value == round(
                float(previous_price),
                2
            ):

                continue

        possible_values.append(
            value
        )

    # ------------------------------------------------------
    # Choose random value
    # ------------------------------------------------------

    if possible_values:

        return random.choice(
            possible_values
        )

    # ------------------------------------------------------
    # Fallback
    # ------------------------------------------------------
    #
    # If there is no random value available,
    # use the minimum price.
    #
    # This still respects the 95% rule.
    #

    fallback = round(
        minimum_price,
        2
    )

    # If fallback equals user's offer,
    # try one paise below previous value.
    #

    if (
        user_offer is not None
        and fallback == round(
            float(user_offer),
            2
        )
    ):

        if previous_price is not None:

            alternative = round(
                float(previous_price) - 0.01,
                2
            )

            if alternative >= minimum_price:

                return alternative

    return fallback


# ==========================================================
# HOME PAGE
# ==========================================================

@app.route("/")
def index():

    return render_template(
        "index.html",
        vegetables=vegetables
    )


# ==========================================================
# PURCHASE
# ==========================================================

@app.route(
    "/purchase/<int:veg_id>",
    methods=["GET", "POST"]
)
def purchase(veg_id):

    # ------------------------------------------------------
    # CHECK VEGETABLE
    # ------------------------------------------------------

    if veg_id not in vegetables:

        flash(
            "Vegetable not found!",
            "error"
        )

        return redirect(
            url_for("index")
        )

    vegetable = vegetables[veg_id]

    # ------------------------------------------------------
    # GET
    # ------------------------------------------------------

    if request.method == "GET":

        return render_template(
            "purchase.html",
            vegetable=vegetable,
            veg_id=veg_id
        )

    # ------------------------------------------------------
    # GET QUANTITY
    # ------------------------------------------------------

    try:

        quantity = int(
            request.form.get(
                "quantity",
                0
            )
        )

    except (ValueError, TypeError):

        flash(
            "Please enter a valid quantity.",
            "error"
        )

        return render_template(
            "purchase.html",
            vegetable=vegetable,
            veg_id=veg_id
        )

    # ------------------------------------------------------
    # QUANTITY VALIDATION
    # ------------------------------------------------------

    if quantity <= 0:

        flash(
            "Quantity must be greater than 0.",
            "error"
        )

        return render_template(
            "purchase.html",
            vegetable=vegetable,
            veg_id=veg_id
        )

    if quantity < 100:

        flash(
            "Minimum quantity is 100 grams.",
            "error"
        )

        return render_template(
            "purchase.html",
            vegetable=vegetable,
            veg_id=veg_id
        )

    if quantity > 10000:

        flash(
            "Maximum quantity is 10,000 grams.",
            "error"
        )

        return render_template(
            "purchase.html",
            vegetable=vegetable,
            veg_id=veg_id
        )

    # ======================================================
    # ORIGINAL TOTAL
    # ======================================================

    original_total = round(
        vegetable["price"] * quantity,
        2
    )

    # ======================================================
    # GET CART
    # ======================================================

    cart = get_cart()

    # ======================================================
    # CREATE CART ITEM
    # ======================================================

    cart_item = {

        "veg_id": veg_id,

        "name": vegetable["name"],

        "emoji": vegetable["emoji"],

        "quantity": quantity,

        "price": vegetable["price"],

        "total": original_total,

        # Keep original price separately.
        #
        # This is important if the item is bargained.
        #

        "original_total": original_total
    }

    cart.append(
        cart_item
    )

    save_cart(
        cart
    )

    # ======================================================
    # CREATE PURCHASE SESSION
    # ======================================================

    session["purchase"] = {

        "veg_id": veg_id,

        "quantity": quantity,

        # Current/final price

        "actual_price": original_total,

        # Original price NEVER changes

        "original_total": original_total,

        "rate": vegetable["price"],

        "attempt": 0,

        "cart_index": len(cart) - 1,

        "previous_agent_price": None
    }

    # ------------------------------------------------------
    # Clear previous counter
    # ------------------------------------------------------

    session.pop(
        "last_counter_price",
        None
    )

    # ======================================================
    # DECISION PAGE
    # ======================================================

    return render_template(

        "decision.html",

        vegetable=vegetable,

        quantity=quantity,

        actual_total=original_total
    )


# ==========================================================
# CART PAGE
# ==========================================================

@app.route("/cart")
def cart():

    cart_items = get_cart()

    cart_total = calculate_cart_total(
        cart_items
    )

    return render_template(

        "cart.html",

        cart=cart_items,

        cart_total=cart_total
    )


# ==========================================================
# REMOVE FROM CART
# ==========================================================

@app.route(
    "/remove-from-cart/<int:index>",
    methods=["POST"]
)
def remove_from_cart(index):

    cart = get_cart()

    # ------------------------------------------------------
    # CHECK INDEX
    # ------------------------------------------------------

    if index < 0 or index >= len(cart):

        flash(
            "Cart item not found.",
            "error"
        )

        return redirect(
            url_for("cart")
        )

    # ------------------------------------------------------
    # REMOVE ITEM
    # ------------------------------------------------------

    removed_item = cart.pop(
        index
    )

    save_cart(
        cart
    )

    # ------------------------------------------------------
    # UPDATE ACTIVE PURCHASE INDEX
    # ------------------------------------------------------

    purchase_data = session.get(
        "purchase"
    )

    if purchase_data:

        current_index = purchase_data.get(
            "cart_index"
        )

        # Current item removed

        if current_index == index:

            session.pop(
                "purchase",
                None
            )

            session.pop(
                "last_counter_price",
                None
            )

        # Earlier item removed

        elif (
            current_index is not None
            and current_index > index
        ):

            purchase_data[
                "cart_index"
            ] = current_index - 1

            session["purchase"] = (
                purchase_data
            )

    flash(

        f"{removed_item['name'].title()} "
        "removed from cart.",

        "success"
    )

    return redirect(
        url_for("cart")
    )


# ==========================================================
# CLEAR CART
# ==========================================================

@app.route(
    "/clear-cart",
    methods=["POST"]
)
def clear_cart():

    session.pop(
        "cart",
        None
    )

    session.pop(
        "purchase",
        None
    )

    session.pop(
        "last_counter_price",
        None
    )

    flash(
        "Your cart has been cleared.",
        "success"
    )

    return redirect(
        url_for("cart")
    )


# ==========================================================
# START BARGAINING FROM CART
# ==========================================================

@app.route(
    "/bargain-item/<int:index>",
    methods=["GET"]
)
def bargain_item(index):

    cart = get_cart()

    # ------------------------------------------------------
    # VALIDATE INDEX
    # ------------------------------------------------------

    if index < 0 or index >= len(cart):

        flash(
            "Cart item not found.",
            "error"
        )

        return redirect(
            url_for("cart")
        )

    item = cart[index]

    veg_id = item["veg_id"]

    if veg_id not in vegetables:

        flash(
            "Vegetable not found.",
            "error"
        )

        return redirect(
            url_for("cart")
        )

    vegetable = vegetables[veg_id]

    quantity = int(
        item["quantity"]
    )

    # ------------------------------------------------------
    # IMPORTANT
    #
    # Get ORIGINAL PRICE.
    #
    # If item was previously discounted,
    # don't use discounted price as original.
    # ------------------------------------------------------

    original_total = round(

        float(
            item.get(
                "original_total",
                vegetable["price"] * quantity
            )
        ),

        2
    )

    current_total = round(

        float(
            item["total"]
        ),

        2
    )

    # ======================================================
    # CREATE PURCHASE
    # ======================================================

    session["purchase"] = {

        "veg_id": veg_id,

        "quantity": quantity,

        "actual_price": current_total,

        "original_total": original_total,

        "rate": vegetable["price"],

        "attempt": 0,

        "cart_index": index,

        "previous_agent_price": None
    }

    session.pop(
        "last_counter_price",
        None
    )

    return redirect(
        url_for("bargain")
    )


# ==========================================================
# BARGAINING
# ==========================================================

@app.route(
    "/bargain",
    methods=["GET", "POST"]
)
def bargain():

    purchase_data = session.get(
        "purchase"
    )

    # ------------------------------------------------------
    # CHECK PURCHASE
    # ------------------------------------------------------

    if not purchase_data:

        flash(
            "Please select a vegetable first.",
            "error"
        )

        return redirect(
            url_for("cart")
        )

    veg_id = purchase_data["veg_id"]

    quantity = int(
        purchase_data["quantity"]
    )

    # ------------------------------------------------------
    # ORIGINAL PRICE
    # ------------------------------------------------------
    #
    # This must remain unchanged throughout bargaining.
    #

    original_total = round(

        float(
            purchase_data.get(
                "original_total",
                purchase_data["actual_price"]
            )
        ),

        2
    )

    # ------------------------------------------------------
    # CHECK VEGETABLE
    # ------------------------------------------------------

    if veg_id not in vegetables:

        flash(
            "Vegetable not found.",
            "error"
        )

        return redirect(
            url_for("cart")
        )

    vegetable = vegetables[veg_id]

    # ======================================================
    # GET
    # ======================================================

    if request.method == "GET":

        return render_template(

            "bargain.html",

            vegetable=vegetable,

            quantity=quantity,

            actual_total=original_total,

            attempt=purchase_data.get(
                "attempt",
                0
            ),

            counter_price=session.get(
                "last_counter_price"
            )
        )

    # ======================================================
    # GET USER OFFER
    # ======================================================

    try:

        offer = round(

            float(
                request.form.get(
                    "offer",
                    0
                )
            ),

            2
        )

    except (ValueError, TypeError):

        flash(
            "Please enter a valid offer.",
            "error"
        )

        return redirect(
            url_for("bargain")
        )

    # ======================================================
    # OFFER MUST BE POSITIVE
    # ======================================================

    if offer <= 0:

        flash(
            "Offer must be greater than ₹0.",
            "error"
        )

        return redirect(
            url_for("bargain")
        )

    # ======================================================
    # USER OFFER GREATER THAN ORIGINAL PRICE
    # ======================================================
    #
    # IMPORTANT:
    #
    # We DO NOT accept it.
    #
    # We DO NOT continue bargaining.
    #
    # We simply stop this offer and ask for another
    # valid offer.
    #
    # The process does NOT create a new agent value.
    #
    # ======================================================

    if offer > original_total:

        flash(

            f"Your offer cannot be greater than "
            f"the original price of ₹{original_total:.2f}.",

            "error"
        )

        return redirect(
            url_for("bargain")
        )

    # ======================================================
    # GET CURRENT AGENT VALUE
    # ======================================================

    current_agent_price = session.get(
        "last_counter_price"
    )

    # ======================================================
    # FIRST AGENT VALUE
    # ======================================================

    if current_agent_price is None:

        current_agent_price = generate_agent_price(

            original_total,

            previous_price=None,

            user_offer=offer
        )

        session[
            "last_counter_price"
        ] = current_agent_price

    else:

        current_agent_price = round(

            float(
                current_agent_price
            ),

            2
        )

    # ======================================================
    # USER OFFER >= AGENT VALUE
    # ======================================================
    #
    # Agent accepts customer's offer.
    #
    # Example:
    #
    # Original = ₹50
    # Agent    = ₹48.50
    # User     = ₹49
    #
    # Result:
    #
    # ACCEPT ₹49
    # ↓
    # BILLING
    #
    # ======================================================

    if offer >= current_agent_price:

        final_price = round(
            offer,
            2
        )

        cart = get_cart()

        cart_index = purchase_data.get(
            "cart_index"
        )

        # --------------------------------------------------
        # CHECK CART ITEM
        # --------------------------------------------------

        if (
            cart_index is None
            or cart_index < 0
            or cart_index >= len(cart)
        ):

            flash(
                "Cart item could not be found.",
                "error"
            )

            return redirect(
                url_for("cart")
            )

        # --------------------------------------------------
        # UPDATE CART PRICE
        #
        # DON'T REMOVE ITEM.
        # --------------------------------------------------

        cart[cart_index][
            "total"
        ] = final_price

        save_cart(
            cart
        )

        # --------------------------------------------------
        # UPDATE PURCHASE
        # --------------------------------------------------

        purchase_data[
            "actual_price"
        ] = final_price

        session["purchase"] = (
            purchase_data
        )

        session[
            "last_counter_price"
        ] = final_price

        # ==================================================
        # GO TO BILLING
        # ==================================================

        return render_template(

            "billing.html",

            vegetable=vegetable,

            quantity=quantity,

            final_price=final_price,

            bargained=True,

            accepted_offer=True,

            cart_total=calculate_cart_total(
                cart
            ),

            checkout_mode=False,

            preview=True
        )

    # ======================================================
    # USER OFFER IS LOWER THAN AGENT
    # ======================================================
    #
    # Continue bargaining.
    #
    # ======================================================

    attempt = (

        purchase_data.get(
            "attempt",
            0
        ) + 1
    )

    purchase_data[
        "attempt"
    ] = attempt

    # ======================================================
    # FINAL ATTEMPT
    # ======================================================
    #
    # On attempt 4, keep the current agent value.
    #
    # ======================================================

    if attempt >= 4:

        final_agent_price = round(

            float(
                current_agent_price
            ),

            2
        )

        purchase_data[
            "final_agent_price"
        ] = final_agent_price

        purchase_data[
            "actual_price"
        ] = final_agent_price

        purchase_data[
            "previous_agent_price"
        ] = final_agent_price

        session["purchase"] = (
            purchase_data
        )

        session[
            "last_counter_price"
        ] = final_agent_price

        return render_template(

            "bargain_closed.html",

            vegetable=vegetable,

            quantity=quantity,

            offer=offer,

            counter_price=final_agent_price
        )

    # ======================================================
    # GENERATE NEXT AGENT PRICE
    # ======================================================
    #
    # VERY IMPORTANT:
    #
    # previous_price = current_agent_price
    #
    # This guarantees:
    #
    # next_agent_price < current_agent_price
    #
    # ======================================================

    next_agent_price = generate_agent_price(

        original_total,

        previous_price=current_agent_price,

        user_offer=offer
    )

    # ======================================================
    # SAFETY CHECK
    # ======================================================
    #
    # Never allow agent price to increase.
    #
    # ======================================================

    if next_agent_price >= current_agent_price:

        next_agent_price = round(

            current_agent_price - 0.01,

            2
        )

        # Never go below 95%.

        minimum_price = round(

            original_total * 0.95,

            2
        )

        if next_agent_price < minimum_price:

            next_agent_price = minimum_price

    # ======================================================
    # SAVE AGENT PRICE
    # ======================================================

    purchase_data[
        "previous_agent_price"
    ] = next_agent_price

    session["purchase"] = (
        purchase_data
    )

    session[
        "last_counter_price"
    ] = next_agent_price

    # ======================================================
    # BARGAINING MESSAGE
    # ======================================================

    message = bargain_messages.get(

        attempt,

        bargain_messages[3]
    )

    response_title = (
        message["title"]
    )

    response_reason = (
        message["reason"]
    )

    # ======================================================
    # SHOW BARGAINING RESULT
    # ======================================================

    return render_template(

        "bargain.html",

        vegetable=vegetable,

        quantity=quantity,

        actual_total=original_total,

        attempt=attempt,

        offer=offer,

        response_title=response_title,

        response_reason=response_reason,

        counter_price=next_agent_price
    )


# ==========================================================
# ACCEPT AGENT COUNTER
# ==========================================================

@app.route(
    "/accept-counter",
    methods=["POST"]
)
def accept_counter():

    purchase_data = session.get(
        "purchase"
    )

    # ------------------------------------------------------
    # CHECK PURCHASE
    # ------------------------------------------------------

    if not purchase_data:

        flash(
            "No active purchase found.",
            "error"
        )

        return redirect(
            url_for("cart")
        )

    veg_id = purchase_data["veg_id"]

    quantity = int(
        purchase_data["quantity"]
    )

    cart_index = purchase_data.get(
        "cart_index"
    )

    final_price = session.get(
        "last_counter_price"
    )

    # ------------------------------------------------------
    # CHECK COUNTER
    # ------------------------------------------------------

    if final_price is None:

        flash(
            "No counter offer available.",
            "error"
        )

        return redirect(
            url_for("bargain")
        )

    final_price = round(

        float(
            final_price
        ),

        2
    )

    # ------------------------------------------------------
    # CHECK VEGETABLE
    # ------------------------------------------------------

    if veg_id not in vegetables:

        flash(
            "Vegetable not found.",
            "error"
        )

        return redirect(
            url_for("cart")
        )

    vegetable = vegetables[veg_id]

    # ======================================================
    # GET CART
    # ======================================================

    cart = get_cart()

    # ======================================================
    # UPDATE CART
    #
    # DO NOT REMOVE ITEM.
    # ======================================================

    if (
        cart_index is not None
        and 0 <= cart_index < len(cart)
    ):

        cart[cart_index][
            "total"
        ] = final_price

        save_cart(
            cart
        )

    else:

        flash(
            "Cart item could not be found.",
            "error"
        )

        return redirect(
            url_for("cart")
        )

    # ======================================================
    # UPDATE PURCHASE
    # ======================================================

    purchase_data[
        "actual_price"
    ] = final_price

    session["purchase"] = (
        purchase_data
    )

    # ======================================================
    # BILLING PREVIEW
    # ======================================================

    return render_template(

        "billing.html",

        vegetable=vegetable,

        quantity=quantity,

        final_price=final_price,

        bargained=True,

        accepted_offer=False,

        cart_total=calculate_cart_total(
            cart
        ),

        preview=True
    )


# ==========================================================
# CHECKOUT
# ==========================================================

@app.route("/checkout")
def checkout():

    cart_items = get_cart()

    # ------------------------------------------------------
    # EMPTY CART
    # ------------------------------------------------------

    if not cart_items:

        flash(
            "Your cart is empty.",
            "error"
        )

        return redirect(
            url_for("index")
        )

    # ------------------------------------------------------
    # PROCESS FIRST CART ITEM
    # ------------------------------------------------------

    item = cart_items[0]

    veg_id = item["veg_id"]

    quantity = int(
        item["quantity"]
    )

    final_price = round(

        float(
            item["total"]
        ),

        2
    )

    # ------------------------------------------------------
    # ORIGINAL TOTAL
    # ------------------------------------------------------

    original_total = round(

        float(
            item.get(
                "original_total",
                vegetables[veg_id]["price"] * quantity
            )
        ),

        2
    )

    # ------------------------------------------------------
    # CHECK VEGETABLE
    # ------------------------------------------------------

    if veg_id not in vegetables:

        flash(
            "Vegetable not found.",
            "error"
        )

        return redirect(
            url_for("cart")
        )

    vegetable = vegetables[veg_id]

    # ======================================================
    # CREATE CHECKOUT SESSION
    # ======================================================

    session["purchase"] = {

        "veg_id": veg_id,

        "quantity": quantity,

        "actual_price": final_price,

        "original_total": original_total,

        "rate": vegetable["price"],

        "attempt": 0,

        "cart_index": 0,

        "previous_agent_price": None
    }

    session.pop(
        "last_counter_price",
        None
    )

    # ======================================================
    # BILLING PREVIEW
    # ======================================================

    return render_template(

        "billing.html",

        vegetable=vegetable,

        quantity=quantity,

        final_price=final_price,

        bargained=False,

        checkout_mode=True,

        cart_total=calculate_cart_total(
            cart_items
        )
    )


# ==========================================================
# FINAL BILLING
# ==========================================================

@app.route(
    "/billing",
    methods=["POST"]
)
def billing():

    purchase_data = session.get(
        "purchase"
    )

    # ------------------------------------------------------
    # CHECK PURCHASE
    # ------------------------------------------------------

    if not purchase_data:

        flash(
            "No active checkout found.",
            "error"
        )

        return redirect(
            url_for("cart")
        )

    veg_id = purchase_data["veg_id"]

    quantity = int(
        purchase_data["quantity"]
    )

    cart_index = purchase_data.get(
        "cart_index"
    )

    final_price = round(

        float(
            purchase_data["actual_price"]
        ),

        2
    )

    # ------------------------------------------------------
    # CHECK VEGETABLE
    # ------------------------------------------------------

    if veg_id not in vegetables:

        flash(
            "Vegetable not found.",
            "error"
        )

        return redirect(
            url_for("cart")
        )

    vegetable = vegetables[veg_id]

    # ======================================================
    # GET CART
    # ======================================================

    cart = get_cart()

    # ======================================================
    # FINALIZE ORDER
    #
    # ONLY HERE ITEM IS REMOVED.
    # ======================================================

    if (
        cart_index is not None
        and 0 <= cart_index < len(cart)
    ):

        completed_item = cart.pop(
            cart_index
        )

        save_cart(
            cart
        )

    else:

        flash(
            "Checkout item could not be found.",
            "error"
        )

        return redirect(
            url_for("cart")
        )

    # ======================================================
    # CLEAR PURCHASE
    # ======================================================

    session.pop(
        "purchase",
        None
    )

    session.pop(
        "last_counter_price",
        None
    )

    # ======================================================
    # FINAL BILLING PAGE
    # ======================================================

    return render_template(

        "billing.html",

        vegetable=vegetable,

        quantity=quantity,

        final_price=final_price,

        bargained=False,

        completed=True,

        cart_total=calculate_cart_total(
            cart
        )
    )


# ==========================================================
# NEW PURCHASE
# ==========================================================

@app.route("/new-purchase")
def new_purchase():

    # ------------------------------------------------------
    # CLEAR ACTIVE PURCHASE ONLY
    # ------------------------------------------------------

    session.pop(
        "purchase",
        None
    )

    session.pop(
        "last_counter_price",
        None
    )

    # ------------------------------------------------------
    # KEEP CART
    # ------------------------------------------------------

    return redirect(
        url_for("index")
    )


# ==========================================================
# RUN APPLICATION
# ==========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )