import csv
import statistics 

list_months = []
list_pl = []


with open('budget_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    for column in csv_reader:
        Months, Profitlosses = column
        list_pl.append(int(Profitlosses))
        list_months.append(str(Months))
        

#Total number of months

totalmonths = (len(list_months))

#Total Amount
netamount = sum(list_pl)

#Average Change between months over the entire period

net_change = [y - x for x, y in zip(list_pl[:-1], list_pl[1:])]

def straight_average(num_list):
    total = 0.0
    length = len(num_list)
    for num in num_list:
        total += float(num)
    return (total/length)


#The greatest increase in profits (date and amount) over the entire period



netamounts = sum(list_pl)
total_months = len(list_months)
max_val = max(list_pl)
min_val = min(list_pl)
list_minmax = list(zip(list_pl, list_months))

max_change = max(list_pl) 
max_date = max(list_months)


#The greatest decrease in losses (date and amount) over the entire period

min_change = min(list_pl)
min_date = min(list_months)

#Final Result

results = (f" Total Months: {totalmonths} \n Total Revenue: {netamount} \n Average Revenue Change: ({straight_average(net_change)}) \n Greatest Increase in Profits: {max(list_minmax)[1]}: {max(list_minmax)[0]} \n Greatest Decrease in Profits: {min(list_minmax)[1]}: {min(list_minmax)[0]}")

print(results)

# Export results to text file

saveResults = open('pyhomework.txt', 'w')
saveResults.write(results)
saveResults.close()
