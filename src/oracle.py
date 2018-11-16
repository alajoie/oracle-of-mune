import random

class Oracle:
    def ask(self, likelihood):       
        if likelihood == "Advantage":
            return max(self.__roll(), self.__roll())
        elif likelihood == "Disadvantage":
            return min(self.__roll(), self.__roll())
        else:
            return self.__roll()

    
    def __roll(self):
        return random.randint(1,6)
        
