import json
import random
from datetime import datetime
import streamlit as st
import streamlit.components.v1 as components

WEAK_CATEGORIES = [
    "Classical Music",
    "World History",
    "Science",
    "Literature",
    "Language / Vocabulary",
    "Theatre",
    "Art",
    "Math",
    "Opera",
    "Shakespeare",
    "Bible",
    "Philosophy",
]

# --------------------
# Page setup
# --------------------

st.set_page_config(
    page_title="Canon",
    page_icon="🎯",
    layout="centered"
)


# --------------------
# Helper functions
# --------------------

def get_display_mode():
    if st.session_state.category_filter == "Weak Spots":
        return "Weak Spots"

    if st.session_state.category_filter == "Active Misses":
        return "Active Misses"

    if st.session_state.category_filter == "Daily 20":
        return "Daily 20"

    if st.session_state.category_filter == "Anytime Test":
        return "Anytime Test"

    return st.session_state.session_mode

def is_anytime_test_mode():
    return st.session_state.category_filter == "Anytime Test"

def load_questions():
    with open("data/questions.json", "r", encoding="utf-8") as file:
        return json.load(file)


def clean_answer(text):
    return text.strip().lower()


def is_correct(user_answer, question):
    accepted_answers = [question["answer"]] + question.get("aliases", [])

    return clean_answer(user_answer) in [
        clean_answer(answer) for answer in accepted_answers
    ]


def reset_quiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.results = []
    st.session_state.submitted = False
    st.session_state.last_answer = ""
    st.session_state.last_correct = False
    st.session_state.session_history_saved = False
    st.session_state.session_mode = "Practice"

    if "session_length" not in st.session_state:
        st.session_state.session_length = min(10, len(questions))

    if "difficulty_mode" not in st.session_state:
        st.session_state.difficulty_mode = "All"

    if "category_filter" not in st.session_state:
        st.session_state.category_filter = "All"

    eligible_question_indexes = []

    active_missed_question_ids = get_active_missed_question_ids()

    if st.session_state.category_filter == "Daily 20":
        active_miss_indexes = []
        weak_spot_indexes = []

        for index, question in enumerate(questions):
            if question["id"] in active_missed_question_ids:
                active_miss_indexes.append(index)
            elif question["category"] in WEAK_CATEGORIES:
                weak_spot_indexes.append(index)

        random.shuffle(active_miss_indexes)
        random.shuffle(weak_spot_indexes)

        daily_20_indexes = active_miss_indexes[:10] + weak_spot_indexes[:10]

        random.shuffle(daily_20_indexes)

        st.session_state.eligible_question_count = len(daily_20_indexes)
        st.session_state.question_order = daily_20_indexes[:20]

        return

    if st.session_state.category_filter == "Anytime Test":
        difficulty_1_indexes = []
        difficulty_2_indexes = []
        difficulty_3_indexes = []

        for index, question in enumerate(questions):
            difficulty = question["difficulty"]

            if difficulty == 1:
                difficulty_1_indexes.append(index)
            elif difficulty == 2:
                difficulty_2_indexes.append(index)
            elif difficulty >= 3:
                difficulty_3_indexes.append(index)

        random.shuffle(difficulty_1_indexes)
        random.shuffle(difficulty_2_indexes)
        random.shuffle(difficulty_3_indexes)

        anytime_indexes = (
            difficulty_1_indexes[:5]
            + difficulty_2_indexes[:25]
            + difficulty_3_indexes[:20]
        )

        random.shuffle(anytime_indexes)

        st.session_state.eligible_question_count = len(anytime_indexes)
        st.session_state.question_order = anytime_indexes[:50]

        return

    for index, question in enumerate(questions):
        difficulty = question["difficulty"]
        category = question["category"]

        difficulty_matches = (
            st.session_state.difficulty_mode == "All"
            or st.session_state.difficulty_mode == "Warmup" and difficulty <= 2
            or st.session_state.difficulty_mode == "Challenge" and difficulty >= 3
        )

        category_matches = (
            st.session_state.category_filter == "All"
            or st.session_state.category_filter == category
            or (
                st.session_state.category_filter == "Weak Spots"
                and category in WEAK_CATEGORIES
            )
            or (
                st.session_state.category_filter == "Active Misses"
                and question["id"] in active_missed_question_ids
            )
        )

        if difficulty_matches and category_matches:
            eligible_question_indexes.append(index)

    st.session_state.eligible_question_count = len(eligible_question_indexes)

    random.shuffle(eligible_question_indexes)

    actual_session_length = min(
        st.session_state.session_length,
        len(eligible_question_indexes)
    )

    st.session_state.question_order = eligible_question_indexes[
        :actual_session_length
    ]


def submit_answer(user_answer, question):
    correct = is_correct(user_answer, question)

    if correct:
        st.session_state.score += 1

    st.session_state.results.append(
        {
            "question_id": question["id"],
            "question": question["question"],
            "user_answer": user_answer,
            "correct_answer": question["answer"],
            "was_correct": correct,
            "category": question["category"]
        }
    )

    st.session_state.submitted = True
    st.session_state.last_answer = user_answer
    st.session_state.last_correct = correct


def go_to_next_question():
    st.session_state.current_question += 1
    st.session_state.submitted = False
    st.session_state.last_answer = ""
    st.session_state.last_correct = False
def start_missed_questions_practice():
    missed_question_ids = []

    for result in st.session_state.results:
        if not result["was_correct"]:
            missed_question_ids.append(result["question_id"])

    missed_question_indexes = []

    for index, question in enumerate(questions):
        if question["id"] in missed_question_ids:
            missed_question_indexes.append(index)

    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.results = []
    st.session_state.submitted = False
    st.session_state.last_answer = ""
    st.session_state.last_correct = False
    st.session_state.session_history_saved = False
    st.session_state.session_mode = "Missed Questions"
    st.session_state.question_order = missed_question_indexes
def load_session_history():
    with open("data/session_history.json", "r", encoding="utf-8") as file:
        return json.load(file)

def get_active_missed_question_ids():
    history = load_session_history()

    missed_counts = {}

    for session in history:
        for question_id in session.get("missed_question_ids", []):
            if question_id not in missed_counts:
                missed_counts[question_id] = 0

            missed_counts[question_id] += 1

    active_missed_ids = []

    for question_id, count in missed_counts.items():
        active_missed_ids.append(question_id)

    return active_missed_ids

def save_session_history():
    history = load_session_history()

    total_questions = len(st.session_state.question_order)

    if total_questions > 0:
        accuracy = round((st.session_state.score / total_questions) * 100)
    else:
        accuracy = 0

    missed_question_ids = []

    for result in st.session_state.results:
        if not result["was_correct"]:
            missed_question_ids.append(result["question_id"])

    session_record = {
    "date": datetime.now().isoformat(timespec="seconds"),
    "score": st.session_state.score,
    "total_questions": total_questions,
    "accuracy": accuracy,
    "display_mode": get_display_mode(),
    "difficulty_mode": st.session_state.difficulty_mode,
    "category_filter": st.session_state.category_filter,
    "missed_question_ids": missed_question_ids,
    "results": st.session_state.results
}

    history.append(session_record)

    with open("data/session_history.json", "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)
def show_recent_sessions():
    history = load_session_history()

    st.sidebar.divider()
    st.sidebar.subheader("Recent Sessions")

    if len(history) == 0:
        st.sidebar.write("No sessions yet.")
        return

    recent_sessions = history[-5:]
    recent_sessions.reverse()

    for session in recent_sessions:
        date = session["date"][:10]
        score = session["score"]
        total = session["total_questions"]
        accuracy = session["accuracy"]
        display_mode = session.get("display_mode", "Practice")

        st.sidebar.write(
            f"{date}: {display_mode} — **{score}/{total}** — {accuracy}%"
        )
def show_most_missed_questions():
    history = load_session_history()

    missed_counts = {}

    for session in history:
        for question_id in session["missed_question_ids"]:
            if question_id not in missed_counts:
                missed_counts[question_id] = 0

            missed_counts[question_id] += 1

    st.sidebar.divider()
    st.sidebar.subheader("Most Missed")

    if len(missed_counts) == 0:
        st.sidebar.write("No misses yet.")
        return

    sorted_misses = sorted(
        missed_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for question_id, count in sorted_misses[:5]:
        matching_question = None

        for question in questions:
            if question["id"] == question_id:
                matching_question = question
                break

        if matching_question:
            st.sidebar.write(
                f"{matching_question['category']}: {matching_question['answer']} — missed {count}x"
            )
def show_weakest_categories():
    history = load_session_history()

    category_stats = {}

    for session in history:
        if "results" not in session:
            continue

        for result in session["results"]:
            category = result["category"]

            if category not in category_stats:
                category_stats[category] = {
                    "correct": 0,
                    "total": 0
                }

            category_stats[category]["total"] += 1

            if result["was_correct"]:
                category_stats[category]["correct"] += 1

    st.sidebar.divider()
    st.sidebar.subheader("Weakest Categories")

    if len(category_stats) == 0:
        st.sidebar.write("No category history yet.")
        return

    category_accuracies = []

    for category, stats in category_stats.items():
        correct = stats["correct"]
        total = stats["total"]
        accuracy = round((correct / total) * 100)

        category_accuracies.append(
            {
                "category": category,
                "correct": correct,
                "total": total,
                "accuracy": accuracy
            }
        )

    category_accuracies.sort(
        key=lambda item: item["accuracy"]
    )

    for item in category_accuracies[:5]:
        st.sidebar.write(
            f"{item['category']}: **{item['accuracy']}%** "
            f"({item['correct']}/{item['total']})"
        )

def get_category_stats(results):
    category_stats = {}

    for result in results:
        category = result["category"]

        if category not in category_stats:
            category_stats[category] = {
                "correct": 0,
                "total": 0
            }

        category_stats[category]["total"] += 1

        if result["was_correct"]:
            category_stats[category]["correct"] += 1

    return category_stats

def show_training_dashboard():
    history = load_session_history()

    st.subheader("Training Dashboard")

    if len(history) == 0:
        st.write("No completed sessions yet.")
        return

    total_sessions = len(history)
    total_correct = 0
    total_questions = 0
    total_misses = 0

    for session in history:
        total_correct += session["score"]
        total_questions += session["total_questions"]
        total_misses += len(session["missed_question_ids"])

    if total_questions > 0:
        lifetime_accuracy = round((total_correct / total_questions) * 100)
    else:
        lifetime_accuracy = 0

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Sessions", total_sessions)
    col2.metric("Lifetime Accuracy", f"{lifetime_accuracy}%")
    col3.metric("Questions Answered", total_questions)
    col4.metric("Total Misses", total_misses)

    st.divider()
def show_question_bank_health():
    total_questions = len(questions)

    ids = []
    duplicate_ids = []
    missing_answers = 0
    missing_categories = 0
    missing_aliases = 0

    for question in questions:
        question_id = question["id"]

        if question_id in ids:
            duplicate_ids.append(question_id)

        ids.append(question_id)

        if "answer" not in question or question["answer"] == "":
            missing_answers += 1

        if "category" not in question or question["category"] == "":
            missing_categories += 1

        if "aliases" not in question:
            missing_aliases += 1

    st.sidebar.divider()
    st.sidebar.subheader("Question Bank")

    st.sidebar.write(f"Total questions: **{total_questions}**")

    if len(duplicate_ids) == 0:
        st.sidebar.write("Duplicate IDs: **0**")
    else:
        st.sidebar.error(f"Duplicate IDs: {duplicate_ids}")

    if missing_answers == 0:
        st.sidebar.write("Missing answers: **0**")
    else:
        st.sidebar.error(f"Missing answers: {missing_answers}")

    if missing_categories == 0:
        st.sidebar.write("Missing categories: **0**")
    else:
        st.sidebar.error(f"Missing categories: {missing_categories}")

    if missing_aliases == 0:
        st.sidebar.write("Missing alias fields: **0**")
    else:
        st.sidebar.warning(f"Missing alias fields: {missing_aliases}")
def show_question_bank_by_category():
    category_counts = {}

    for question in questions:
        category = question["category"]

        if category not in category_counts:
            category_counts[category] = 0

        category_counts[category] += 1

    st.sidebar.divider()
    st.sidebar.subheader("Bank by Category")

    sorted_categories = sorted(
        category_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for category, count in sorted_categories:
        st.sidebar.write(f"{category}: **{count}**")

def show_anytime_timer(question_number):
    components.html(
        f"""
        <div style="
            font-family: sans-serif;
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 8px;
        ">
            Time remaining: <span id="canon-timer">15</span>
        </div>

        <script>
        const timerKey = "{question_number}";
        let timeLeft = 15;

        const timerElement = document.getElementById("canon-timer");

        const countdown = setInterval(() => {{
            timeLeft -= 1;

            if (timerElement) {{
                timerElement.textContent = timeLeft;
            }}

            if (timeLeft <= 0) {{
                clearInterval(countdown);

                const doc = window.parent.document;
                const buttons = Array.from(doc.querySelectorAll("button"));

                const timeExpiredButton = buttons.find(button =>
                    button.innerText.trim() === "Time Expired"
                );

                if (timeExpiredButton) {{
                    timeExpiredButton.click();
                }}
            }}
        }}, 1000);
        </script>
        """,
        height=45
    )

def focus_answer_box(focus_key=""):
    components.html(
        f"""
        <script>
        const canonFocusKey = "{focus_key}";

        let attempts = 0;

        const focusInterval = setInterval(() => {{
            attempts += 1;

            const doc = window.parent.document;

            const inputs = Array.from(
                doc.querySelectorAll("input[type='text'], textarea")
            );

            const visibleInputs = inputs.filter(input => {{
                const style = window.parent.getComputedStyle(input);

                return (
                    !input.disabled &&
                    input.offsetParent !== null &&
                    style.visibility !== "hidden" &&
                    style.display !== "none"
                );
            }});

            const answerInput = visibleInputs[visibleInputs.length - 1];

            if (answerInput) {{
                answerInput.focus();
                answerInput.click();
                clearInterval(focusInterval);
            }}

            if (attempts >= 30) {{
                clearInterval(focusInterval);
            }}
        }}, 100);
        </script>
        """,
        height=0
    )


def enable_enter_for_next_question():
    components.html(
        """
        <script>
        setTimeout(() => {
            const doc = window.parent.document;

            const buttons = Array.from(doc.querySelectorAll("button"));

            const nextButton = buttons.find(button =>
                button.innerText.trim() === "Next Question"
            );

            if (nextButton) {
                nextButton.focus();
            }

            if (!window.parent.__canonEnterNextInstalled) {
                window.parent.__canonEnterNextInstalled = true;

                doc.addEventListener("keydown", function(event) {
                    const activeElement = doc.activeElement;
                    const tagName = activeElement ? activeElement.tagName.toLowerCase() : "";

                    const userIsTyping =
                        tagName === "input" ||
                        tagName === "textarea" ||
                        activeElement?.isContentEditable;

                    if (event.key === "Enter" && !userIsTyping) {
                        const buttons = Array.from(doc.querySelectorAll("button"));

                        const nextButton = buttons.find(button =>
                            button.innerText.trim() === "Next Question"
                        );

                        if (nextButton) {
                            event.preventDefault();
                            nextButton.click();
                        }
                    }
                });
            }
        }, 250);
        </script>
        """,
        height=0
    )

# --------------------
# Load data
# --------------------

questions = load_questions()


# --------------------
# Session state
# --------------------

if "current_question" not in st.session_state:
    reset_quiz()


# --------------------
# App header
# --------------------

st.title("🎯 Canon")
st.caption("Jeopardy training, one clue at a time.")

show_training_dashboard()

# --------------------
# Sidebar
# --------------------

st.sidebar.title("Canon")
st.sidebar.write(f"{get_display_mode()} Mode")
session_length_label = st.sidebar.selectbox(
    "Session Length",
    options=["10 questions", "20 questions", "All questions"]
)

if session_length_label == "10 questions":
    selected_session_length = min(10, len(questions))
elif session_length_label == "20 questions":
    selected_session_length = min(20, len(questions))
else:
    selected_session_length = len(questions)

if selected_session_length != st.session_state.session_length:
    st.session_state.session_length = selected_session_length
    reset_quiz()
    st.rerun()
difficulty_mode = st.sidebar.selectbox(
    "Difficulty",
    options=["All", "Warmup", "Challenge"]
)

if difficulty_mode != st.session_state.difficulty_mode:
    st.session_state.difficulty_mode = difficulty_mode
    reset_quiz()
    st.rerun()
categories = sorted(set(question["category"] for question in questions))
category_options = ["All", "Weak Spots", "Active Misses", "Daily 20", "Anytime Test"] + categories

category_filter = st.sidebar.selectbox(
    "Category",
    options=category_options
)

if category_filter != st.session_state.category_filter:
    st.session_state.category_filter = category_filter
    reset_quiz()
    st.rerun()
questions_answered = len(st.session_state.results)

if questions_answered > 0:
    accuracy = round((st.session_state.score / questions_answered) * 100)
else:
    accuracy = 0

if is_anytime_test_mode():
    st.sidebar.write("Score hidden until test is complete.")
else:
    st.sidebar.metric("Score", st.session_state.score)
    st.sidebar.metric("Accuracy", f"{accuracy}%")

st.sidebar.metric(
    "Question",
    f"{min(st.session_state.current_question + 1, len(st.session_state.question_order))} / {len(st.session_state.question_order)}"
)
st.sidebar.write(f"Difficulty: **{st.session_state.difficulty_mode}**")
st.sidebar.write(f"Category: **{st.session_state.category_filter}**")
st.sidebar.write(
    f"Available Questions: **{st.session_state.eligible_question_count}**"
)

if st.sidebar.button("Start New Session / Shuffle"):
    reset_quiz()
    st.rerun()

show_recent_sessions()
show_most_missed_questions()
show_weakest_categories()
show_question_bank_health()
show_question_bank_by_category()
# --------------------
# No eligible questions
# --------------------

if len(st.session_state.question_order) == 0:
    st.warning("No questions match your current filters.")

    st.write("Try changing the category, difficulty, or session length.")

    if st.button("Reset Filters"):
        st.session_state.difficulty_mode = "All"
        st.session_state.category_filter = "All"
        reset_quiz()
        st.rerun()

    st.stop()
# --------------------
# End screen
# --------------------

if st.session_state.current_question >= len(st.session_state.question_order):
    if is_anytime_test_mode():
        st.subheader("Anytime Test Complete")
    else:
        st.subheader("Practice Complete")
    if not st.session_state.session_history_saved:
        save_session_history()
        st.session_state.session_history_saved = True
    st.success(
        f"You scored {st.session_state.score} / {len(st.session_state.question_order)}"
    )

    if is_anytime_test_mode():
        anytime_score = st.session_state.score

        if anytime_score >= 40:
            st.info("Strong test score. This is a very encouraging Anytime-style result.")
        elif anytime_score >= 35:
            st.info("Solid test score. This is in the realistic passing-range conversation.")
        elif anytime_score >= 30:
            st.info("Decent test score. Keep building speed and weak-category recall.")
        else:
            st.info("Training score. Review misses and keep building the canon base.")

    st.divider()

    st.subheader("Category Breakdown")

    category_stats = get_category_stats(st.session_state.results)

    for category, stats in category_stats.items():
        correct = stats["correct"]
        total = stats["total"]
        accuracy = round((correct / total) * 100)

        st.write(f"**{category}:** {correct} / {total} — {accuracy}%")

    st.divider()

    missed_results = []

    for result in st.session_state.results:
        if not result["was_correct"]:
            missed_results.append(result)

    if len(missed_results) > 0:
        st.subheader("Missed This Session")

        for result in missed_results:
            st.write(
                f"**{result['category']}** — {result['correct_answer']}"
            )

            st.caption(result["question"])

        st.divider()

    st.subheader("Review")

    show_only_missed = st.checkbox("Show only missed questions")

    for result in st.session_state.results:
        if show_only_missed and result["was_correct"]:
            continue

        if result["was_correct"]:
            st.markdown(f"### ✅ {result['category']}")
        else:
            st.markdown(f"### ❌ {result['category']}")

        st.write(result["question"])
        st.write(f"Your answer: {result['user_answer']}")
        st.write(f"Correct answer: {result['correct_answer']}")

        st.divider()

    missed_count = 0

    for result in st.session_state.results:
        if not result["was_correct"]:
            missed_count += 1

    if missed_count > 0:
        if st.button(f"Practice Missed Questions ({missed_count})"):
            start_missed_questions_practice()
            st.rerun()

    if st.button("Start Over"):
        reset_quiz()
        st.rerun()

    st.stop()


# --------------------
# Current question
# --------------------

question_number = st.session_state.current_question + 1
total_questions = len(st.session_state.question_order)

st.caption(
    f"Mode: {st.session_state.category_filter} | "
    f"Difficulty: {st.session_state.difficulty_mode} | "
    f"{total_questions} of {st.session_state.eligible_question_count} available questions"
)

question_index = st.session_state.question_order[
    st.session_state.current_question
]

question = questions[question_index]

st.write(f"Question {question_number} of {total_questions}")

if is_anytime_test_mode():
    show_anytime_timer(question_number)

st.caption(question["category"].upper())

st.subheader(question["question"])


# --------------------
# Answer form
# --------------------

if not st.session_state.submitted:
    with st.form(key=f"question_{question_number}", clear_on_submit=True):
        user_answer = st.text_input("Your answer")

        st.caption("Type your answer and press Enter.")

        submitted = st.form_submit_button("Submit")

    focus_answer_box(question_number)

    if submitted:
        submit_answer(user_answer, question)

        if is_anytime_test_mode():
            go_to_next_question()

        st.rerun()

    if is_anytime_test_mode():
        st.markdown(
            """
            <style>
            div[data-testid="stButton"]:has(button[kind="secondary"]) {
                display: none;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        if st.button("Time Expired"):
            submit_answer("", question)
            go_to_next_question()
            st.rerun()


# --------------------
# Feedback
# --------------------

if st.session_state.submitted:
    if st.session_state.last_correct:
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect")

        st.write(f"Your answer: {st.session_state.last_answer}")
        st.write(f"Correct answer: {question['answer']}")

    enable_enter_for_next_question()

    st.caption("Press Enter to continue to the next question.")

    if st.button("Next Question"):
        go_to_next_question()
        st.rerun()