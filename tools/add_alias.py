import json


QUESTION_ID = 121
NEW_ALIAS = "Napolean"


with open("../data/questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)


question_found = False
alias_added = False

for question in questions:
    if question["id"] == QUESTION_ID:
        question_found = True

        if "aliases" not in question:
            question["aliases"] = []

        if NEW_ALIAS not in question["aliases"]:
            question["aliases"].append(NEW_ALIAS)
            alias_added = True

        print(f"Question: {question['question']}")
        print(f"Answer: {question['answer']}")
        print(f"Aliases: {question['aliases']}")


if not question_found:
    print(f"No question found with ID {QUESTION_ID}.")

else:
    with open("../data/questions.json", "w", encoding="utf-8") as file:
        json.dump(questions, file, indent=4, ensure_ascii=False)

    if alias_added:
        print(f"Added alias: {NEW_ALIAS}")
    else:
        print(f"Alias already exists: {NEW_ALIAS}")

    print("questions.json updated safely.")