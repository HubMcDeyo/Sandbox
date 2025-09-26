def main() -> None: #Define the function main (codespace #1) 
    pass #Add pass to avoid error (Pass=ignore). Also allows the code below to run without indentation.
Width = int(input("Width:")) #input width
Length = int(input("Length:")) #input length
Area = Width * Length #Area =length*width
Time = 10 + (Area / 40) #Time=10 minutes (load time) + (Area / 40) where 40 is the rate she mows in ft/min.
Area_Time = Area / Time #The area she mows per hour is the total area divided by the Time.
Cost = (30 / 60) * Area_Time #Cost=Area mowed per hour *cost per minute (30 / 60).
print(f"${Cost:.2f}") #output cost to 2 decimals


if __name__ == "__main__":
    main()
