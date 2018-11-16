import random

class Balance(self):
    def __init__(self):
        self.balance_of_fate = 0
        self.interventions = [
                "New entity",
                "Entity positive",
                "Entity negative",
                "Advance plot",
                "Regress plot",
                "Wild"]

    def getBalanceOfFate(self):
        return self.balance_of_fate

    def weighOnBalance(self, roll):
        if roll == 6:
            self.balance_of_fate = self.balance_of_fate + 1

    def checkBalanceOfFate(self):
        if self.getBalanceOfFate() > 2:
            self.balance_of_fate = 0
            return self.triggerIntervention()
        else:
            return ""

    def triggerIntervention(self):
        return self.interventions[random.randint(0,5)]

