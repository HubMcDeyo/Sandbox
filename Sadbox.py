def main() -> None:
    string = input()
    Num = string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u")
    Num2 = Num + string.count("y")
    print(Num, Num2)
if __name__ == "__main__":
    main()
