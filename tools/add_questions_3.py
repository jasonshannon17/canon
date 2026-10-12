import json


NEW_QUESTIONS = [
    {
        "id": 121,
        "question": "This French military leader was defeated at Waterloo in 1815.",
        "answer": "Napoleon Bonaparte",
        "aliases": ["Napoleon"],
        "category": "World History",
        "difficulty": 2
    },
    {
        "id": 122,
        "question": "This 1815 meeting redrew Europe after the Napoleonic Wars.",
        "answer": "Congress of Vienna",
        "aliases": ["Vienna"],
        "category": "World History",
        "difficulty": 3
    },
    {
        "id": 123,
        "question": "This Austrian statesman was a major figure at the Congress of Vienna.",
        "answer": "Metternich",
        "aliases": ["Klemens von Metternich", "Prince Metternich"],
        "category": "World History",
        "difficulty": 3
    },
    {
        "id": 124,
        "question": "This queen ruled England during the defeat of the Spanish Armada.",
        "answer": "Elizabeth I",
        "aliases": ["Queen Elizabeth I", "Elizabeth the First"],
        "category": "World History",
        "difficulty": 2
    },
    {
        "id": 125,
        "question": "This 1066 battle marked the Norman conquest of England.",
        "answer": "Battle of Hastings",
        "aliases": ["Hastings"],
        "category": "World History",
        "difficulty": 2
    },
    {
        "id": 126,
        "question": "This document was signed by King John in 1215.",
        "answer": "Magna Carta",
        "aliases": ["The Magna Carta"],
        "category": "World History",
        "difficulty": 2
    },
    {
        "id": 127,
        "question": "This Russian czar was known as 'the Great' and built St. Petersburg.",
        "answer": "Peter the Great",
        "aliases": ["Peter I"],
        "category": "World History",
        "difficulty": 2
    },
    {
        "id": 128,
        "question": "This Russian empress was also known as 'the Great.'",
        "answer": "Catherine the Great",
        "aliases": ["Catherine II"],
        "category": "World History",
        "difficulty": 2
    },
    {
        "id": 129,
        "question": "This empire had Suleiman the Magnificent as one of its major rulers.",
        "answer": "Ottoman Empire",
        "aliases": ["Ottoman"],
        "category": "World History",
        "difficulty": 3
    },
    {
        "id": 130,
        "question": "This Mongol leader founded one of history's largest empires.",
        "answer": "Genghis Khan",
        "aliases": ["Chinggis Khan"],
        "category": "World History",
        "difficulty": 2
    },
    {
        "id": 131,
        "question": "This composer wrote the Moonlight Sonata.",
        "answer": "Beethoven",
        "aliases": ["Ludwig van Beethoven"],
        "category": "Classical Music",
        "difficulty": 2
    },
    {
        "id": 132,
        "question": "This composer wrote the 1812 Overture.",
        "answer": "Tchaikovsky",
        "aliases": ["Pyotr Ilyich Tchaikovsky", "Peter Tchaikovsky"],
        "category": "Classical Music",
        "difficulty": 2
    },
    {
        "id": 133,
        "question": "This composer wrote The Planets.",
        "answer": "Gustav Holst",
        "aliases": ["Holst"],
        "category": "Classical Music",
        "difficulty": 3
    },
    {
        "id": 134,
        "question": "This composer wrote Carmina Burana.",
        "answer": "Carl Orff",
        "aliases": ["Orff"],
        "category": "Classical Music",
        "difficulty": 3
    },
    {
        "id": 135,
        "question": "This composer wrote The Rite of Spring.",
        "answer": "Igor Stravinsky",
        "aliases": ["Stravinsky"],
        "category": "Classical Music",
        "difficulty": 3
    },
    {
        "id": 136,
        "question": "This composer wrote the opera Fidelio.",
        "answer": "Beethoven",
        "aliases": ["Ludwig van Beethoven"],
        "category": "Classical Music",
        "difficulty": 3
    },
    {
        "id": 137,
        "question": "This composer wrote Finlandia.",
        "answer": "Jean Sibelius",
        "aliases": ["Sibelius"],
        "category": "Classical Music",
        "difficulty": 3
    },
    {
        "id": 138,
        "question": "This composer wrote The Moldau.",
        "answer": "Bedrich Smetana",
        "aliases": ["Smetana", "Bedřich Smetana"],
        "category": "Classical Music",
        "difficulty": 3
    },
    {
        "id": 139,
        "question": "This scientist developed the polio vaccine commonly associated with an injectable shot.",
        "answer": "Jonas Salk",
        "aliases": ["Salk"],
        "category": "Science",
        "difficulty": 3
    },
    {
        "id": 140,
        "question": "This scientist developed an oral polio vaccine.",
        "answer": "Albert Sabin",
        "aliases": ["Sabin"],
        "category": "Science",
        "difficulty": 3
    },
    {
        "id": 141,
        "question": "This woman won two Nobel Prizes and researched radioactivity.",
        "answer": "Marie Curie",
        "aliases": ["Curie", "Madame Curie"],
        "category": "Science",
        "difficulty": 2
    },
    {
        "id": 142,
        "question": "This scientist is associated with the uncertainty principle.",
        "answer": "Werner Heisenberg",
        "aliases": ["Heisenberg"],
        "category": "Science",
        "difficulty": 3
    },
    {
        "id": 143,
        "question": "This scientist proposed the laws of planetary motion.",
        "answer": "Johannes Kepler",
        "aliases": ["Kepler"],
        "category": "Science",
        "difficulty": 3
    },
    {
        "id": 144,
        "question": "This scientist improved the telescope and supported heliocentrism.",
        "answer": "Galileo Galilei",
        "aliases": ["Galileo"],
        "category": "Science",
        "difficulty": 2
    },
    {
        "id": 145,
        "question": "This astronomer proposed a heliocentric model of the solar system.",
        "answer": "Nicolaus Copernicus",
        "aliases": ["Copernicus"],
        "category": "Science",
        "difficulty": 2
    },
    {
        "id": 146,
        "question": "This scientist's name is attached to the periodic table.",
        "answer": "Dmitri Mendeleev",
        "aliases": ["Mendeleev"],
        "category": "Science",
        "difficulty": 3
    },
    {
        "id": 147,
        "question": "This author wrote The Divine Comedy.",
        "answer": "Dante Alighieri",
        "aliases": ["Dante"],
        "category": "Literature",
        "difficulty": 2
    },
    {
        "id": 148,
        "question": "This author wrote Don Quixote.",
        "answer": "Miguel de Cervantes",
        "aliases": ["Cervantes"],
        "category": "Literature",
        "difficulty": 2
    },
    {
        "id": 149,
        "question": "This author wrote Paradise Lost.",
        "answer": "John Milton",
        "aliases": ["Milton"],
        "category": "Literature",
        "difficulty": 3
    },
    {
        "id": 150,
        "question": "This author wrote The Canterbury Tales.",
        "answer": "Geoffrey Chaucer",
        "aliases": ["Chaucer"],
        "category": "Literature",
        "difficulty": 3
    },
    {
        "id": 151,
        "question": "This author wrote The Stranger.",
        "answer": "Albert Camus",
        "aliases": ["Camus"],
        "category": "Literature",
        "difficulty": 3
    },
    {
        "id": 152,
        "question": "This author wrote One Hundred Years of Solitude.",
        "answer": "Gabriel García Márquez",
        "aliases": ["Gabriel Garcia Marquez", "García Márquez", "Garcia Marquez", "Marquez"],
        "category": "Literature",
        "difficulty": 3
    },
    {
        "id": 153,
        "question": "This author wrote The Odyssey and The Iliad.",
        "answer": "Homer",
        "aliases": [],
        "category": "Literature",
        "difficulty": 2
    },
    {
        "id": 154,
        "question": "This author wrote Anna Karenina and War and Peace.",
        "answer": "Leo Tolstoy",
        "aliases": ["Tolstoy"],
        "category": "Literature",
        "difficulty": 2
    },
    {
        "id": 155,
        "question": "This musical features Jean Valjean and Javert.",
        "answer": "Les Misérables",
        "aliases": ["Les Miserables", "Les Mis"],
        "category": "Theatre",
        "difficulty": 2
    },
    {
        "id": 156,
        "question": "This musical features the songs 'Memory' and 'Jellicle Songs for Jellicle Cats.'",
        "answer": "Cats",
        "aliases": [],
        "category": "Theatre",
        "difficulty": 2
    },
    {
        "id": 157,
        "question": "This musical features Eva Perón.",
        "answer": "Evita",
        "aliases": [],
        "category": "Theatre",
        "difficulty": 2
    },
    {
        "id": 158,
        "question": "This musical by Lin-Manuel Miranda is about one of America's Founding Fathers.",
        "answer": "Hamilton",
        "aliases": [],
        "category": "Theatre",
        "difficulty": 2
    },
    {
        "id": 159,
        "question": "This playwright wrote A Streetcar Named Desire and The Glass Menagerie.",
        "answer": "Tennessee Williams",
        "aliases": ["Williams"],
        "category": "Theatre",
        "difficulty": 3
    },
    {
        "id": 160,
        "question": "This playwright wrote Death of a Salesman and The Crucible.",
        "answer": "Arthur Miller",
        "aliases": ["Miller"],
        "category": "Theatre",
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
    json.dump(existing_questions, file, indent=4)

print(f"Done. Question bank now has {len(existing_questions)} questions.")