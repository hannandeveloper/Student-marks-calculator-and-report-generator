std = {}

def add_marks():
    std_name = input("Enter name: ")
    std["name"] = std_name
    # for i in range(1,6):
    #    try:
    #         marks = int(input(f"Enter {i} subject marks : "))
    #    except ValueError:
    #         print("enter numaric values")
    return std

add_marks()
print(std)
    