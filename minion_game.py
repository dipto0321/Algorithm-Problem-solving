# https://www.hackerrank.com/challenges/the-minion-game/problem


def minion_game(string: str) -> None:
    """
    Play the 'Minion Game' where two players, Kevin and Stuart, compete to form words from the given string.
    Kevin can only use words starting with vowels, while Stuart can only use words starting with consonants.
    Each player's score is the total number of times their words appear in the original string.

    Args:
        string (str): The string from which words are formed.

    Prints:
        str: The winner and their score in the format "WinnerName Score" or "Draw" if there is no winner.
    Note:
        1. The time complexity of this solution is O(n) where n is the length of the input string.
        2. The space complexity of this solution is O(1) as it uses a constant amount of extra space.
        3. The solution is efficient and can handle large inputs.
        4. 'length - i' is the number of substrings that can be formed starting from the character at index i. This is a quick and efficient way of calculating substrings occurrences including overlapping.
    """
    k_score, s_score = 0, 0
    length = len(string)
    VOWELS = "AEIOU"

    for i in range(length):
        if string[i] in VOWELS:
            k_score += length - i
        else:
            s_score += length - i

    if k_score > s_score:
        print(f"Kevin {k_score}")
    elif s_score > k_score:
        print(f"Stuart {s_score}")
    else:
        print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)
