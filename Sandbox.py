import sys

def main() -> None: #Define the function main (codespace #1) 
    case_count: int = int(sys.stdin.readline().rstrip())
    Violets = ["violet", "blue-violet", "red-violet"] #note that all types are string lists. Use brackets to make a list, as having each type as a string means that a color could be in multiple segments at once.
    Greens = ["blue-green", "green", "yellow-green"]
    Oranges = ["orange", "red-orange", "yellow-orange"]
    Primaries = ["blue", "yellow", "red"]
    for g in range(case_count): 
        Color: str = sys.stdin.readline().rstrip()
        if Color in Primaries:
            print(f"No colors need to be mixed to make {Color}.")
        elif Color in Violets:
            print(f"In order to make {Color}, blue and red must be mixed.")
        elif Color in Greens:
            print(f"In order to make {Color}, blue and yellow must be mixed.") #The number of types of secondary colors (e.g oranges and violets) is n!/2 n=primary colors.
        elif Color in Oranges: #Number of total colors with a max level of secondary= 3/2 * n! + n. (n!/2 +n! +n) double the number in the next level (from the previous level). All colors (any level) = (sum (2^(b-3)*n!) from 2 to b, (steps of 1; integers only)) + n.  (e.g type is b. secondary colors=b is 2. primary=b is 1. tertiary, b is 3).
            print(f"In order to make {Color}, red and yellow must be mixed.")
if __name__ == "__main__":
    main()