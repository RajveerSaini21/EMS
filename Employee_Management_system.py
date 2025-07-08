employee_data = {
    101 : {'name': 'Rajveer' , 'age' : 20 , 'department' : "Software Engineer" , 'salary' : 500000},
    102 : {'name': 'Esha' , 'age' : 20 , 'department' : 'HR' , 'salary' : 600000}
}

def add_employee():
    try:
        emp_id = int(input("Enter Employee ID : "))
        if(emp_id in employee_data):
            print("Employee ID already exists. Please enter new Employee ID")
            return 

        name = input("Enter Employee Name : ")
        age = int(input("Enter Employee Age : "))
        department = input("Enter Employee Department")
        salary = float(input("Enter Employee Salary : "))

        employee_data[emp_id] = {
            'name' : name , 
            'age' : age ,
            'department' : department , 
            'salary' : salary
        }

        print("Employee added successfully") ;
        
    except ValueError :
        print("Invalid Input")

def view_employee():
    if not employee_data :
        print("No employees available\n")
        return 

    print("{:<10} {:<15} {:<5} {:<20} {:<10}".format('Emp_ID', 'Name', 'Age', 'Department', 'Salary'))
    print()
    for emp_id, info in employee_data.items():
        print("{:<10} {:<15} {:<5} {:<20} {:<10}".format(emp_id, info['name'], info['age'], info['department'], info['salary']))
    print() 
        
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID : "))
        if emp_id in employee_data:
            emp = employee_data[emp_id]
            print(f"\nEmployee Found:\nName: {emp['name']}\nAge: {emp['age']}\nDepartment: {emp['department']}\nSalary: {emp['salary']}\n")
        else:
            print("Employee Not Found")
    except:
        print("Invalid Employee ID")
            

def main_menu():
    while True:
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice : ")

        if(choice == '1'):
            add_employee()
        elif(choice == '2'):
            view_employee() 
        elif(choice == '3'):
            search_employee()
        elif(choice == '4'):
            print("Thank You for usign Employee Management System") 
            break 
        else:
            print("Invalid choice")

if __name__ == "__main__": 
    main_menu() 