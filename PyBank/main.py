# Modules
import os
import csv

# Open budget_data.csv
file = os.path.join('..','PyBank','Resources','budget_data.csv')
with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    
    #Declare and initiate variables
    Month =[]
    ProfitLosses =[]
    ProfitChange =[]
    totalProfitLosses = 0
    GreatestIncrease = 0
    GreatestDecrease = 0
    GreatestIncreaseMonth =""
    GreatestDecreaseMonth =""
    AverageChange = 0
    profitLossesChangeTotal = 0
    
    #Loop through all rows in the file, and calcuate total Profit/Losses
    #Assign values to the list of month and profitlosses
    for row in csvreader:
        totalProfitLosses += int(row[1])
        Month.append(row[0])
        ProfitLosses.append(row[1])
    for i in (range(len(ProfitLosses)-1)):
        ProfitChange.append(int(ProfitLosses[i+1])-int(ProfitLosses[i]))
        i+=1
    for i in (range(len(ProfitChange))):
        profitLossesChangeTotal += ProfitChange[i]
        i+=1
    #Calculate averate changes - change between end period profit/losses and beginning profit/losses, and then divide by total periods
    AverageChange = profitLossesChangeTotal/len(ProfitChange)
    AverageChange = "{:.2f}".format(AverageChange)
    #Compare and find the greatest increase and greatest decrease value
    for i in range(len(ProfitChange)):
        if int(ProfitChange[i]) > GreatestIncrease:
            GreatestIncrease = int(ProfitChange[i])
            GreatestIncreaseMonth = Month[i+1]
        else:
            GreatestIncrease = GreatestIncrease
        if int(ProfitChange[i]) < GreatestDecrease:
            GreatestDecrease = int(ProfitChange[i])
            GreatestDecreaseMonth = Month[i+1]
        else:
            GreatestDecrease = GreatestDecrease

        i+=1
    #Print out the results
    print("Financial Analysis")
    print("-----------------------------------------------------")
    print(f"Total Months: {len(Month)}")
    print(f"Total: ${totalProfitLosses}")
    print(f"Average Change: ${AverageChange}")
    print(f"Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncrease})")
    print(f"Greatest Decrease in Profits: {GreatestDecreaseMonth} (${GreatestDecrease})")

# Write output to a text file
output_path = os.path.join("..", "PyBank","output", "PyBankResult.txt")

with open(output_path, 'w', newline='') as outputfile:

    outputfile.write(f"Financial Analysis"'\n')
    outputfile.write(f"-----------------------------------------------------"'\n')
    outputfile.write(f"Total Months: {len(Month)}"'\n')
    outputfile.write(f"Total: ${totalProfitLosses}"'\n')
    outputfile.write(f"Average Change: ${AverageChange}"'\n')
    outputfile.write(f"Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncrease})"'\n')
    outputfile.write(f"Greatest Decrease in Profits: {GreatestDecreaseMonth} (${GreatestDecrease})"'\n')
    outputfile.close

