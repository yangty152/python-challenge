import os

import csv

file = os.path.join('..','PyBank','Resources','budget_data.csv')
print(file)
with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    Month = []
    ProfitLosses =[]
    totalProfitLosses = 0
    GreatestIncrease = 0
    GreatestDecrease = 0
    csv_header = next(csvreader)
    i = 0
    GreatestIncreaseMonth =""
    GreatestDecreaseMonth =""
    AverageChange = 0
    
    for row in csvreader:
        totalProfitLosses += int(row[1])
        Month.append(row[0])
        ProfitLosses.append(row[1])

    for i in range(len(Month)):
        if int(ProfitLosses[i]) > GreatestIncrease:
            GreatestIncrease = int(ProfitLosses[i])
            GreatestIncreaseMonth = Month[i]
        else:
            GreatestIncrease = GreatestIncrease
        if int(ProfitLosses[i]) < GreatestDecrease:
            GreatestDecrease = int(ProfitLosses[i])
            GreatestDecreaseMonth = Month[i]
        else:
            GreatestDecrease = GreatestDecrease

        i+=1
    AverageChange = totalProfitLosses/len(Month)
    print("Financial Analysis")
    print("-----------------------------------------------------")
    print(f"Total Months: {len(Month)}")
    print(f"Total: ${totalProfitLosses}")
    print(f"Average Change: ${AverageChange}")
    print(f"Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncrease})")
    print(f"Greatest Decrease in Profits: {GreatestDecreaseMonth} (${GreatestDecrease})")


