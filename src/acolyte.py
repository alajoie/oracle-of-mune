
class Acolyte:
    def __init__(self):
        self.assertive_counter = 0
        self.intervention_trigger = 0
        self.translations = [
                "No, and...",
                "No.",
                "No, but...",
                "Yes, but...",
                "Yes.",
                "Yes, and..."]

    def interpret(self, answer):
        if self.isIndecisive(answer):
            self.assertive_counter = self.assertive_counter + 1
        else:
            self.assertive_counter = 0
        if self.get_assertive_counter() > 2:
            self.assertive_counter = 0
            return self.forceDecisiveAnswer(answer)
        else:
            index = answer - 1
            return self.translations[index]

    def isIndecisive(self, answer):
        if answer != 2 or answer != 5:
            return True
        return False

    def get_assertive_counter(self):
        return self.assertive_counter

    def forceDecisiveAnswer(self, answer):
        if self.isPositive(answer):
            return "Yes."
        else:
            return "No."

    def isPositive(self, answer):
        if answer >= 4 and answer < 7:
            return True
        return False
            



