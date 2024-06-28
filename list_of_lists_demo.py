def main():

    list_of_lists = [[3, 7, 9],
                     [6, 9, 2],
                     [1, 5, 7]]
    print(list_of_lists[0][1])
    for row in range(len(list_of_lists)):
       for column in range(len(list_of_lists[row])):
        print(list_of_lists[row][column])

main()