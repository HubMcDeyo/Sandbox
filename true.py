import sys
import math
import string


def main() -> None:
    test_cases = int(sys.stdin.readline().rstrip())
    time_to_collide = 0
    for _ in range(test_cases):
        cases=int(sys.stdin.readline().rstrip())
        for caseNum in range(cases):
            case_info = sys.stdin.readline().rstrip()
            v, x = case_info.split(':')
            x= float(x)
            v=float(v)
            if v == 0: 
                time_to_collide = "SAFE"
            print(time_to_collide)
        else:
            time_to_collide = x / v
            if time_to_collide <= 1:
                print("SWERVE")
            elif time_to_collide <= 5:
                print("BRAKE")
            else:
                print("SAFE")
if __name__ == "__main__":
    main()
