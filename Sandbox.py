def main() -> None: #Define the function main (codespace #1) 
    pass #Add pass to avoid error (Pass=ignore). Also allows the code below to run without indentation. #MOD=% pseudocode. 
Var1: int = float(input("Enter Number:")) #User is supposed to input an integer, but a float is possible.
if Var1 > 0:
    print("Positive")
elif Var1 < 0:
    print("Negative")
else:
    print("It's Zero")
if Var1 % 2 == 0 and Var1 > 0:
    print("Even")
elif Var1 % 2 == 1:
    print("Odd")
elif Var1 % 1 != 0:
    print("Not an integer")
else: 
    print("...")



if __name__ == "__main__":
    main()
