print("expense calculator: ")
while(True):
    try:
        salary=float(input("enter your salary: "))
        break
    except ValueError:
        print("The salary should be a number")
        print("try again")
total_expense=0
expend_inventory=dict()
balance=salary
while(True):
    try:                
        expenditure_name=input("Enter yor expense name: ")
        expenditure_name = expenditure_name.strip().lower()
        if expenditure_name == 'q':
            break
        expenditure_amount=float(input("Enter the amount for "+ expenditure_name +" :")) 
    
    except ValueError: 
    
        print("the expenditure_amount should be a number")    
        print("try again")     
    if(expenditure_amount <= balance):
        balance =balance-expenditure_amount
        if expenditure_name not in expend_inventory.keys(): 
            expend_inventory[expenditure_name]=expenditure_amount
        else: 
            temp=expend_inventory[expenditure_name]
            expend_inventory[expenditure_name]=temp+expenditure_amount
    else:
        print(" Insufficientfunds")
total_expense = salary-balance

                
print(expend_inventory)                
print("salary                               : ",salary) 
print("---------------------------------")
for key, value in expend_inventory.items():  
    print("{0}                              : {1} ".format(key,value))
print("------------------------------------")    
print("total expend_inventory is            :",total_expense)    
print("balance                              :",balance )    
