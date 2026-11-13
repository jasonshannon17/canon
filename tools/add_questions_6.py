import json


NEW_QUESTIONS = [
    {
        "id": 241,
        "question": "He was the first president of the United States.",
        "answer": "George Washington",
        "aliases": ["Washington"],
        "category": "Presidents & Government",
        "difficulty": 1
    },
    {
        "id": 242,
        "question": "This president issued the Emancipation Proclamation during the Civil War.",
        "answer": "Abraham Lincoln",
        "aliases": ["Lincoln"],
        "category": "Presidents & Government",
        "difficulty": 1
    },
    {
        "id": 243,
        "question": "This president served four terms, more than any other U.S. president.",
        "answer": "Franklin D. Roosevelt",
        "aliases": ["Franklin Roosevelt", "FDR", "Roosevelt"],
        "category": "Presidents & Government",
        "difficulty": 1
    },
    {
        "id": 244,
        "question": "This president resigned from office in 1974 during the Watergate scandal.",
        "answer": "Richard Nixon",
        "aliases": ["Nixon"],
        "category": "Presidents & Government",
        "difficulty": 1
    },
    {
        "id": 245,
        "question": "This president was assassinated in Dallas on November 22, 1963.",
        "answer": "John F. Kennedy",
        "aliases": ["John Kennedy", "JFK", "Kennedy"],
        "category": "Presidents & Government",
        "difficulty": 1
    },
    {
        "id": 246,
        "question": "This president completed the Louisiana Purchase from France in 1803.",
        "answer": "Thomas Jefferson",
        "aliases": ["Jefferson"],
        "category": "Presidents & Government",
        "difficulty": 1
    },
    {
        "id": 247,
        "question": "This president is associated with the Square Deal and the conservation movement.",
        "answer": "Theodore Roosevelt",
        "aliases": ["Teddy Roosevelt", "TR", "Roosevelt"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 248,
        "question": "This president succeeded Franklin D. Roosevelt in 1945.",
        "answer": "Harry S. Truman",
        "aliases": ["Harry Truman", "Truman"],
        "category": "Presidents & Government",
        "difficulty": 1
    },
    {
        "id": 249,
        "question": "This former Supreme Allied Commander became president in 1953.",
        "answer": "Dwight D. Eisenhower",
        "aliases": ["Dwight Eisenhower", "Eisenhower", "Ike"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 250,
        "question": "This president launched the Great Society domestic program.",
        "answer": "Lyndon B. Johnson",
        "aliases": ["Lyndon Johnson", "LBJ", "Johnson"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 251,
        "question": "This president was previously governor of Georgia and later won the Nobel Peace Prize.",
        "answer": "Jimmy Carter",
        "aliases": ["James Carter", "Carter"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 252,
        "question": "Before becoming president, this man served as governor of California and was a Hollywood actor.",
        "answer": "Ronald Reagan",
        "aliases": ["Reagan"],
        "category": "Presidents & Government",
        "difficulty": 1
    },
    {
        "id": 253,
        "question": "This president was the first to be born after the United States declared independence.",
        "answer": "Martin Van Buren",
        "aliases": ["Van Buren"],
        "category": "Presidents & Government",
        "difficulty": 3
    },
    {
        "id": 254,
        "question": "This president served the shortest term, dying about a month after taking office in 1841.",
        "answer": "William Henry Harrison",
        "aliases": ["Harrison"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 255,
        "question": "This president was the only U.S. president to serve two nonconsecutive terms before Donald Trump.",
        "answer": "Grover Cleveland",
        "aliases": ["Cleveland"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 256,
        "question": "This amendment abolished slavery in the United States.",
        "answer": "13th Amendment",
        "aliases": ["Thirteenth Amendment", "the 13th Amendment", "13"],
        "category": "Presidents & Government",
        "difficulty": 1
    },
    {
        "id": 257,
        "question": "This amendment guarantees equal protection under the law and defines U.S. citizenship.",
        "answer": "14th Amendment",
        "aliases": ["Fourteenth Amendment", "the 14th Amendment", "14"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 258,
        "question": "This amendment prohibited denying the right to vote on the basis of race.",
        "answer": "15th Amendment",
        "aliases": ["Fifteenth Amendment", "the 15th Amendment", "15"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 259,
        "question": "This amendment gave women the constitutional right to vote.",
        "answer": "19th Amendment",
        "aliases": ["Nineteenth Amendment", "the 19th Amendment", "19"],
        "category": "Presidents & Government",
        "difficulty": 1
    },
    {
        "id": 260,
        "question": "This amendment limits a president to two elected terms.",
        "answer": "22nd Amendment",
        "aliases": ["Twenty-second Amendment", "Twenty Second Amendment", "the 22nd Amendment", "22"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 261,
        "question": "This amendment lowered the voting age in federal and state elections to 18.",
        "answer": "26th Amendment",
        "aliases": ["Twenty-sixth Amendment", "Twenty Sixth Amendment", "the 26th Amendment", "26"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 262,
        "question": "This article of the Constitution establishes the legislative branch.",
        "answer": "Article I",
        "aliases": ["Article 1", "one"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 263,
        "question": "This article of the Constitution establishes the executive branch.",
        "answer": "Article II",
        "aliases": ["Article 2", "two"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 264,
        "question": "This article of the Constitution establishes the judicial branch.",
        "answer": "Article III",
        "aliases": ["Article 3", "three"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 265,
        "question": "The vice president serves as president of this chamber of Congress.",
        "answer": "Senate",
        "aliases": ["the Senate", "U.S. Senate", "United States Senate"],
        "category": "Presidents & Government",
        "difficulty": 1
    },
    {
        "id": 266,
        "question": "The Speaker presides over this chamber of Congress.",
        "answer": "House of Representatives",
        "aliases": ["the House", "House", "U.S. House", "United States House of Representatives"],
        "category": "Presidents & Government",
        "difficulty": 1
    },
    {
        "id": 267,
        "question": "This federal department is headed by the attorney general.",
        "answer": "Department of Justice",
        "aliases": ["Justice Department", "DOJ", "Justice"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 268,
        "question": "This Cabinet official is traditionally fourth in the presidential line of succession, after the vice president and congressional leaders.",
        "answer": "Secretary of State",
        "aliases": ["the Secretary of State"],
        "category": "Presidents & Government",
        "difficulty": 3
    },
    {
        "id": 269,
        "question": "This Supreme Court case established the principle of judicial review in 1803.",
        "answer": "Marbury v. Madison",
        "aliases": ["Marbury versus Madison", "Marbury"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 270,
        "question": "This 1954 Supreme Court decision ruled that racial segregation in public schools was unconstitutional.",
        "answer": "Brown v. Board of Education",
        "aliases": ["Brown versus Board of Education", "Brown v Board", "Brown"],
        "category": "Presidents & Government",
        "difficulty": 1
    },
    {
        "id": 271,
        "question": "This Supreme Court case established the right to an attorney for indigent criminal defendants in state courts.",
        "answer": "Gideon v. Wainwright",
        "aliases": ["Gideon versus Wainwright", "Gideon"],
        "category": "Presidents & Government",
        "difficulty": 3
    },
    {
        "id": 272,
        "question": "This Supreme Court case led to the warning police give suspects about their rights before custodial interrogation.",
        "answer": "Miranda v. Arizona",
        "aliases": ["Miranda versus Arizona", "Miranda"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 273,
        "question": "This First Lady chaired the commission that drafted the Universal Declaration of Human Rights.",
        "answer": "Eleanor Roosevelt",
        "aliases": ["Eleanor"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 274,
        "question": "This First Lady launched the 'Just Say No' anti-drug campaign.",
        "answer": "Nancy Reagan",
        "aliases": ["Nancy"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 275,
        "question": "This First Lady later served as a U.S. senator and secretary of state.",
        "answer": "Hillary Clinton",
        "aliases": ["Hillary Rodham Clinton", "Hillary"],
        "category": "Presidents & Government",
        "difficulty": 1
    },
    {
        "id": 276,
        "question": "This body formally elects the president and vice president of the United States.",
        "answer": "Electoral College",
        "aliases": ["the Electoral College"],
        "category": "Presidents & Government",
        "difficulty": 1
    },
    {
        "id": 277,
        "question": "A presidential veto can be overridden by this fraction of both houses of Congress.",
        "answer": "two-thirds",
        "aliases": ["2/3", "two thirds", "two-thirds vote"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 278,
        "question": "The Constitution requires a president to be at least this many years old.",
        "answer": "35",
        "aliases": ["thirty-five", "35 years old", "thirty five"],
        "category": "Presidents & Government",
        "difficulty": 1
    },
    {
        "id": 279,
        "question": "The Constitution requires a U.S. senator to be at least this many years old.",
        "answer": "30",
        "aliases": ["thirty", "30 years old"],
        "category": "Presidents & Government",
        "difficulty": 2
    },
    {
        "id": 280,
        "question": "The Constitution requires a member of the House of Representatives to be at least this many years old.",
        "answer": "25",
        "aliases": ["twenty-five", "25 years old", "twenty five"],
        "category": "Presidents & Government",
        "difficulty": 2
    }
]


with open("../data/questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)


existing_ids = {question["id"] for question in questions}

questions_to_add = []

for question in NEW_QUESTIONS:
    if question["id"] in existing_ids:
        print(f"Skipping duplicate ID: {question['id']}")
    else:
        questions_to_add.append(question)


questions.extend(questions_to_add)


with open("../data/questions.json", "w", encoding="utf-8") as file:
    json.dump(questions, file, indent=4, ensure_ascii=False)


print(f"Added {len(questions_to_add)} questions.")
print(f"Question bank now has {len(questions)} questions.")