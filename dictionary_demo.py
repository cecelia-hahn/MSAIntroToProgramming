def main():
    scores = [1, 4, 6, 7, 78]
    student_names = ["Alice", "Bob", "Jerry", "Jane", "Bill"]
    for index in range(len(scores)):
        print(f"{student_names[index]}: {scores[index]}")

    #create a dictionary of names and scores
    student_scores = {
        "Alice": 87,
        "Bob": 79,
        "Jerry": 94,
        "Sarah": 90
    }
    #print bob and sarah's scores
    print("\n")
    print(student_scores["Bob"])
    print(student_scores["Sarah"])

    #get all the keys and values from the student score dictionary
    print("\n")
    for student in student_scores:
        print(f"{student}: {student_scores[student]}")

    #declare a car dictionary
    car = {"Make": "Ferarri", "Model": "F-50", "Year": 2021, "Value": 500000, "Engine": 4.8}
    #get all the keys and values from the car dictionary
    print("\n")
    for key, value in car.items():
        print(f"{key}: {value}")


main()