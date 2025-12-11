# QUESTION
class question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkanswer(self, answer):
        return self.answer == answer


# QUIZ
class quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionindex = 0

    def getquestion(self):
        return self.questions[self.questionindex]

    def displayquestion(self):
        question = self.getquestion()
        print(f"\nSoru {self.questionindex + 1}: {question.text}")

        for q in question.choices:
            print("- " + q)

        answer = input("Cevap: ")
        self.guess(answer)
        self.loadquestion()

    def guess(self, answer):
        question = self.getquestion()
        if question.checkanswer(answer):
            self.score += 1
        self.questionindex += 1

    def loadquestion(self):
        if self.questionindex == len(self.questions):
            self.showscore()
        else:
            self.displayprogress()
            self.displayquestion()

    def showscore(self):
        print("\nQuiz bitti!")
        print("Skor:", self.score)

    def displayprogress(self):
        total = len(self.questions)
        current = self.questionindex + 1
        print(f"Question {current} of {total}".center(50, "*"))


# SORULAR
q1 = question("En iyi programlama dili hangisidir?", ["c#", "python", "java", "c++"], "python")
q2 = question("En popüler programlama dili hangisidir?", ["c++", "python", "java", "c#"], "python")
q3 = question("En çok kazandıran programlama dili hangisidir?", ["c++", "java", "python", "c#"], "python")

questions = [q1, q2, q3]

# QUIZ ÇALIŞTIR
quiz = quiz(questions)
quiz.displayquestion()
