import json


with open("../data/questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)


with open("../data/session_history.json", "r", encoding="utf-8") as file:
    history = json.load(file)


question_lookup = {}

for question in questions:
    question_lookup[question["id"]] = question


missed_counts = {}

for session in history:
    for question_id in session.get("missed_question_ids", []):
        if question_id not in missed_counts:
            missed_counts[question_id] = 0

        missed_counts[question_id] += 1


sorted_misses = sorted(
    missed_counts.items(),
    key=lambda item: item[1],
    reverse=True
)


print()
print("Active Misses Report")
print("--------------------")
print(f"Total active missed questions: {len(sorted_misses)}")
print()

if len(sorted_misses) == 0:
    print("No active misses yet.")
else:
    for question_id, miss_count in sorted_misses:
        question = question_lookup.get(question_id)

        if question is None:
            print(f"Question ID {question_id}: missed {miss_count}x, but not found in question bank.")
            continue

        print(f"ID {question_id} | missed {miss_count}x | {question['category']} | {question['answer']}")
        print(f"  {question['question']}")
        print()

        category_miss_counts = {}

for question_id, miss_count in missed_counts.items():
    question = question_lookup.get(question_id)

    if question is None:
        continue

    category = question["category"]

    if category not in category_miss_counts:
        category_miss_counts[category] = 0

    category_miss_counts[category] += miss_count


sorted_category_misses = sorted(
    category_miss_counts.items(),
    key=lambda item: item[1],
    reverse=True
)


print()
print("Misses by Category")
print("------------------")

for category, miss_count in sorted_category_misses:
    print(f"{category}: {miss_count} misses")