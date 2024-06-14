def main():
    a = 7
    b = 7
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    else:
        print(f"{a} is equal to {b}")

    #print the appropriate letter grade based on the test score
    #A: 100-90, B: 89-80. C: 79-70, D: 69-60, F: 59 or lower
    print("\nGrade Decision: 1")
    test_score = 79.3
    if ((test_score <= 100) and (test_score >= 90)):
        print(f"{test_score} --> A")
    elif ((test_score <= 90) and (test_score >= 80)):
        print(f"{test_score} --> B")
    elif ((test_score <= 80) and (test_score >= 70)):
        print(f"{test_score} --> C")
    elif ((test_score <= 70) and (test_score >= 60)):
        print(f"{test_score} --> D")
    else:
        print(f"{test_score} --> F")

    #grade decision statement restructured
    print("\nGrade Decision: 2")
    if ((test_score <= 100) and (test_score >= 90)):
        print(f"{test_score} --> A")
    elif (test_score >= 80):
        print(f"{test_score} --> B")
    elif (test_score >= 70):
        print(f"{test_score} --> C")
    elif (test_score >= 60):
        print(f"{test_score} --> D")
    else:
        print(f"{test_score} --> F")

 
            
main()