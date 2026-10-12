import json


NEW_QUESTIONS = [
    {
        "id": 201,
        "question": "This word describes a word that imitates the sound it names, like 'buzz' or 'clang'.",
        "answer": "onomatopoeia",
        "aliases": ["onomatopoeic"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    },
    {
        "id": 202,
        "question": "This common prefix meaning 'against' or 'opposite' appears in words like antifreeze and antibody.",
        "answer": "anti",
        "aliases": ["anti-"],
        "category": "Language / Vocabulary",
        "difficulty": 1
    },
    {
        "id": 203,
        "question": "This suffix meaning 'the study of' appears in biology, geology, and theology.",
        "answer": "ology",
        "aliases": ["-ology"],
        "category": "Language / Vocabulary",
        "difficulty": 1
    },
    {
        "id": 204,
        "question": "Meaning 'good' or 'well', this Latin root appears in benefit, benevolent, and benign.",
        "answer": "bene",
        "aliases": ["ben"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    },
    {
        "id": 205,
        "question": "Meaning 'bad' or 'evil', this Latin root appears in malicious, malady, and malfunction.",
        "answer": "mal",
        "aliases": ["male"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    },
    {
        "id": 206,
        "question": "Meaning 'all', this root appears in omnipotent, omnivore, and omnibus.",
        "answer": "omni",
        "aliases": ["omni-"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    },
    {
        "id": 207,
        "question": "Meaning 'many', this Greek-derived prefix appears in polygon, polyglot, and polytheism.",
        "answer": "poly",
        "aliases": ["poly-"],
        "category": "Language / Vocabulary",
        "difficulty": 1
    },
    {
        "id": 208,
        "question": "Meaning 'one' or 'single', this prefix appears in monologue, monopoly, and monotheism.",
        "answer": "mono",
        "aliases": ["mono-"],
        "category": "Language / Vocabulary",
        "difficulty": 1
    },
    {
        "id": 209,
        "question": "A word that is spelled the same as another word but has a different meaning, like 'bat' the animal and 'bat' used in baseball, is this.",
        "answer": "homonym",
        "aliases": ["homonyms"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    },
    {
        "id": 210,
        "question": "A word that sounds like another word but has a different meaning, like 'flower' and 'flour', is this.",
        "answer": "homophone",
        "aliases": ["homophones"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    },
    {
        "id": 211,
        "question": "A word with the opposite meaning of another word is called this.",
        "answer": "antonym",
        "aliases": ["antonyms"],
        "category": "Language / Vocabulary",
        "difficulty": 1
    },
    {
        "id": 212,
        "question": "A word with the same or nearly the same meaning as another word is called this.",
        "answer": "synonym",
        "aliases": ["synonyms"],
        "category": "Language / Vocabulary",
        "difficulty": 1
    },
    {
        "id": 213,
        "question": "This term means a word formed from the first letters of a phrase, like NASA or SCUBA.",
        "answer": "acronym",
        "aliases": ["acronyms"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    },
    {
        "id": 214,
        "question": "A word or phrase that reads the same forward and backward, like 'level' or 'madam', is this.",
        "answer": "palindrome",
        "aliases": ["palindromes"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    },
    {
        "id": 215,
        "question": "This punctuation mark is used to show possession or to mark omitted letters in a contraction.",
        "answer": "apostrophe",
        "aliases": ["an apostrophe"],
        "category": "Language / Vocabulary",
        "difficulty": 1
    },
    {
        "id": 216,
        "question": "This punctuation mark is used to join words in compounds like 'well-known' or to split words at line breaks.",
        "answer": "hyphen",
        "aliases": ["a hyphen"],
        "category": "Language / Vocabulary",
        "difficulty": 1
    },
    {
        "id": 217,
        "question": "This punctuation mark can join two closely related independent clauses; it is stronger than a comma but weaker than a period.",
        "answer": "semicolon",
        "aliases": ["semi-colon", "a semicolon"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    },
    {
        "id": 218,
        "question": "This mark made of three dots can indicate omitted words or a trailing-off thought.",
        "answer": "ellipsis",
        "aliases": ["ellipses", "three dots"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    },
    {
        "id": 219,
        "question": "In grammar, a noun that names a person, place, thing, or idea is this part of speech.",
        "answer": "noun",
        "aliases": ["a noun"],
        "category": "Language / Vocabulary",
        "difficulty": 1
    },
    {
        "id": 220,
        "question": "In grammar, a word that modifies a verb, adjective, or another word of the same type is called this.",
        "answer": "adverb",
        "aliases": ["an adverb"],
        "category": "Language / Vocabulary",
        "difficulty": 1
    },
    {
        "id": 221,
        "question": "In grammar, this part of speech connects words, phrases, or clauses; examples include 'and', 'but', and 'or'.",
        "answer": "conjunction",
        "aliases": ["a conjunction"],
        "category": "Language / Vocabulary",
        "difficulty": 1
    },
    {
        "id": 222,
        "question": "A word placed before a noun or pronoun to show a relationship, as in 'on the table' or 'under the bridge', is this part of speech.",
        "answer": "preposition",
        "aliases": ["a preposition"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    },
    {
        "id": 223,
        "question": "This word for a newly coined term or expression comes from Greek roots meaning 'new' and 'word'.",
        "answer": "neologism",
        "aliases": ["neologisms"],
        "category": "Language / Vocabulary",
        "difficulty": 3
    },
    {
        "id": 224,
        "question": "This term means a mild or indirect word substituted for one considered too harsh, as 'passed away' for 'died'.",
        "answer": "euphemism",
        "aliases": ["euphemisms"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    },
    {
        "id": 225,
        "question": "This term means a deliberately harsh or blunt expression, the opposite of a euphemism.",
        "answer": "dysphemism",
        "aliases": ["dysphemisms"],
        "category": "Language / Vocabulary",
        "difficulty": 3
    },
    {
        "id": 226,
        "question": "This figure of speech directly compares two unlike things using 'like' or 'as'.",
        "answer": "simile",
        "aliases": ["a simile"],
        "category": "Language / Vocabulary",
        "difficulty": 1
    },
    {
        "id": 227,
        "question": "This figure of speech describes one thing as another without using 'like' or 'as'.",
        "answer": "metaphor",
        "aliases": ["a metaphor"],
        "category": "Language / Vocabulary",
        "difficulty": 1
    },
    {
        "id": 228,
        "question": "This figure of speech gives human qualities to nonhuman things, as when the wind 'whispers'.",
        "answer": "personification",
        "aliases": ["personifying"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    },
    {
        "id": 229,
        "question": "This figure of speech uses deliberate exaggeration for effect, as in 'I've told you a million times'.",
        "answer": "hyperbole",
        "aliases": ["exaggeration"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    },
    {
        "id": 230,
        "question": "This term describes repeated initial consonant sounds, as in 'Peter Piper picked a peck'.",
        "answer": "alliteration",
        "aliases": ["alliterative"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    },
    {
        "id": 231,
        "question": "This term describes repeated vowel sounds, as in the long 'o' sound in 'go slow over the road'.",
        "answer": "assonance",
        "aliases": ["assonant"],
        "category": "Language / Vocabulary",
        "difficulty": 3
    },
    {
        "id": 232,
        "question": "This term describes repeated consonant sounds, often at the ends of words, as in 'pitter patter'.",
        "answer": "consonance",
        "aliases": ["consonant repetition"],
        "category": "Language / Vocabulary",
        "difficulty": 3
    },
    {
        "id": 233,
        "question": "In poetry, this five-foot meter with an unstressed-stressed rhythm is strongly associated with Shakespeare.",
        "answer": "iambic pentameter",
        "aliases": ["iambic pentametre", "pentameter", "pentametre"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    },
    {
        "id": 234,
        "question": "This 14-line poetic form is associated with Shakespeare, Petrarch, and strict rhyme schemes.",
        "answer": "sonnet",
        "aliases": ["a sonnet"],
        "category": "Language / Vocabulary",
        "difficulty": 1
    },
    {
        "id": 235,
        "question": "This poetic term means the continuation of a sentence beyond the end of a line or stanza.",
        "answer": "enjambment",
        "aliases": ["enjambement"],
        "category": "Language / Vocabulary",
        "difficulty": 3
    },
    {
        "id": 236,
        "question": "This term means a phrase whose meaning cannot be understood from the literal meanings of its words, like 'kick the bucket'.",
        "answer": "idiom",
        "aliases": ["an idiom", "idiomatic expression"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    },
    {
        "id": 237,
        "question": "This term means a shortened form of a word or phrase, like 'Dr.' for doctor.",
        "answer": "abbreviation",
        "aliases": ["abbreviations"],
        "category": "Language / Vocabulary",
        "difficulty": 1
    },
    {
        "id": 238,
        "question": "This term means a word created by combining parts of two other words, like brunch from breakfast and lunch.",
        "answer": "portmanteau",
        "aliases": ["blend", "word blend"],
        "category": "Language / Vocabulary",
        "difficulty": 3
    },
    {
        "id": 239,
        "question": "This term means a word that comes from the name of a person, like boycott or sandwich.",
        "answer": "eponym",
        "aliases": ["eponyms"],
        "category": "Language / Vocabulary",
        "difficulty": 3
    },
    {
        "id": 240,
        "question": "This term means the history and origin of a word.",
        "answer": "etymology",
        "aliases": ["word origin", "word origins"],
        "category": "Language / Vocabulary",
        "difficulty": 2
    }
]


with open("../data/questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)


existing_ids = set()

for question in questions:
    existing_ids.add(question["id"])


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