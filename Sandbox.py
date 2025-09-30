def main() -> None: #Define the function main (codespace #1) 
    pass #Add pass to avoid error (Pass=ignore). Also allows the code below to run without indentation. #MOD=% pseudocode. 
Var1: int = float(input()) #User is supposed to input an integer, but a float is possible.
if Var1 > 0:
    print("Positive")
if Var1 < 0:
    print("Negative")
if Var1 == 0:
    print("It's Zero")
if Var1 % 2 == 0:
    print("Even")
if Var1 % 2 == 1:
    print("Odd")
if Var1 % 1 != 0:
    print("It was supposed to be an integer")



if __name__ == "__main__":
    main()
