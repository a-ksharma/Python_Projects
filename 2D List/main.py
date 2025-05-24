list1=[]

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def take_value(r,c):
    print("")
    for i in range(r):
        row=[]
        for j in range(c):
            e=get_int(f"Enter the elements for position:({i},{j}):")
            row.append(e)
        list1.append(row)

def traverse(r,c):
    print("\n\nTraversing the list")
    for a in range(r):
        print("[",end=" ")
        for b in range(c):
            print(list1[a][b],end=" ")
        print("]")

if __name__=='__main__':
    r=get_positive_int("Enter number of rows you want in list:")
    c=get_positive_int("Enter number of columns you want in list:")
    take_value(r,c)
    traverse(r,c)