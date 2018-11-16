import oracle
import acolyte

def ask_the_oracle():
    o = oracle.Oracle()
    a = acolyte.Acolyte()

    while True:
        answer = 0
        print("Ask the Oracle a [L]ikely, [N]eutral, or [U]likely Question")
        print("Seek a [P]ortent or consult the [T]WENE")
        print("or [D]epart in peace.")
        print("\n")
        inquiry = input('What knowledge do you seek: ')
        if inquiry == 'L' or inquiry =='l':
            print("The Oracle responds to your LIKELY inquiry: ")
            answer = o.ask("Advantage")
            print(str(a.interpret(answer)) + '\n')
        elif inquiry == 'N'or inquiry == 'n':
            print("The Oracle responds to your NEUTRAL inquiry: ")
            answer = o.ask('N')
            print("\033[31m" + str(a.interpret(answer)) + "\033[37m" + "\n")
        elif inquiry == 'U' or inquiry == 'u':
            print("The Oracle responds to your UNLIKELY inquiry: ")
            answer = o.ask("Disadvantage")
            print(str(a.interpret(answer)) + '\n')
        elif inquiry == 'P' or inquiry == 'p':
            print("PORTENT")
        elif inquiry == 'T' or inquiry == 't':
            print("TWENE")
        elif inquiry == 'D' or inquiry == 'd':
            print("May Wisdom light your footsteps Adventurer!")
            return False
        else:
            print("The Acolyte is uncertain how to explain your inquiry. Try again.")

def main():
    ask_the_oracle()

if __name__ == '__main__':
    main()

