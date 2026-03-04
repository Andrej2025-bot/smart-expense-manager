expenses = []

while True:
    print("\n-------===MENU===-------")                                                             
    print("1 - ADD expense")
    print("2 - Show all expenses")
    print("3 - Statistics")
    print("4 - Delete expense by index")
    print("5 - Exit")
            
    try:
        choice = input("Select an option (1 - 5):").strip()
        choice = int(choice)
        
        if choice < 1 or choice > 5:
            print("Enter numbers from 1 - 5 ")
            continue
    
    except ValueError:
        print("Enter number")
        continue

    if choice == 1:
        print("______ADD Expense______")
        
        while True:
            name = input("Expense name:").strip().title()
            
            if name == "":
                print("The name cannot be empty")
                continue
            
            cleaned = name.replace(" ","").replace("-","").replace("_","")                 
            
            if not cleaned.isalpha():
                print("The name must contain only letters, no numbers")
                continue
            
            while True:
                    amount = input("Enter amount:").strip()                 
                    
                    if amount == "":
                        print("You did not enter the amount of the expense")
                        continue
                    
                    clean_amount = amount.replace(" ","")
                    
                    if not clean_amount.isdigit():
                        print("You must enter a number")
                        continue
                    
                    amount = int(clean_amount)
                    
                    if amount <= 0:
                        print("The expense cannot be less than or equal to 0")
                        continue
                    break
            
            while True:
                category = input("Enter the expense category (Food,Car,Home...)").strip().title()           
                
                if category == "":
                    print("You did not enter a category")
                    continue
                
                clean_category = category.replace(" ","").replace("-","").replace("_","")
                
                if not clean_category.isalpha():
                    print("You must enter letters, not numbers.")
                    continue
                break
            
            if name != "" and category!= "": 
                
                expense = {
                    "name":name,
                    "amount":amount,
                    "category":category
                }
                
                expenses.append(expense)
                print("Done! The expense has been saved to the list")
                
                while True:
                    continue_choice = input("Do you have any more expenses ? (yes or no)").strip().lower()
                    
                    if continue_choice == "":
                        print("You haven't entered anything, do you want to continue yes or no") 
                        continue
                    
                    if continue_choice not in ("yes","no"):                
                        print("You must enter only yes or no")
                        continue
                    break
                
                if continue_choice == "no":
                    break
   
    elif choice == 2:
        print("______Display expenses______")                                            
        
        if not expenses:
            print("You have no expenses (The list is empty)")
        else:                                                                                             
            for index, item in enumerate(expenses):
                print(f"{index:<3} - {item['name']:<10} | {item['amount']:<5}€ | {item['category']}")
        continue
    
    elif choice == 3:
        print("______Statistics______")
        
        if not expenses:
            print("The list is empty")
        else:
            total_amount = 0
            
            for item in expenses:
                total_amount += item["amount"]
            print("Your total expenses :", total_amount ,"€")
            print("The number of your expenses is:", len(expenses)) 

            smallest_amount = expenses[0]["amount"]
            largest_amount = expenses[0]["amount"]

            for expense in expenses:
                
                if expense["amount"] < smallest_amount:
                    smallest_amount = expense["amount"]
                
                if expense["amount"] > largest_amount:
                    largest_amount = expense["amount"]

            print("The smallest expense is:", smallest_amount)
            print("The largest expense is:",largest_amount)
    
    elif choice == 4:
        print("______Delete expense______")
        
        while True:
            try:
                index_input = input("Which expense do you want to remove? Enter a number :").strip()
                
                if not index_input:
                    print("You must enter a number")
                    continue
                
                if not index_input.isdigit():
                    print("Must contain only numbers")                                          
                    continue

                while True:
                    you_sure = input("Are you sure ? (Yes/No)").strip().title()

                    if you_sure == "":
                        print("You have not entered anything, enter Yes or No")
                        continue

                    if you_sure not in("Yes","No"):
                        print("You must enter only Yes or No")
                        continue
                    break

                if you_sure == "No":
                    print("Cancelled")
                    break
                
                index = int(index_input)
                
                expenses.pop(index)
                print("Expense deleted")
                break
            
            except IndexError:
                print("Index does not exist")
    
    else: 
        print("End of application. Goodbye.")
        break       