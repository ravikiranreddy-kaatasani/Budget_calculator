print("expense calculator: ")
while(True): #When ever the user enter the wrong input (anything except numbers).it will repeat the loop .
    try:
        salary=float(input("enter your salary: "))
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
        if expenditure_name == 'q': #exit the loop when q is entered
            break
        expenditure_amount=float(input("Enter the amount for "+ expenditure_name +" :")) 
    
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
total_expense = salary-balance #expense

                
print(expend_inventory)                
print("salary                               : ",salary) 
print("---------------------------------")
for key, value in expend_inventory.items():  
    print("{0}                              : {1} ".format(key,value))
print("------------------------------------")    
print("total expend_inventory is            :",total_expense)    
print("balance                              :",balance )    
