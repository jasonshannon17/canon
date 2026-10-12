import json


with open("../data/questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)


category_stats = {}

for question in questions:
    category = question["category"]

    if category not in category_stats:
        category_stats[category] = {
            "count": 0,
            "difficulty_total": 0
        }

    category_stats[category]["count"] += 1
    category_stats[category]["difficulty_total"] += question["difficulty"]


sorted_categories = sorted(
    category_stats.items(),
    key=lambda item: item[1]["count"],
    reverse=True
)


print()
print("Category Report")
print("---------------")
print(f"Total questions: {len(questions)}")
print()

for category, stats in sorted_categories:
    count = stats["count"]
    average_difficulty = round(stats["difficulty_total"] / count, 2)

    print(
        f"{category}: {count} questions "
        f"(avg difficulty {average_difficulty})"
    )

print()