def main() -> None:
    loop = int(input())
    eel = 0
    final = 0
    for i in range(loop):
        eel = int(input())
        for g in range(eel+1):
            final = g*(g-1)
    print(final)
if __name__ == "__main__":
    main()
