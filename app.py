from flask import Flask, render_template, request

app = Flask(__name__)

# # SUBJECT DATA
# subjects = {
#     "DBMS": 5,
#     "OS": 4,
#     "Math": 3,
#     "AI": 2,
#     "CN": 3
# }

# TOOL 1
def get_subjects():
    return subjects

# TOOL 2
def calculate_plan(days, subjects):
    total_weight = sum(subjects.values())
    plan = {}

    for subject, weight in subjects.items():
        allocated_days = (weight / total_weight) * days
        plan[subject] = round(allocated_days)

    return plan

#Agent logic
def run_agent(user_goal, subjects_input, difficulty_input, days):
    logs = []
    

    # ----------------------------
    # Step 1: Parse subjects
    # ----------------------------
    logs.append("THOUGHT: Parsing subjects and difficulty")

    subjects_list = [s.strip() for s in subjects_input.split(",")]
    difficulty_list = [int(d.strip()) for d in difficulty_input.split(",")]

    subject_data = dict(zip(subjects_list, difficulty_list))

    logs.append(f"OBSERVATION: {subject_data}")

    # ----------------------------
    # Step 2: Calculate plan
    # ----------------------------
    logs.append("THOUGHT: Distributing time based on difficulty")

    total_weight = sum(subject_data.values())
    plan = {}

    for subject, weight in subject_data.items():
        allocated_days = (weight / total_weight) * int(days)
        plan[subject] = round(allocated_days)

    logs.append(f"ACTION: Calculator Tool → {plan}")

    return plan, logs


@app.route("/", methods=["GET", "POST"])
def home():
    plan = None
    logs = None

    if request.method == "POST":
        subjects = request.form["subjects"]
        difficulty = request.form["difficulty"]
        days = request.form["days"]

        plan, logs = run_agent("", subjects, difficulty, days)

    return render_template("index.html", plan=plan, logs=logs)


if __name__ == "__main__":
    app.run(debug=True)