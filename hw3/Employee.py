# create a class for employee
class Employee():

    # initialize the attributes included in employee
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # create a function that will increase salary by a percent determined by user
    def salary_increase(self):
        self.salary = self.salary * percent

    # print out the person's new salary in a statement
    def __str__(self):
        return f"{self.name}'s new salary is {self.salary}."

# ask for user input to determine by what percent to increase salary
percent = int(input("How much do you want to increase salary? (Ex. enter as 10 for 10%)"))

# convert percent to number to then be used to multiply by the salary
percent = (percent / 100) + 1

# determine attributes in the class to create object
employee1 = Employee("John", 5000)

# call the salary_ increase function
employee1.salary_increase()

# print out the statement created
print(employee1)



#------ AI session link ------#
# https://chatgpt.com/share/6aa45b7d-95ec-83e8-9da4-4cd34aa577ab