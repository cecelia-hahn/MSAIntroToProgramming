#Write a program to calculate the user's wage from an input of hours worked daily and hourly wage
#Ask the user to input from the keyboard for two inputs, one is the hours worked daily and the other is the hourly wage. Multiplying hours worked daily and hourly wage will give you the wages earned in a day.
#The two input numbers are not necessarily integers. For example, the user can enter values like 35.5 for hours worked or 17.85 for hourly wage.
#Calculate the yearly wage given the two inputs
#Note that the working hours is daily. Assume the user works 350 days per year and the same amount of hours every day.
#It would help to first write down the mathematical formula needed to calculate the yearly wage
#12% will be deducted from yearly earnings for taxes
#Print the a Pay Advice containing:
#hours worked
#hourly wage
#wages before taxes
#tax amount
#annual wages after taxes
#money values should be printed with a $ sign and all numbers should be rounded to 2 decimal places

#INPUT
def get_hours_worked_daily():
    #ask user for hours worked daily and validate input. prompt user again if input is bad
    hours_worked = 0
    while(True):
        try: 
            hours_worked = float(input("Enter your hours worked per day: "))
        #check if hours is <= 0 and >= 24
            if hours_worked <= 0 or hours_worked >= 24:
                print("ERROR: Please enter a number greater than 0 and less than 24")
                continue
            else:
                break
        #check if value is not numerical
        except:
            print("ERROR: Please enter a number greater than 0")
    return hours_worked
hours_worked = get_hours_worked_daily()

def get_hourly_wage():
    hourly_wage = 0
    while(True):
        try:
            hourly_wage = float(input("Enter your hourly wage: "))
        #check if wage is <= 0
            if hourly_wage <= 0:
                print("ERROR: Please enter a number greater than 0")
                continue
            else:
                break
        #check if value is not numerical
        except:
            print("ERROR: Please enter a number greater than 0")
    return hourly_wage
hourly_wage = get_hourly_wage()

#PROCESSING
#find daily wage
daily_wage = hourly_wage * hours_worked
#find yearly wage
yearly_wage = daily_wage * 350
#find how much tax is applied
tax_amount = yearly_wage * 0.12
#calculate wages after tax
wages_after_tax = yearly_wage - tax_amount

#OUTPUT
print(f"Pay Advice\n------------- \nHours Worked: {hours_worked: .2f}\nHourly Wage: {hourly_wage: .2f}\nWages Before Taxes: {yearly_wage: .2f}\nTax Amount: {tax_amount: .2f}\nAnnual Wage After Taxes: {wages_after_tax: .2f}")
