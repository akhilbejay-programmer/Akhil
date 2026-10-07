from flask import Flask, render_template


# ==========================================================
# FLASK APPLICATION
# ==========================================================

app = Flask(__name__)


# ==========================================================
# 8-WEEK CSP JOURNEY DATA
# ==========================================================

weeks = [
    {
        "week": 1,
        "title": "Sachivalayam Visit",
        "icon": "👥",
        "theme": "Nellore",
        "description": (
            "The first week Visited Sachivalayam "
        ),
        "activities": [
            "Day-1: visited sachivalayam to take permission for project",
            "Day-2: Conducted survey in Nellore dist",
            "Day-3: Conducted survey on food Habits and Nutrition",
            "Day-4: we enquired the persons and there daily food habits",
            "Day-5: we created awareness about the food habits",
            "Day-6: we visited the houses of our area"
        ],
        "learning": (
            "A balanced diet should include a variety of foods "
            "such as vegetables, fruits, grains and suitable protein sources."
        ),
        "awareness": (
            "Good nutrition is an important part of maintaining "
            "overall health and well-being."
        )
    },

    {
        "week": 2,
        "title": "Houses Visit",
        "icon": "🥗",
        "theme": "Prepared for awareness program",
        "description": (
            "The second week focused on awareness camp"
        ),
        "activities": [
            "Day-1: Prepared for speech on Nutrition",
            "Day-2: Conducted awareness program on food habits and nutrition",
            "Day-3: We explained to people how to maintain diet",
            "Day-4: We have explained to citizens about the blanced diet",
            "Day-5: We note the problems of citizens",
            "Day-6: Visited some houses in the part of survey"
        ],
        "learning": (
            "Choosing a variety of nutritious foods can support "
            "a balanced and healthy eating pattern."
        ),
        "awareness": (
            "Small improvements in daily food choices can contribute "
            "to healthier eating habits."
        )
    },

    {
        "week": 3,
        "title": "Awareness Program",
        "icon": "🍎",
        "theme": "Calculate BMI of people",
        "description": (
            "The third week focused on BMI of people"),
        "activities": [
                    "Day-1: Calculate the body mas index of people",
                    "Day-2: Measured the height and weight of people",
                    "Day-3: Calculate the body mas index of height and weight",
                    "Day-4: We gave information to the obesity people",
                    "Day-5: We gave information to the over weighted people",
                    "Day-6: Created awareness about BMI"
                ],
        "learning": (
            "Water is essential for normal body functions and "
            "maintaining hydration."
        ),
        "awareness": (
            "Regular fluid intake is an important part of everyday "
            "health and wellness."
        )
    },

    {
        "week": 4,
        "title": "Explanation of food habits and nutrition",
        "icon": "🏃",
        "theme": "Move Every Day exercises",
        "description": (
            "The fourth week focused on Exercises "
        ),
        "activities": [
                            "Day-1: visited some house in our area",
                            "Day-2: Conducted awareness on health diet",
                            "Day-3: explained about nutrition",
                            "Day-4: supplied some fruits to the people",
                            "Day-5: Given awareness about exercises",
                            "Day-6: Provied some fruits to aged people"
                        ],
        "learning": (
            "Regular physical activity supports physical fitness "
            "and contributes to overall well-being."
        ),
        "awareness": (
            "Simple activities such as walking can be included "
            "in everyday routines."
        )
    },

    {
        "week": 5,
        "title": "School Visite",
        "icon": "🧼",
        "theme": "KNR High School",
        "description": (
            "The fifth week focused on Visited High School"),
        "activities": [
                                    "Day-1: visited High School and taken permission",
                                    "Day-2: Given awareness to the school children",
                                    "Day-3: explained about nutrition",
                                    "Day-4: Conducted survey about there problems",
                                    "Day-5: Given awareness about exercises",
                                    "Day-6: visited primary school as a part of survvey"
                                ],
        "learning": (
            "Good hygiene practices can help reduce the risk of "
            "food contamination and illness."
        ),
        "awareness": (
            "Clean hands, clean utensils and safe food handling "
            "are important parts of healthy living."
        )
    },

    {
        "week": 6,
        "title": "Awareness at School",
        "icon": "🌱",
        "theme": "Final awareness campin in School",
        "description": (
            "The sixth week focused on awareness about excessive "
            "salt and free sugar consumption."
        ),
        "activities": [
                                            "Day-1: visited High School",
                                            "Day-2: Given awareness to children and parents",
                                            "Day-3: Explained about nutrition",
                                            "Day-4: Given information about diabetics",
                                            "Day-5: Again interacted with people",
                                            "Day-6: This is the last day of project, we took photographs"
                                        ],
        "learning": (
            "Reducing frequent consumption of foods and drinks "
            "high in free sugars and excessive salt can support "
            "healthier eating patterns."
        ),
        "awareness": (
            "Reading food labels can help people become more aware "
            "of salt and sugar content."
        )
    },

    {
        "week": 7,
        "title": "Website Development",
        "icon": "📅",
        "theme": "Building Webpage for CSP",
        "description": (
            "The seventh week brought nutrition, hydration, activity website"
        ),
        "activities": [
                                                    "Day-1: Designed a website for CSP",
                                                    "Day-2: Collected data and requirements",
                                                    "Day-3: Developed front-end website",
                                                    "Day-4: Developed back-end website",
                                                    "Day-5: Tested Final Output",
                                                    "Day-6: Finally Deployed in server"
                                                ],
        "learning": (
            "Healthy living involves several connected habits rather "
            "than depending on a single food or activity."
        ),
        "awareness": (
            "Consistent healthy habits can make everyday wellness "
            "easier to maintain."
        )
    },

    {
        "week": 8,
        "title": "Project Submission",
        "icon": "🎯",
        "theme": "Final work",
        "description": (
            "The final week focused on reviewing the eight-week journey and submission of project"
        ),
        "activities": [
                                                            "Day-1: Reviewing the project",
                                                            "Day-2: Collected data and requirements",
                                                            "Day-3: modified the Changes",
                                                            "Day-4: Tested Final Output",
                                                            "Day-5: Submitted to the Coordinator",
                                                            "Day-6: Successfully completed 8-weeks journey"
                                                        ],
        "learning": (
            "Health awareness is an ongoing process. The knowledge "
            "gained during the project can be applied in everyday life."
        ),
        "awareness": (
            "Healthy habits should be continued beyond the completion "
            "of the project."
        )
    }
]


# ==========================================================
# HOME
# ==========================================================

@app.route("/")
def index():
    return render_template(
        "index.html",
        weeks=weeks
    )


# ==========================================================
# 8-WEEK JOURNEY
# ==========================================================

@app.route("/journey")
def journey():
    return render_template(
        "journey.html",
        weeks=weeks
    )


# ==========================================================
# NUTRITION TIPS
# ==========================================================

@app.route("/tips")
def tips():
    return render_template(
        "tips.html"
    )


# ==========================================================
# ABOUT CSP
# ==========================================================

@app.route("/about")
def about():
    return render_template(
        "about.html"
    )


# ==========================================================
# RUN APPLICATION
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True)