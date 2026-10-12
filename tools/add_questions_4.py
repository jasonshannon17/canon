import json


NEW_QUESTIONS = [
    {
        "id": 161,
        "question": "This number is the only even prime number.",
        "answer": "2",
        "aliases": ["Two"],
        "category": "Math",
        "difficulty": 1
    },
    {
        "id": 162,
        "question": "This term describes a triangle with three equal sides.",
        "answer": "Equilateral",
        "aliases": ["Equilateral triangle"],
        "category": "Math",
        "difficulty": 2
    },
    {
        "id": 163,
        "question": "This term describes a triangle with two equal sides.",
        "answer": "Isosceles",
        "aliases": ["Isosceles triangle"],
        "category": "Math",
        "difficulty": 2
    },
    {
        "id": 164,
        "question": "This Greek letter is commonly used to represent the ratio of a circle's circumference to its diameter.",
        "answer": "Pi",
        "aliases": ["π"],
        "category": "Math",
        "difficulty": 1
    },
    {
        "id": 165,
        "question": "This Roman numeral represents 50.",
        "answer": "L",
        "aliases": [],
        "category": "Math",
        "difficulty": 2
    },
    {
        "id": 166,
        "question": "This Roman numeral represents 500.",
        "answer": "D",
        "aliases": [],
        "category": "Math",
        "difficulty": 2
    },
    {
        "id": 167,
        "question": "This branch of mathematics deals with sine, cosine, and tangent.",
        "answer": "Trigonometry",
        "aliases": ["Trig"],
        "category": "Math",
        "difficulty": 2
    },
    {
        "id": 168,
        "question": "This branch of mathematics studies points, lines, angles, surfaces, and solids.",
        "answer": "Geometry",
        "aliases": [],
        "category": "Math",
        "difficulty": 1
    },
    {
        "id": 169,
        "question": "This mathematician is associated with a theorem about right triangles.",
        "answer": "Pythagoras",
        "aliases": ["Pythagorean theorem"],
        "category": "Math",
        "difficulty": 2
    },
    {
        "id": 170,
        "question": "This sequence begins 0, 1, 1, 2, 3, 5, 8.",
        "answer": "Fibonacci sequence",
        "aliases": ["Fibonacci"],
        "category": "Math",
        "difficulty": 2
    },
    {
        "id": 171,
        "question": "This value is the square root of 144.",
        "answer": "12",
        "aliases": ["Twelve"],
        "category": "Math",
        "difficulty": 1
    },
    {
        "id": 172,
        "question": "This term describes the longest side of a right triangle.",
        "answer": "Hypotenuse",
        "aliases": [],
        "category": "Math",
        "difficulty": 2
    },
    {
        "id": 173,
        "question": "This musical features the Phantom and Christine.",
        "answer": "The Phantom of the Opera",
        "aliases": ["Phantom of the Opera", "Phantom"],
        "category": "Theatre",
        "difficulty": 2
    },
    {
        "id": 174,
        "question": "This musical features the songs 'Tonight' and 'America' and is inspired by Romeo and Juliet.",
        "answer": "West Side Story",
        "aliases": [],
        "category": "Theatre",
        "difficulty": 2
    },
    {
        "id": 175,
        "question": "This musical features Tevye and the song 'If I Were a Rich Man.'",
        "answer": "Fiddler on the Roof",
        "aliases": ["Fiddler"],
        "category": "Theatre",
        "difficulty": 2
    },
    {
        "id": 176,
        "question": "This musical features the songs 'The Impossible Dream' and 'Dulcinea.'",
        "answer": "Man of La Mancha",
        "aliases": [],
        "category": "Theatre",
        "difficulty": 3
    },
    {
        "id": 177,
        "question": "This playwright wrote Waiting for Godot.",
        "answer": "Samuel Beckett",
        "aliases": ["Beckett"],
        "category": "Theatre",
        "difficulty": 3
    },
    {
        "id": 178,
        "question": "This playwright wrote The Importance of Being Earnest.",
        "answer": "Oscar Wilde",
        "aliases": ["Wilde"],
        "category": "Theatre",
        "difficulty": 3
    },
    {
        "id": 179,
        "question": "This playwright wrote A Doll's House and Hedda Gabler.",
        "answer": "Henrik Ibsen",
        "aliases": ["Ibsen"],
        "category": "Theatre",
        "difficulty": 3
    },
    {
        "id": 180,
        "question": "This playwright wrote Pygmalion.",
        "answer": "George Bernard Shaw",
        "aliases": ["Bernard Shaw", "Shaw", "G. B. Shaw", "GB Shaw"],
        "category": "Theatre",
        "difficulty": 3
    },
    {
        "id": 181,
        "question": "This wall began falling in 1989, symbolizing the end of the Cold War.",
        "answer": "Berlin Wall",
        "aliases": ["The Berlin Wall"],
        "category": "World History",
        "difficulty": 2
    },
    {
        "id": 182,
        "question": "This South African leader became president in 1994 after years imprisoned on Robben Island.",
        "answer": "Nelson Mandela",
        "aliases": ["Mandela"],
        "category": "World History",
        "difficulty": 2
    },
    {
        "id": 183,
        "question": "This Indian leader used nonviolent resistance against British rule.",
        "answer": "Mahatma Gandhi",
        "aliases": ["Gandhi"],
        "category": "World History",
        "difficulty": 2
    },
    {
        "id": 184,
        "question": "This Chinese leader proclaimed the People's Republic of China in 1949.",
        "answer": "Mao Zedong",
        "aliases": ["Mao", "Mao Tse-tung", "Mao Tse Tung"],
        "category": "World History",
        "difficulty": 3
    },
    {
        "id": 185,
        "question": "This revolution began in 1789 with events including the storming of the Bastille.",
        "answer": "French Revolution",
        "aliases": ["The French Revolution"],
        "category": "World History",
        "difficulty": 2
    },
    {
        "id": 186,
        "question": "This queen of France was executed during the French Revolution.",
        "answer": "Marie Antoinette",
        "aliases": [],
        "category": "World History",
        "difficulty": 2
    },
    {
        "id": 187,
        "question": "This Byzantine emperor is associated with a famous law code.",
        "answer": "Justinian",
        "aliases": ["Justinian I"],
        "category": "World History",
        "difficulty": 3
    },
    {
        "id": 188,
        "question": "This Carthaginian general crossed the Alps with elephants.",
        "answer": "Hannibal",
        "aliases": ["Hannibal Barca"],
        "category": "World History",
        "difficulty": 2
    },
    {
        "id": 189,
        "question": "This Egyptian queen was allied with Julius Caesar and Mark Antony.",
        "answer": "Cleopatra",
        "aliases": ["Cleopatra VII"],
        "category": "World History",
        "difficulty": 2
    },
    {
        "id": 190,
        "question": "This English king had six wives.",
        "answer": "Henry VIII",
        "aliases": ["Henry the Eighth", "King Henry VIII"],
        "category": "World History",
        "difficulty": 2
    },
    {
        "id": 191,
        "question": "This Verdi opera is set in ancient Egypt.",
        "answer": "Aida",
        "aliases": [],
        "category": "Opera",
        "difficulty": 2
    },
    {
        "id": 192,
        "question": "This Verdi opera features the aria 'La donna è mobile.'",
        "answer": "Rigoletto",
        "aliases": [],
        "category": "Opera",
        "difficulty": 3
    },
    {
        "id": 193,
        "question": "This Puccini opera features Mimì and Rodolfo.",
        "answer": "La Bohème",
        "aliases": ["La Boheme", "Bohème", "Boheme"],
        "category": "Opera",
        "difficulty": 3
    },
    {
        "id": 194,
        "question": "This Mozart opera features Papageno and the Queen of the Night.",
        "answer": "The Magic Flute",
        "aliases": ["Magic Flute", "Die Zauberflöte", "Die Zauberflote"],
        "category": "Opera",
        "difficulty": 3
    },
    {
        "id": 195,
        "question": "This Wagner opera cycle includes Das Rheingold and Götterdämmerung.",
        "answer": "The Ring Cycle",
        "aliases": ["Ring Cycle", "Der Ring des Nibelungen", "The Ring"],
        "category": "Opera",
        "difficulty": 3
    },
    {
        "id": 196,
        "question": "This Rossini opera features Figaro as a barber.",
        "answer": "The Barber of Seville",
        "aliases": ["Barber of Seville"],
        "category": "Opera",
        "difficulty": 3
    },
    {
        "id": 197,
        "question": "This Greek hero killed Medusa.",
        "answer": "Perseus",
        "aliases": [],
        "category": "Mythology",
        "difficulty": 3
    },
    {
        "id": 198,
        "question": "This Greek hero completed twelve labors.",
        "answer": "Heracles",
        "aliases": ["Hercules"],
        "category": "Mythology",
        "difficulty": 2
    },
    {
        "id": 199,
        "question": "This Supreme Court case established the 'separate but equal' doctrine.",
        "answer": "Plessy v. Ferguson",
        "aliases": ["Plessy", "Plessy vs Ferguson"],
        "category": "Civics",
        "difficulty": 3
    },
    {
        "id": 200,
        "question": "This Supreme Court case protected a student's right to wear a black armband in school.",
        "answer": "Tinker v. Des Moines",
        "aliases": ["Tinker", "Tinker vs Des Moines"],
        "category": "Civics",
        "difficulty": 3
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
    json.dump(existing_questions, file, indent=4, ensure_ascii=False)

print(f"Done. Question bank now has {len(existing_questions)} questions.")