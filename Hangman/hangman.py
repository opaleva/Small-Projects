from random import choice, seed, randint
from data import words, gallows


def guess_word(correct: str, search_word: str, blank: str) -> None:
    print()
    for i in range(len(search_word)):
        if search_word[i] in correct:
            blank = blank[:i] + search_word[i] + blank[i+1:]
    print(blank.center(125))


def check_correctness(letter: str) -> str:
    if len(letter) != 1:
        print("You should input a single letter")
    elif not letter.isalpha() or not letter.islower():
        print("Please enter a lowercase English letter")
    else:
        return letter


def main():
    seed(randint(1, 1000))
    search_word: str = choice(words)
    correct: str = ""
    wrong: str = ""
    blank: str = "█" * len(search_word)
    print(f'\n {" EXECUTIONER ".center(123, "❀")}')
    print("programming languages".center(125, "~"))

    j: int = 8
    while j > 0:
        guess_word(correct, search_word, blank)
        print("Input a letter:\n".center(125), end="")
        letter = input("".center(8))
        if check_correctness(letter) == letter:
            if letter in correct or letter in wrong:
                print("You've already guessed this letter".center(125))
            elif letter in search_word:
                correct = correct + letter
            elif letter not in search_word:
                print("That letter doesn't appear in the word".center(125))
                wrong = wrong + letter
                print(f'Wrong letters: {" ".join(sorted(wrong))}'.center(125))
                print(gallows[-j])
                j -= 1

        if len(correct) == len(set(search_word)):
            print("\n", f'☰{search_word}☰'.center(121))
            print("You survived!".center(125))
            break
        elif j == 0:
            print("You lost!\n".center(125))


if __name__ == '__main__':
    main()
