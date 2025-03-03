"""My own Wordle guessing game!"""

__author__ = "730557969"


def contains_char(word: str, letter: str) -> bool:
    """Working through each letter of a given word"""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    idx: int = 0
    while idx < len(word):
        """Allows the function to evaluate letter at each index of word"""
        if word[idx] == letter:  # the word does contain the letter
            return True
        idx = idx + 1  # adds to the index to continue on
    return False  # the word does not contain the letter


"""Variables needed for emojified (colored boxes)"""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Function for Emojis to indicate if letters in guess match the secret word!"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    idx: int = 0
    string: str = ""  # allows colored boxes to be in one string
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            string = string + GREEN_BOX  # correct letter at correct location
        else:
            if contains_char(word=secret, letter=guess[idx]) == True:
                string = string + YELLOW_BOX  # word has letter but wrong location
            else:
                string = string + WHITE_BOX  # word does not contain that letter
        idx = idx + 1  # moves onto the next index/letter
    return string


def input_guess(expected_length: int) -> str:
    """Function to indicate if guess length matches secret word length"""
    word_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(word_guess) != expected_length:  # expected length and guess don't match
        word_guess = input(f"That wasn't {expected_length} chars! Try again!")
    return word_guess  # expected length and guess do match


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    wordle_guess: str = ""  # will reassign variable throughout program as you guess
    n: int = 1  # number of turns taken
    while secret != wordle_guess and n <= 6:
        """Secret word and your guess don't match but still have turns left!"""
        print(f"=== Turn {n}/6 ===")
        wordle_guess = input_guess(expected_length=len(secret))
        """Makes sure guess and secret word match in length"""
        print(emojified(guess=wordle_guess, secret=secret))
        """Indicates correctness of individual letters of guess compared to secret"""
        n += 1  # used up one of your turns
        """Next turn with new guess"""
    if secret == wordle_guess:  # You won and are done!
        print(f"You won in {n-1}/6 turns!")  # (n-1): for N+=1 when while loop is False
    else:  # You did not guess secret word and ran out of turns
        print("X/6 - Sorry, try again tomorrow")


if __name__ == "__main__":
    main(secret="codes")  # when program runs, secret word will be "codes"
