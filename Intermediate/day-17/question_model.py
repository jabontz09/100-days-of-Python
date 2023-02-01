class Question:

    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer

new_q = Question("whos the strongest avenger", "Hulk")
print(f"{new_q.text}: {new_q.answer}")