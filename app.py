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

    std["Obtained"] = obtained_marks
    std["percentage"] = obtained_marks/total_marks*100
    std["Grade"] = grade(std["percentage"])
    std["Status"] = status(std["percentage"])
    with open("marks.txt","a") as file:
        file.write(f"\n{std}")
    return std 

def grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage>= 50:
     return "D"
    else:
        return "F"

def status(percentage):
    if percentage >= 50:
        return "Pass"
    else:
        return "fail"

def save():
    try:
        save_result = int(input("How many results you want to save: "))
        save_result += 1
        for i in range (1,save_result):
            print(i)
            add_marks()
    except:
       print("Enter a valid numaic number")

def view_all():
    with open("marks.txt","r") as data:
        result = data.read()
        print(result)


    