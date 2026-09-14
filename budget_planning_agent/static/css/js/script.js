// ==========================================================
// AKHIL'S MONTHLY BUDGET PLANNER
// MAIN JAVASCRIPT
// ==========================================================


// ==========================================================
// PAGE LOADED
// ==========================================================

document.addEventListener("DOMContentLoaded", function () {

    console.log(
        "Akhil's Monthly Budget Planner loaded successfully."
    );


    // ------------------------------------------------------
    // AUTO HIDE FLASH MESSAGES
    // ------------------------------------------------------

    const flashMessages =
        document.querySelectorAll(".flash");


    flashMessages.forEach(function (message) {

        setTimeout(function () {

            message.style.transition =
                "opacity 0.5s ease";

            message.style.opacity = "0";


            setTimeout(function () {

                message.remove();

            }, 500);

        }, 4000);

    });


    // ------------------------------------------------------
    // INCOME INPUT VALIDATION
    // ------------------------------------------------------

    const incomeInput =
        document.getElementById("income");


    if (incomeInput) {

        incomeInput.addEventListener(
            "input",
            function () {

                if (this.value < 0) {

                    this.value = 0;

                }

            }
        );

    }


    // ------------------------------------------------------
    // PLANNER FORM
    // ------------------------------------------------------

    const plannerForm =
        document.querySelector(
            'form[action*="planner"]'
        );


    if (plannerForm) {

        plannerForm.addEventListener(
            "submit",
            function () {

                const name =
                    document.getElementById("name");

                const income =
                    document.getElementById("income");


                if (
                    name &&
                    name.value.trim() === ""
                ) {

                    alert(
                        "Please enter your name."
                    );

                    name.focus();

                    return;

                }


                if (
                    income &&
                    (
                        income.value === "" ||
                        Number(income.value) <= 0
                    )
                ) {

                    alert(
                        "Please enter a valid monthly income."
                    );

                    income.focus();

                    return;

                }

            }
        );

    }


    // ------------------------------------------------------
    // CONFIRM DELETE
    // ------------------------------------------------------

    const deleteForms =
        document.querySelectorAll(
            'form[action*="delete"]'
        );


    deleteForms.forEach(function (form) {

        form.addEventListener(
            "submit",
            function (event) {

                const confirmed =
                    confirm(
                        "Are you sure you want to delete this budget record?"
                    );


                if (!confirmed) {

                    event.preventDefault();

                }

            }
        );

    });


    // ------------------------------------------------------
    // CONFIRM CLEAR HISTORY
    // ------------------------------------------------------

    const clearForm =
        document.querySelector(
            'form[action*="clear"]'
        );


    if (clearForm) {

        clearForm.addEventListener(
            "submit",
            function (event) {

                const confirmed =
                    confirm(
                        "Are you sure you want to clear all budget history?"
                    );


                if (!confirmed) {

                    event.preventDefault();

                }

            }
        );

    }

});