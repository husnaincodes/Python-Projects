student_grades = { }
def add_student(name ,grade):
    student_grades[name]= grade
    print(f"Added {name} with a {grade} marks")



def update_student(name , grade):
        if name in student_grades:
            student_grades[name]= grade
            print(f"{name} with marks are updated {grade}")
        else:
             print(f"{name} is not found !!")



def delete_student(name):
    if name in student_grades:
     del student_grades[name]
     print(f"{name}  has been successfully deleted")
    else:
        print(f"{name} is not found !!")




def display_all_student():
    if student_grades:
        for name , grade in student_grades.items():
            print(f"{name} | {grade}")
    else:
        print("Student not found!!")



def main():
    while True:
        print("\n Student Grade Management System ")
        print("1. Add student ")
        print("2. Update student ")
        print("3. Delete student ")
        print("4. View  students ")
        print("5. Exit")
        
        choice  = int(input("Enter your choice : "))
        if choice == 1 :
            name  = input("Enter a student name :")
            grade = int(input("Enter a student grade/marks: "))
            add_student(name,grade)
        elif choice==2:
            name  = input("Enter a student name :")
            grade = int(input("Enter a student grade/marks: "))
            update_student(name,grade)
        elif choice==3:
            name  = input("Enter a student name :")
            delete_student(name)
        elif choice==4:
            display_all_student()
        elif choice == 5:
            print("closing the program......")
            break
        else:
            print("Invalid choice!!")
if __name__ == "__main__":
    main()