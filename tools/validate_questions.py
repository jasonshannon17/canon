import json


REQUIRED_FIELDS = [
    "id",
    "question",
    "answer",
    "aliases",
    "category",
    "difficulty"
]


with open("../data/questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)


errors = []
warnings = []

seen_ids = set()

for index, question in enumerate(questions):
    location = f"Question at list position {index + 1}"

    for field in REQUIRED_FIELDS:
        if field not in question:
            errors.append(f"{location} is missing field: {field}")

    if "id" in question:
        question_id = question["id"]

        if question_id in seen_ids:
            errors.append(f"Duplicate ID found: {question_id}")

        seen_ids.add(question_id)

    if "question" in question and question["question"].strip() == "":
        errors.append(f"Question ID {question.get('id', 'UNKNOWN')} has an empty question.")

    if "answer" in question and question["answer"].strip() == "":
        errors.append(f"Question ID {question.get('id', 'UNKNOWN')} has an empty answer.")

    if "category" in question and question["category"].strip() == "":
        errors.append(f"Question ID {question.get('id', 'UNKNOWN')} has an empty category.")

    if "aliases" in question and not isinstance(question["aliases"], list):
        errors.append(f"Question ID {question.get('id', 'UNKNOWN')} has aliases that are not a list.")

    if "difficulty" in question:
        difficulty = question["difficulty"]

        if not isinstance(difficulty, int):
            errors.append(f"Question ID {question.get('id', 'UNKNOWN')} has non-integer difficulty.")
        elif difficulty < 1 or difficulty > 5:
            warnings.append(
                f"Question ID {question.get('id', 'UNKNOWN')} has unusual difficulty: {difficulty}"
            )


print()
print("Question Bank Validation")
print("------------------------")
print(f"Total questions: {len(questions)}")
print(f"Unique IDs: {len(seen_ids)}")
print()

if len(errors) == 0:
    print("Errors: 0")
else:
    print(f"Errors: {len(errors)}")
    for error in errors:
        print(f"- {error}")

print()

if len(warnings) == 0:
    print("Warnings: 0")
else:
    print(f"Warnings: {len(warnings)}")
    for warning in warnings:
        print(f"- {warning}")

print()

if len(errors) == 0:
    print("Question bank looks good.")
else:
    print("Fix errors before running Canon.")