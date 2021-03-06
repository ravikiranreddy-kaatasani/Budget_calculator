print("expense calculator: ")
while(True): #When ever the user enter the wrong input (anything except numbers).it will repeat the loop .
    try:
        salary=float(input("enter your salary: "))
        if salary < 0:
             print("Enter only positive numbers")
             continue
        break
    except ValueError: #throw exception if salary input is not number.
        print("The salary should be a number")
        print("try again")
total_expense=0 #init base expense = 0
expend_inventory=dict() 
balance=salary #init balance is equal to salary
while(True):
    try:                
        expenditure_name=input("Enter yor expense name : ") 
        expenditure_name = expenditure_name.strip().lower() #remove spaces and change it to lower to ensure expenditure_names are unique
        if expenditure_name.isdigit():
            print("expenditure name allows only strings")
            continue
        if expenditure_name == 'q': #exit the loop when q is entered
            break
        expenditure_amount=float(input("Enter the amount for "+ expenditure_name +" :")) 
        if expenditure_amount<0:
            print("expenditure_amount allows positive numbers")
            continue
    
    except ValueError: 
    
        print("the expenditure_amount should be a number")    
        print("try again")     
        
    if(expenditure_amount <= balance): #check min balance is available or not
        balance =balance-expenditure_amount #update balance
        if expenditure_name not in expend_inventory.keys(): #check if key is repeated
            expend_inventory[expenditure_name]=expenditure_amount
        else: 
            temp=expend_inventory[expenditure_name] 
            expend_inventory[expenditure_name]=temp+expenditure_amount
    else:
        print(" Insufficientfunds")
        break
total_expense = sum(expend_inventory.values()) #expense

                
print(expend_inventory)                
print("salary".ljust(35)," : ",salary) 
print("-"*37,'-'*(len(str(salary))+3))
for name, amount in expend_inventory.items():  
    print(name.ljust(35)," : ",str(amount).rjust(len(str(salary))))
print("-"*37,'-'*(len(str(salary))+3))     
print("total expend_inventory is".ljust(35)," : ",str(total_expense).rjust(len(str(salary))))    
print("balance".ljust(35)," : ",str(balance).rjust(len(str(salary))))
