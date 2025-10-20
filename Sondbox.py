from itertools import repeat


def mainfunction() -> None:
    # Read input, remove spaces, reverse the string and check palindrome
    String = input("Enter a string: ")  # Get the String
    Strong = String.replace(" ", "")  # remove all spaces

    # create reversed string using slice with step -1
    reversed_str = Strong[::-1]

    # case-insensitive palindrome check
    if Strong.lower() == reversed_str.lower():
        print("palindrome:", String)
    else:
        # print the reversed form (not empty)
        print("not a palindrome:", reversed_str)


if __name__ == "__main__":
    mainfunction()