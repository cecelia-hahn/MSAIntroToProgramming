#Write a program to convert pounds to kilograms
#Write a function to get a positive number from the user
def get_positive_float_input():
  #ask a user for their weight in pounds and validate correct input
  #if bad input, reprompt user
  user_weight = 0
  #bad_input = True
  while(True):
    try:
      user_weight = float(input("Enter your weight in pounds:"))
      #check if user_weight > 0. If not, reprompt the user
      if user_weight <= 0:
        print("ERROR: Please enter a weight greater than 0")
        continue
      else:
        break
    except:
      print("ERROR: Please enter a number greater than 0")
  return user_weight
#INPUT
#Get weight from user
user_weight = get_positive_float_input()
 

#PROCESSING
#Use a conversion to convert pounds to kilograms: 2.205lbs = 1kg
lbs_to_kg_conversion = 2.205
user_weight_in_kg = user_weight / lbs_to_kg_conversion

#OUTPUT
#Print output to the user
#You weigh XXXX kg
print(f"You weigh {user_weight_in_kg:.2f}kgs.")