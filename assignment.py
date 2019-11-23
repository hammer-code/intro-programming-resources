from typing import List
import random

def print_separator():
    print('--------------')

class Options(object):
    def __init__(self, options: list, answer_index: int):
        if len(options) != 4:
            raise ValueError("options should have 4 elements")

        if not self.is_valid_answer_index(answer_index):
            raise ValueError("answer_index should be between 0 - 4")

        self.options = options
        self.answer_index = answer_index

    def print(self):
        for index in range(len(self.options)):
            option = self.options[index]
            print(f"{index}) {option}")

    def is_correct_answer(self, chosen_index: int):
        return self.answer_index == chosen_index

    def is_valid_answer_index(self, answer_index: int):
        return answer_index >= 0 and answer_index <= 4

class Question(object):
    def __init__(self, text: str, options: Options):
        self.text = text
        self.options = options

    def get_answer(self):
        answered = False
        answer = None
        while not answered:
            answer = input("Your answer: ")
            try:
                answer = int(answer)
            except ValueError:
                print("Should be number")
                continue

            if self.options.is_valid_answer_index(answer):
                answered = True
            else:
                print("Please choose between 0-3")

        return answer

    def is_correct(self, answer: int):
        return self.options.is_correct_answer(answer)

    def ask(self, number):
        print(f"{number}) {self.text}")
        print("Options:")
        self.options.print()

        answer = self.get_answer()
        return self.is_correct(answer)

class Assigments:
    def __init__(self, title: str, questions: List[Question]):
        self.title = title
        self.questions = questions
        self.answers = []

        random.shuffle(self.questions)

    def run(self):
        print(f"Welcome to {self.title} assigments!")
        print("Please answer the following questions")
        print_separator()

        n = 1
        for q in self.questions:
            self.answers.append(q.ask(1))
            print_separator()
            n += 1

        self._print_score()

    def _get_score(self):
        questions_count = len(self.questions)
        correct_answers_count = len(list(filter(lambda answer: answer is True, self.answers)))
        return (correct_answers_count / questions_count) * 100

    def _print_score(self):
        score = self._get_score()
        print("Your score: ", score)