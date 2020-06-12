import csv
from bisect import bisect
feedback = "{name} has worked {hours} hours and earned ${total}, of which ${tax} is deducted by tax, leaving ${income}."

def income(x):
    income = x * 36.75
    y = 0
    if x > 40: y += (x-40) * 18.375
    return (income + y)

# returns a value by calculating the worker's hours
# by the regular rate of 36.75, as well as addding
# any extra hours > 40 at half the rate, 18.375

def tax(x):
    bracket = [532, 668, 729, 794, 838]
    rate = [0.15, 0.2, 0.25, 0.3, 0.35]
    if x <= 532: return 0
    index = (bisect(bracket, x)) - 1
    amount = x - bracket[index]
    tax = amount * rate[index]
    while index > 0:
        amount = bracket[index] - bracket[index-1]
        tax += amount * rate[index-1]
        index -= 1
    return round(tax, 2)

# calculated how much a worker's income is taxed cumulatively,
# each value in a bracket is taxed for a certain amount and must
# be worked out procedurally, thus giving the total tax amount

def dataimport(x):
    output = []
    with open(x, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            x = income(int(row['Hours']))
            y = tax(income(int(row['Hours'])))
            output.append((
                row['Name'], 
                row['Hours'], 
                round(x, 2), 
                y, 
                round(x - y, 2)
                ))
        return output

# uses csv.dictreader to gather the name and hours of
# the workers and printing each of them in their
# repective rows, in a sentence-formatted string

# when not being used in menu GUI, use
# print(feedback.format(
    # name = row['Name'],
    # hours = row['Hours'],
    # total = round(x, 2),
    # tax = y,
    # income = round(x - y, 2)
    # ))

def userinput(x,y):
    n = str(x)
    h = int(y)
    i = income(h)
    t =  tax(i)
    with open ("temp.csv", "a", newline="") as csvfile:
        fieldnames = ["Name", "Hours"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writerow({"Name":n, "Hours":h})

# used if the user wants to input their own data, by
# asking for name an hours and using the defined
# functions to print it with the imported data

# data appended by the user is temporarily held in a
# separate file which is cleared upon exiting the program

# when not being used in menu GUI, use
# print(feedback.format(
        # name = n,
        # hours = h,
        # total = i,
        # tax = t,
        # income = i - t
        # ))

def clear():
    with open ("temp.csv", "w", newline="") as csvfile:
        fieldnames = ["Name", "Hours"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()

def main():
    while True:
        user = str(input("input data/show data/end program: "))
        if user == "input data":
            userinput(input("name: "),input("hours: "))
        elif user == "show data":
            dataimport("data.csv")
            print("\nrecent additions:\n")
            dataimport("temp.csv")
        else:
            clear()
            break
    return "exiting program..."

# the main function to distinguish between which
# function the user wants to perform, input their
# own data, show existing data or exit the program
