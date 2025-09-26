def main() -> None: #Define the function main (codespace #1) 
    pass #Add pass to avoid error (Pass=ignore). Also allows the code below to run without indentation.
Width = int(input("Width:")) #input width
Length = int(input("Length:")) #input length
Area = Width * Length #Area =length*width
Area_mowed = Area / (40 * 60) #The area she mows per hour is the total area divided by 40 ft/min *60 min
Cost = 30 * Area_mowed #Cost=Area mowed per hour *cost per hour
print(f"${Cost:.2f}") #output cost to 2 decimals


if __name__ == "__main__":
    main()
