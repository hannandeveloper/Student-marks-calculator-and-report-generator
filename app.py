std = {}
total_marks = 50

def add_marks():
    obtained_marks = 0
    std_name = input("Enter name: ")
    std["name"] = std_name
    for i in range(1,6):
       try:
            marks = int(input(f"Enter {i} subject marks : "))
            std[f"{i} sub"] = marks
            obtained_marks= obtained_marks + marks
       except ValueError:
            print("enter numaric values")
    std["percentage"] = obtained_marks/total_marks*100
    with open("marks.txt","a") as file:
        file.write(str(std))
    return std 

add_marks()
print(std)
    