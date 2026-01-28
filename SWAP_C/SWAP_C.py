"""Solution for SWAP-C
Miles Deyo-1/13/26"""


import sys

def main() -> None:
    Best_score: int = 99999999999999 #approx. infinite to start. 
    test_case_count: int = int(sys.stdin.readline().rstrip())
    for g in range(test_case_count):
        orig_data: str = sys.stdin.readline().rstrip()
        E,A,B,C,D = orig_data.split()
        Score1 = int(A) + int(B) + int(C) + int(D) #E represents model number, which isn't needed in the score calculation.
        case_count: str = int(sys.stdin.readline().rstrip())
        for _ in range(case_count): 
            Percent = Score1 * 0.8  #80% of Score1 
            comp_data: str = sys.stdin.readline().rstrip() #comparison data
            comp_model_num, comp_size, comp_weight, comp_power, comp_cost = comp_data.split()
            comp_score = int(comp_size) + int(comp_weight) + int(comp_power) + int(comp_cost) #comparison data score. 
            if comp_score < Best_score: #if the comp_score is less than or equal to 80% of Score1, then best score is now comp_score. 
                Best_score = comp_score #best score only becomes the comp_score if less than or equal to percent, and it's less than the current best_score.
                Best_model = comp_model_num
            if Best_score <= Percent:
                print(Best_model, Best_score) 
            elif Best_score > Percent:
                print(E, Score1) 
            

        






if __name__ == "__main__":
    main()
