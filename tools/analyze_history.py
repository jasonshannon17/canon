import json


with open("../data/session_history.json", "r", encoding="utf-8") as file:
    history = json.load(file)


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


category_accuracies = []

for category, stats in category_stats.items():
    correct = stats["correct"]
    total = stats["total"]

    if total > 0:
        accuracy = round((correct / total) * 100)
    else:
        accuracy = 0

    category_accuracies.append(
        {
            "category": category,
            "correct": correct,
            "total": total,
            "accuracy": accuracy
        }
    )


category_accuracies.sort(key=lambda item: item["accuracy"])


print()
print("Weakest Categories")
print("------------------")

if len(category_accuracies) == 0:
    print("No usable session history yet.")
else:
    for item in category_accuracies:
        print(
            f"{item['category']}: "
            f"{item['accuracy']}% "
            f"({item['correct']}/{item['total']})"
        )

print()