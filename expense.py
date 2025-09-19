class Expense: #Define a class named Expense 

    #define the initialization method(__init__) whith three parameters:
    #name, category & amount

    def __init__(self, name, category, amount) -> None:
        self.name = name #Assign the value of the parameter name to the instance variable self.name
        self.category = category #Assign the value of the parameter category to the instance variable self.category
        self.amount = amount #Assign the value of the parameter amount to the instance variable self.amount


    def __str__(self) -> str: #Define the string representation method (__str__) for the Expense class
        return f"Expense(Name: {self.name}, Category: {self.category}, Amount: ${self.amount:.2f})"
        #Return a formatted string that includes the name, category, and amount of the expense