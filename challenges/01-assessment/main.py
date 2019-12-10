from importer import import_questions_from_csv
from assignment import Question, Options, Assigments

qns = [
    Question("5 + 5 = ", Options([10, 2, 3, 4]), 0),
    Question("Who is Indonesian first president?", Options(["Hatta", "SBY", "Soekarno", "Jokowi"]), 2),
    Question("What is capital city of Japan?", Options(["Palu", "Tokyo", "Kuala Lumpur", "Bangkok"]), 1),
    Question("8 ^ 2 = ", Options(["32", "16", "125", "64"]), 3),
    Question("Who is the creator of python programming language?", Options(["Guido van Rossum", "Kent Beck", "Bob Martin", "Dan Abramov"]), 0),
]

for q in import_questions_from_csv():
    text = q["question_text"]
    options = Options(q["options"])
    qns.append(Question(text, options, q["answer_index"]))

assigment = Assigments("General Knowledge", qns)

if __name__ == "__main__":
    try:
        assigment.run()
    except KeyboardInterrupt:
        print("")
        print("Bye!")
