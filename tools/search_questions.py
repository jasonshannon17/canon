import json


SEARCH_TERM = "Strauss"


with open("../data/questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)


search_term_lower = SEARCH_TERM.lower()

matches = []

for question in questions:
    searchable_text = " ".join(
        [
            str(question["id"]),
            question["question"],
            question["answer"],
            question["category"],
            " ".join(question["aliases"])
        ]
    ).lower()

    if search_term_lower in searchable_text:
        matches.append(question)


print()
print(f"Search results for: {SEARCH_TERM}")
print("-------------------------")

if len(matches) == 0:
    print("No matches found.")

else:
    for question in matches:
        print()
        print(f"ID: {question['id']}")
        print(f"Category: {question['category']}")
        print(f"Question: {question['question']}")
        print(f"Answer: {question['answer']}")
        print(f"Aliases: {question['aliases']}")

print()