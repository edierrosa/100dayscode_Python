class Question:
    """Models a question object."""

    def __init__(self, question_text, question_answer):
        self.text = question_text
        self.answer = question_answer
