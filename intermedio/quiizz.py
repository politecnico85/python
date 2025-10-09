class Quizz:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        for i, option in enumerate(question.options):
            print(f"{i + 1}. {option}")
        answer = input("Enter the number of the correct answer: ")
        if question.options[int(answer) - 1] == question.answer:
            score += 1
    print(f"You got {score} out of {len(questions)} correct!")

questions = [
    Question("What is the capital of France?", ["Berlin", "London", "Paris", "Madrid"], "Paris"),
    Question("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
    Question("What is the color of the sky?", ["Green", "Blue", "Red", "Yellow"], "Blue")
]

run_quiz(questions)
