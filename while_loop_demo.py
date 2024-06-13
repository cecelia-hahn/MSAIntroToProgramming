def main():

    #create a while loop that prints integers between 0 and 10
    output_value = 0
    stop_value = 10
    #run the loop while output value is less than or equal to the stop value
    while output_value <= stop_value:
        print(output_value)
        #increment output value
        ##less efficient way:
        #output_value = output_value + 1
        ##more efficient:
        output_value += 1

    print("\n\n")
    output_value = 0
    #same thing but with infinite loop
    while True:
        print(output_value)
        output_value += 1

        #if output value is greater than stop value, break the loop
        if (output_value > stop_value):
            break

main()