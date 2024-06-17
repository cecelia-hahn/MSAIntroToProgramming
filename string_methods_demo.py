def main():
    #capitalize a string
    my_name = "cecelia"
    print(my_name.capitalize())

    #make a string uppercase
    print(my_name.upper())

    #make a string lowercase
    last_name = "HAHN"
    print(f"{my_name.capitalize()} {last_name.lower()}")

    #determine if a string starts with a set of characters
    print(my_name.startswith("c"))

    if(not my_name.startswith("cece") and not my_name.startswith("Cece")):
        print(f"You spelled {my_name} incorrectly")
    else:
        print(f"You spelled {my_name} correctly")

    #determine if a string ends with a set of characters
    print(my_name.endswith("lia"))

    #find a set of characters in a string
    #finds first one in the string unless index specified second; first letter is 0
    print(my_name.find("e", 2))

    #loop through a string
    for letter in my_name:
        print(letter)

    print(f"{my_name} has {len(my_name)} letters")

    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index}: {my_name[letter_index]}")

    print("\n\n")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    #write code that counts the # of "dog" occurences in sentence
    #expected output: 3
    #use a while loop
    
    number_of_dogs = 0
    dog_index = 0
    while True:
        dog_index = sentence.find("dog", dog_index)
        if dog_index == -1:
            break
        else:
            number_of_dogs += 1
            dog_index += 1
    print(f"Number of dogs: {number_of_dogs}")
    
    #how to use the split method
    car_info = "Ferrari, F-50, 2021, 500000, 4.8"
    car_data = car_info.split(",")
    print(car_data)

main()