import os
import csv

#defining all array lits
dates = []
prof_loss = []
new_prof_loss = []
avr_chng = []

budget_data_path = os.path.join("Resources", "budget_data.csv")

with open(budget_data_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csv_reader:
        #converting years into array list
        dates.append(row[0])
        #converting profit and loss into array list
        prof_loss.append(row[1])
 
#Sum-up the profit and loss  
summ = 0
for element in prof_loss:
     summ = int(summ) + int(element)

#printing calculated total of months and profit/loss
print(f'Financial Analysis')
print(f'--------------------')
print(f'Total Months: {len(dates)}')
print("Total:  $ {}".format(summ))

#removing last value from profit/loss array list
prof_loss.pop()
#print(prof_loss)

#creating array list new_prof_loss without first profit/loss value of Jan-10
with open(budget_data_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    csv_header = next(csvfile)
    for row in csv_reader:
            new_prof_loss.append(row[1])

     
#print(new_prof_loss)

#creating a new array list of profit/loss change
avr_chng = [int(new_prof_loss) - int(prof_loss) for new_prof_loss, prof_loss in zip(new_prof_loss, prof_loss)]
#print(avr_chng)

#calculating the average of the profit/loss change and printing
summ_new = 0
for element_new in avr_chng:
     summ_new = int(summ_new) + int(element_new)

avr_chng_value = int(summ_new)/int(len(avr_chng))
avr_chng_value = round(avr_chng_value,2)
print("Average  Change: $ {}".format(avr_chng_value))

#inserting 0 as the first value in the average change array list
var = 0
avr_chng.insert(0,var)
#print(avr_chng)

#converting the average change(average change) and year(dates) into dictonary
dictionary = dict(zip(avr_chng,dates))
key1 = max(avr_chng)
key2 = min(avr_chng)
#print(dictionary)

#printing the greatest increase and decrease in profits
print(f'Greatest Increase in Profits: {dictionary[key1]} ($ {key1})')
print(f'Greatest Decrease in Profits: {dictionary[key2]} ($ {key2})')            


