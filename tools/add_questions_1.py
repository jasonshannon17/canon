import json


NEW_QUESTIONS = [
    {
        "id": 31,
        "question": "This Greek goddess of wisdom is the Roman Minerva.",
        "answer": "Athena",
        "aliases": ["Athene"],
        "category": "Mythology",
        "difficulty": 2
    },
    {
        "id": 32,
        "question": "This Greek messenger god is the Roman Mercury.",
        "answer": "Hermes",
        "aliases": [],
        "category": "Mythology",
        "difficulty": 2
    },
    {
        "id": 33,
        "question": "This Greek god of the sea is the Roman Neptune.",
        "answer": "Poseidon",
        "aliases": [],
        "category": "Mythology",
        "difficulty": 2
    },
    {
        "id": 34,
        "question": "This Titan is often shown holding up the heavens.",
        "answer": "Atlas",
        "aliases": [],
        "category": "Mythology",
        "difficulty": 2
    },
    {
        "id": 35,
        "question": "This Shakespeare play features the characters Puck, Oberon, and Titania.",
        "answer": "A Midsummer Night's Dream",
        "aliases": ["Midsummer Night's Dream"],
        "category": "Shakespeare",
        "difficulty": 3
    },
    {
        "id": 36,
        "question": "This Shakespeare play features Brutus and Cassius.",
        "answer": "Julius Caesar",
        "aliases": [],
        "category": "Shakespeare",
        "difficulty": 2
    },
    {
        "id": 37,
        "question": "This Shakespeare character says, 'To be, or not to be.'",
        "answer": "Hamlet",
        "aliases": ["Prince Hamlet"],
        "category": "Shakespeare",
        "difficulty": 2
    },
    {
        "id": 38,
        "question": "This Shakespeare play is set largely in Verona and features Mercutio.",
        "answer": "Romeo and Juliet",
        "aliases": ["Romeo & Juliet"],
        "category": "Shakespeare",
        "difficulty": 2
    },
    {
        "id": 39,
        "question": "This author wrote 1984 and Animal Farm.",
        "answer": "George Orwell",
        "aliases": ["Orwell"],
        "category": "Literature",
        "difficulty": 2
    },
    {
        "id": 40,
        "question": "This author wrote Brave New World.",
        "answer": "Aldous Huxley",
        "aliases": ["Huxley"],
        "category": "Literature",
        "difficulty": 3
    },
    {
        "id": 41,
        "question": "This author created Holden Caulfield.",
        "answer": "J. D. Salinger",
        "aliases": ["Salinger", "JD Salinger"],
        "category": "Literature",
        "difficulty": 3
    },
    {
        "id": 42,
        "question": "This author wrote The Grapes of Wrath.",
        "answer": "John Steinbeck",
        "aliases": ["Steinbeck"],
        "category": "Literature",
        "difficulty": 2
    },
    {
        "id": 43,
        "question": "This author wrote The Old Man and the Sea.",
        "answer": "Ernest Hemingway",
        "aliases": ["Hemingway"],
        "category": "Literature",
        "difficulty": 2
    },
    {
        "id": 44,
        "question": "This author wrote Crime and Punishment and The Brothers Karamazov.",
        "answer": "Fyodor Dostoevsky",
        "aliases": ["Dostoevsky", "Dostoyevsky"],
        "category": "Literature",
        "difficulty": 3
    },
    {
        "id": 45,
        "question": "This river runs through Rome.",
        "answer": "Tiber",
        "aliases": ["The Tiber", "Tiber River"],
        "category": "Geography",
        "difficulty": 3
    },
    {
        "id": 46,
        "question": "This river runs through Vienna, Budapest, and Bratislava.",
        "answer": "Danube",
        "aliases": ["The Danube", "Danube River"],
        "category": "Geography",
        "difficulty": 2
    },
    {
        "id": 47,
        "question": "This mountain range separates Europe and Asia in Russia.",
        "answer": "Ural Mountains",
        "aliases": ["Urals", "The Urals"],
        "category": "Geography",
        "difficulty": 3
    },
    {
        "id": 48,
        "question": "This mountain range runs along the western edge of South America.",
        "answer": "Andes",
        "aliases": ["The Andes", "Andes Mountains"],
        "category": "Geography",
        "difficulty": 2
    },
    {
        "id": 49,
        "question": "This strait separates Alaska from Russia.",
        "answer": "Bering Strait",
        "aliases": ["The Bering Strait"],
        "category": "Geography",
        "difficulty": 2
    },
    {
        "id": 50,
        "question": "Ceylon is the former name of this island nation.",
        "answer": "Sri Lanka",
        "aliases": [],
        "category": "Geography",
        "difficulty": 3
    },
    {
        "id": 51,
        "question": "This amendment ended Prohibition.",
        "answer": "21st Amendment",
        "aliases": ["Twenty-first Amendment", "21st"],
        "category": "Civics",
        "difficulty": 3
    },
    {
        "id": 52,
        "question": "This amendment established presidential term limits.",
        "answer": "22nd Amendment",
        "aliases": ["Twenty-second Amendment", "22nd"],
        "category": "Civics",
        "difficulty": 3
    },
    {
        "id": 53,
        "question": "This amendment deals with presidential succession and disability.",
        "answer": "25th Amendment",
        "aliases": ["Twenty-fifth Amendment", "25th"],
        "category": "Civics",
        "difficulty": 3
    },
    {
        "id": 54,
        "question": "This Supreme Court case established judicial review.",
        "answer": "Marbury v. Madison",
        "aliases": ["Marbury", "Marbury vs Madison"],
        "category": "Civics",
        "difficulty": 3
    },
    {
        "id": 55,
        "question": "This Supreme Court case declared school segregation unconstitutional.",
        "answer": "Brown v. Board of Education",
        "aliases": ["Brown v Board", "Brown vs Board of Education", "Brown"],
        "category": "Civics",
        "difficulty": 2
    },
    {
        "id": 56,
        "question": "This president was in office during the Cuban Missile Crisis.",
        "answer": "John F. Kennedy",
        "aliases": ["JFK", "Kennedy", "John Kennedy"],
        "category": "History",
        "difficulty": 2
    },
    {
        "id": 57,
        "question": "This president was in office when the Berlin Wall fell.",
        "answer": "George H. W. Bush",
        "aliases": ["George Bush", "George Bush Sr.", "Bush"],
        "category": "History",
        "difficulty": 3
    },
    {
        "id": 58,
        "question": "This American president led the country during World War I.",
        "answer": "Woodrow Wilson",
        "aliases": ["Wilson"],
        "category": "History",
        "difficulty": 2
    },
    {
        "id": 59,
        "question": "This man is credited with discovering penicillin.",
        "answer": "Alexander Fleming",
        "aliases": ["Fleming"],
        "category": "Science",
        "difficulty": 3
    },
    {
        "id": 60,
        "question": "This scientist developed the theory of relativity.",
        "answer": "Albert Einstein",
        "aliases": ["Einstein"],
        "category": "Science",
        "difficulty": 2
    },
    {
        "id": 61,
        "question": "This scientist proposed the theory of evolution by natural selection.",
        "answer": "Charles Darwin",
        "aliases": ["Darwin"],
        "category": "Science",
        "difficulty": 2
    },
    {
        "id": 62,
        "question": "This scientist formulated the laws of motion and universal gravitation.",
        "answer": "Isaac Newton",
        "aliases": ["Newton"],
        "category": "Science",
        "difficulty": 2
    },
    {
        "id": 63,
        "question": "The chemical symbol Au stands for this element.",
        "answer": "Gold",
        "aliases": [],
        "category": "Science",
        "difficulty": 2
    },
    {
        "id": 64,
        "question": "The chemical symbol Fe stands for this element.",
        "answer": "Iron",
        "aliases": [],
        "category": "Science",
        "difficulty": 2
    },
    {
        "id": 65,
        "question": "This biblical figure received the Ten Commandments.",
        "answer": "Moses",
        "aliases": [],
        "category": "Bible",
        "difficulty": 2
    },
    {
        "id": 66,
        "question": "This biblical figure survived a den of lions.",
        "answer": "Daniel",
        "aliases": [],
        "category": "Bible",
        "difficulty": 2
    },
    {
        "id": 67,
        "question": "This biblical figure was known for patience after suffering great losses.",
        "answer": "Job",
        "aliases": [],
        "category": "Bible",
        "difficulty": 3
    },
    {
        "id": 68,
        "question": "This apostle betrayed Jesus for thirty pieces of silver.",
        "answer": "Judas Iscariot",
        "aliases": ["Judas"],
        "category": "Bible",
        "difficulty": 2
    },
    {
        "id": 69,
        "question": "This composer wrote Messiah.",
        "answer": "Handel",
        "aliases": ["George Frideric Handel", "George Frederick Handel"],
        "category": "Classical Music",
        "difficulty": 3
    },
    {
        "id": 70,
        "question": "This composer wrote The Blue Danube.",
        "answer": "Johann Strauss II",
        "aliases": ["Strauss", "Johann Strauss"],
        "category": "Classical Music",
        "difficulty": 3
    },
    {
        "id": 71,
        "question": "This composer wrote The Barber of Seville.",
        "answer": "Rossini",
        "aliases": ["Gioachino Rossini"],
        "category": "Opera",
        "difficulty": 3
    },
    {
        "id": 72,
        "question": "This composer is associated with the Ring Cycle.",
        "answer": "Wagner",
        "aliases": ["Richard Wagner"],
        "category": "Opera",
        "difficulty": 3
    },
    {
        "id": 73,
        "question": "This painter created Guernica.",
        "answer": "Pablo Picasso",
        "aliases": ["Picasso"],
        "category": "Art",
        "difficulty": 3
    },
    {
        "id": 74,
        "question": "This painter created The Persistence of Memory.",
        "answer": "Salvador Dalí",
        "aliases": ["Dali", "Salvador Dali"],
        "category": "Art",
        "difficulty": 3
    },
    {
        "id": 75,
        "question": "This artist painted the Mona Lisa.",
        "answer": "Leonardo da Vinci",
        "aliases": ["Da Vinci", "Leonardo"],
        "category": "Art",
        "difficulty": 2
    },
    {
        "id": 76,
        "question": "This artist painted the ceiling of the Sistine Chapel.",
        "answer": "Michelangelo",
        "aliases": ["Michelangelo Buonarroti"],
        "category": "Art",
        "difficulty": 2
    },
    {
        "id": 77,
        "question": "This philosopher wrote Leviathan.",
        "answer": "Thomas Hobbes",
        "aliases": ["Hobbes"],
        "category": "Philosophy",
        "difficulty": 3
    },
    {
        "id": 78,
        "question": "This philosopher is associated with natural rights and the idea of life, liberty, and property.",
        "answer": "John Locke",
        "aliases": ["Locke"],
        "category": "Philosophy",
        "difficulty": 3
    },
    {
        "id": 79,
        "question": "This philosopher wrote The Social Contract.",
        "answer": "Jean-Jacques Rousseau",
        "aliases": ["Rousseau", "Jean Jacques Rousseau"],
        "category": "Philosophy",
        "difficulty": 3
    },
    {
        "id": 80,
        "question": "This ancient Greek philosopher was the teacher of Aristotle.",
        "answer": "Plato",
        "aliases": [],
        "category": "Philosophy",
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