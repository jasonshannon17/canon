import json


NEW_QUESTIONS = [
    {
        "id": 81,
        "question": "This biblical figure built an ark before a great flood.",
        "answer": "Noah",
        "aliases": [],
        "category": "Bible",
        "difficulty": 2
    },
    {
        "id": 82,
        "question": "This biblical giant was defeated by David.",
        "answer": "Goliath",
        "aliases": [],
        "category": "Bible",
        "difficulty": 2
    },
    {
        "id": 83,
        "question": "This biblical woman is the mother of Jesus.",
        "answer": "Mary",
        "aliases": ["Virgin Mary"],
        "category": "Bible",
        "difficulty": 2
    },
    {
        "id": 84,
        "question": "This biblical figure was the first man.",
        "answer": "Adam",
        "aliases": [],
        "category": "Bible",
        "difficulty": 1
    },
    {
        "id": 85,
        "question": "This biblical figure was the first woman.",
        "answer": "Eve",
        "aliases": [],
        "category": "Bible",
        "difficulty": 1
    },
    {
        "id": 86,
        "question": "This opera by Puccini features Cio-Cio-San.",
        "answer": "Madama Butterfly",
        "aliases": ["Madame Butterfly"],
        "category": "Opera",
        "difficulty": 3
    },
    {
        "id": 87,
        "question": "This opera by Puccini features the singer Floria Tosca.",
        "answer": "Tosca",
        "aliases": [],
        "category": "Opera",
        "difficulty": 3
    },
    {
        "id": 88,
        "question": "This opera by Verdi features the Hebrew slaves' chorus.",
        "answer": "Nabucco",
        "aliases": [],
        "category": "Opera",
        "difficulty": 3
    },
    {
        "id": 89,
        "question": "This Mozart opera features the character Figaro.",
        "answer": "The Marriage of Figaro",
        "aliases": ["Marriage of Figaro", "Le nozze di Figaro"],
        "category": "Opera",
        "difficulty": 3
    },
    {
        "id": 90,
        "question": "This opera by Bizet features the toreador Escamillo.",
        "answer": "Carmen",
        "aliases": [],
        "category": "Opera",
        "difficulty": 3
    },
    {
        "id": 91,
        "question": "This composer became deaf later in life and wrote nine symphonies.",
        "answer": "Beethoven",
        "aliases": ["Ludwig van Beethoven"],
        "category": "Classical Music",
        "difficulty": 2
    },
    {
        "id": 92,
        "question": "This composer wrote the Brandenburg Concertos.",
        "answer": "Bach",
        "aliases": ["Johann Sebastian Bach", "J. S. Bach"],
        "category": "Classical Music",
        "difficulty": 3
    },
    {
        "id": 93,
        "question": "This composer wrote Eine kleine Nachtmusik.",
        "answer": "Mozart",
        "aliases": ["Wolfgang Amadeus Mozart", "W. A. Mozart"],
        "category": "Classical Music",
        "difficulty": 2
    },
    {
        "id": 94,
        "question": "This composer wrote Clair de lune.",
        "answer": "Debussy",
        "aliases": ["Claude Debussy"],
        "category": "Classical Music",
        "difficulty": 3
    },
    {
        "id": 95,
        "question": "This composer wrote Boléro.",
        "answer": "Ravel",
        "aliases": ["Maurice Ravel", "Bolero"],
        "category": "Classical Music",
        "difficulty": 3
    },
    {
        "id": 96,
        "question": "This philosopher was sentenced to death in Athens and drank hemlock.",
        "answer": "Socrates",
        "aliases": [],
        "category": "Philosophy",
        "difficulty": 2
    },
    {
        "id": 97,
        "question": "This philosopher was a student of Plato and tutor to Alexander the Great.",
        "answer": "Aristotle",
        "aliases": [],
        "category": "Philosophy",
        "difficulty": 2
    },
    {
        "id": 98,
        "question": "This philosopher wrote Critique of Pure Reason.",
        "answer": "Immanuel Kant",
        "aliases": ["Kant"],
        "category": "Philosophy",
        "difficulty": 3
    },
    {
        "id": 99,
        "question": "This philosopher wrote Beyond Good and Evil and Thus Spoke Zarathustra.",
        "answer": "Friedrich Nietzsche",
        "aliases": ["Nietzsche"],
        "category": "Philosophy",
        "difficulty": 3
    },
    {
        "id": 100,
        "question": "This philosopher said, 'I think, therefore I am.'",
        "answer": "René Descartes",
        "aliases": ["Rene Descartes", "Descartes"],
        "category": "Philosophy",
        "difficulty": 2
    },
    {
        "id": 101,
        "question": "This Dutch artist painted Starry Night.",
        "answer": "Vincent van Gogh",
        "aliases": ["Van Gogh", "Vincent Van Gogh"],
        "category": "Art",
        "difficulty": 2
    },
    {
        "id": 102,
        "question": "This Norwegian artist painted The Scream.",
        "answer": "Edvard Munch",
        "aliases": ["Munch"],
        "category": "Art",
        "difficulty": 2
    },
    {
        "id": 103,
        "question": "This French artist painted Water Lilies.",
        "answer": "Claude Monet",
        "aliases": ["Monet"],
        "category": "Art",
        "difficulty": 2
    },
    {
        "id": 104,
        "question": "This American artist painted Campbell's Soup Cans.",
        "answer": "Andy Warhol",
        "aliases": ["Warhol"],
        "category": "Art",
        "difficulty": 2
    },
    {
        "id": 105,
        "question": "This Mexican artist is known for self-portraits and was married to Diego Rivera.",
        "answer": "Frida Kahlo",
        "aliases": ["Kahlo"],
        "category": "Art",
        "difficulty": 2
    },
    {
        "id": 106,
        "question": "This Shakespeare play features the witches' line 'Double, double toil and trouble.'",
        "answer": "Macbeth",
        "aliases": [],
        "category": "Shakespeare",
        "difficulty": 2
    },
    {
        "id": 107,
        "question": "This Shakespeare play features Prospero, Miranda, and Caliban.",
        "answer": "The Tempest",
        "aliases": ["Tempest"],
        "category": "Shakespeare",
        "difficulty": 3
    },
    {
        "id": 108,
        "question": "This Shakespeare comedy features twins Viola and Sebastian.",
        "answer": "Twelfth Night",
        "aliases": [],
        "category": "Shakespeare",
        "difficulty": 3
    },
    {
        "id": 109,
        "question": "This Shakespeare play features Beatrice and Benedick.",
        "answer": "Much Ado About Nothing",
        "aliases": [],
        "category": "Shakespeare",
        "difficulty": 3
    },
    {
        "id": 110,
        "question": "This Shakespeare tragedy features Desdemona.",
        "answer": "Othello",
        "aliases": [],
        "category": "Shakespeare",
        "difficulty": 2
    },
    {
        "id": 111,
        "question": "This author wrote Great Expectations and A Tale of Two Cities.",
        "answer": "Charles Dickens",
        "aliases": ["Dickens"],
        "category": "Literature",
        "difficulty": 2
    },
    {
        "id": 112,
        "question": "This author wrote To Kill a Mockingbird.",
        "answer": "Harper Lee",
        "aliases": ["Lee"],
        "category": "Literature",
        "difficulty": 2
    },
    {
        "id": 113,
        "question": "This author wrote The Great Gatsby.",
        "answer": "F. Scott Fitzgerald",
        "aliases": ["Fitzgerald", "Scott Fitzgerald"],
        "category": "Literature",
        "difficulty": 2
    },
    {
        "id": 114,
        "question": "This author wrote Jane Eyre.",
        "answer": "Charlotte Brontë",
        "aliases": ["Charlotte Bronte", "Brontë", "Bronte"],
        "category": "Literature",
        "difficulty": 3
    },
    {
        "id": 115,
        "question": "This author wrote Wuthering Heights.",
        "answer": "Emily Brontë",
        "aliases": ["Emily Bronte", "Brontë", "Bronte"],
        "category": "Literature",
        "difficulty": 3
    },
    {
        "id": 116,
        "question": "This river runs through Baghdad.",
        "answer": "Tigris",
        "aliases": ["The Tigris", "Tigris River"],
        "category": "Geography",
        "difficulty": 3
    },
    {
        "id": 117,
        "question": "This river runs through Cairo.",
        "answer": "Nile",
        "aliases": ["The Nile", "Nile River"],
        "category": "Geography",
        "difficulty": 2
    },
    {
        "id": 118,
        "question": "This strait separates Spain from Morocco.",
        "answer": "Strait of Gibraltar",
        "aliases": ["Gibraltar", "The Strait of Gibraltar"],
        "category": "Geography",
        "difficulty": 3
    },
    {
        "id": 119,
        "question": "Siam is the former name of this country.",
        "answer": "Thailand",
        "aliases": [],
        "category": "Geography",
        "difficulty": 2
    },
    {
        "id": 120,
        "question": "Persia is the former name of this country.",
        "answer": "Iran",
        "aliases": [],
        "category": "Geography",
        "difficulty": 2
    }
]


with open("../data/questions.json", "r", encoding="utf-8") as file:
    existing_questions = json.load(file)

existing_ids = set()

for question in existing_questions:
    existing_ids.add(question["id"])

for question in NEW_QUESTIONS:
    if question["id"] not in existing_ids:
        existing_questions.append(question)

with open("../data/questions.json", "w", encoding="utf-8") as file:
    json.dump(existing_questions, file, indent=4)

print(f"Done. Question bank now has {len(existing_questions)} questions.")