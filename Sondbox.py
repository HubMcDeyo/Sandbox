def main() -> None:
    pass
a, b = input().split(" ")
a = int(a)
b = int(b)
if a > b:
    print(b, a)
else:
    print(a, b)
if __name__ == "__main__":
    main()