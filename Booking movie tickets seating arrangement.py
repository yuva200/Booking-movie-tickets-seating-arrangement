am = {"A": {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
      "B": {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}}
pm = {"A": {1: 1, 2: 1, 3: 1, 4: 1, 5: 1},
      "B": {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}}


def disp(mve):
    print("\t1\t2\t3\t4\t5")
    for i,j in mve.items():
        print(i,end="\t")
        for m,n in j.items():
            print(n,end="\t")
        print()


while True:
    ch = int(input("Select 1)AM or 2)PM:: "))
    if ch == 1:
        # seat availablity
        flag = 0
        for i, j in am.items():
            for m, n in j.items():
                if n == 0:
                    print("Seat are available: ")
                    flag = 1
                    break
        if flag == 1:
            print("Seating Arragement: ")
            disp(am)
            row = input("Select Row:: ")
            col = int(input("Select Col:: "))
            if am[row][col] == 0:
                am[row][col] = 1
                if row == "A":
                    print("Total:: 200/-")
                elif row == "B":
                    print("Total:: 150/-")
            else:
                print("Selected Seats Are not available")
        elif flag == 0:
            print("Seating Completed")

    elif ch == 2:
        flag = 0
        for i, j in pm.items():
            for m, n in j.items():
                if n == 0:
                    print("Seat are available: ")
                    flag = 1
                    break
        if flag == 1:
            print("Seating Arragement: ")
            disp(pm)
            row = input("Select Row:: ")
            col = int(input("Select Col:: "))
            if pm[row][col] == 0:
                pm[row][col] = 1
                if row == "A":
                    print("Total:: 200/-")
                elif row == "B":
                    print("Total:: 150/-")
            else:
                print("Selected Seats Are not available")
        elif flag == 0:
            print("Seating Completed")
    else:
        print("No Show Available")