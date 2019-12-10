import csv

def csv_row_to_dict(row):
    return {
        "question_text": row[0],
        "options": row[1].split("."),
        "answer_index": int(row[2])
    }

def import_questions_from_csv():
    questions = []
    with open('qns.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            questions.append(csv_row_to_dict(row))

    return questions

