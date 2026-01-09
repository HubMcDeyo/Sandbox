import sys

def main() -> None: #Define the function main (codespace #1) 
    case_count: int = int(sys.stdin.readline().rstrip())
    Primary_colors = "yellow blue red"
    for g in range(case_count): 
        Color: str = sys.stdin.readline().rstrip()
        if Color == "violet":
            print("In order to make violet, blue and red must be mixed.")
        if Color == "blue-green":
            print("In order to make blue-green, blue and yellow must be mixed.")
        if Color == "yellow":
            print("No colors need to be mixed to make yellow.")
        if Color == "orange":
            print("In order to make orange, red and yellow must be mixed.")
        if Color in Primary_colors:
            print(f"No colors need to be mixed to make {Color}")
if __name__ == "__main__":
    main()

#if "-" in Color: 
           # tokens = Color.split("-")
          #  a = tokens[0]
          #  b = tokens[1]
      #  if Color ==
         #   print(f"In order to make {Color}, ")