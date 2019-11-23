from typing import List
import random
from util import print_separator, index_to_char, char_to_index

class Options(object):
    def __init__(self, options: list):
        if len(options) != 4:
            raise ValueError("options should have 4 elements")

        self.options = options

    def print(self):
        for index in range(len(self.options)):
            option = self.options[index]
            print(f"{index_to_char(index)}) {option}")

class Question(object):
    valid_answers = ['a', 'b', 'c', 'd']
    def __init__(self, text: str, options: Options, answer_index: int):
        self.text = text
        self.options = options

        if not self.is_valid_answer_index(answer_index):
            raise ValueError("answer_index should be between 0 - 4")

        self.answer_index = answer_index

    def is_valid_answer_index(self, answer_index: int):
        return answer_index >= 0 and answer_index <= 4

    def is_valid_answer(self, answer: str):
        return answer in self.valid_answers

    def get_answer(self):
        answered = False
        answer = None
        while not answered:
            answer = input("Your answer: ")

            if self.is_valid_answer(answer):
                answered = True
            else:
                print("Please choose either {}".format(",".join(self.valid_answers)))

        return char_to_index(answer)

    def is_correct_answer(self, chosen_index: int):
        return self.answer_index == chosen_index

    def is_correct(self, answer: int):
        return self.is_correct_answer(answer)

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
            self.answers.append(q.ask(n))
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
