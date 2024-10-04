import random

def difficulty_chooser(num):
    match num:
        case 1:
            difficulty = "Easy"
            return difficulty
        case 2:
            difficulty = "Medium"
            return difficulty
        case 3:
            difficulty = "Hard"
            return difficulty

def guesser(real):
    print("Choose the number of plot to hit: ")
    if int(input()) == real.index('Ö') + 1:
        print("Right!")
        main()
    else:
        print("Wrong!")
        print("The real lawn was: ", real)
        main()

def main():
    print("Ghost on a lawn!")
    Easy = ['Ö', 'n', 'n']
    Medium = ['Ö', 'n', 'n', 'n']
    Hard = ['Ö', 'n', 'n', 'n', 'n']
    difficulty = difficulty_chooser(int(input("Choose difficulty: 1 - Easy, 2 - Medium, 3 - Hard: ")))
    match difficulty:
        case "Easy":
            real = sorted(Easy, key=lambda x: random.random())
            print('n', 'n', 'n')
            guesser(real)
        case "Medium":
            real = sorted(Medium, key=lambda x: random.random())
            print('n', 'n', 'n', 'n')
            guesser(real)
        case "Hard":
            real = sorted(Hard, key=lambda x: random.random())
            print('n', 'n', 'n', 'n', 'n')
            guesser(real)

main()

