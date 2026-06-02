# Expense Traker Project

expenseList= []# list of expenses in form of dictionary
print("Welcome to Expense Traker : Kharcha Kam Kia Karo")

while True:
    print("===MENU===")
    print("1.Add Expense")
    print("2.View All Expense")
    print("3.View Total Kharch")
    print("4.Exit")

    choise = int(input("Please Enter Your Choise :"))

#Add Expense

    if choise == 1:
        date= input("kis date par kharch kiya tha?:")
        categary= input("kis type ka kharcha kiya?(Food,Travel,Books): ")
        discription= input("Aur detail deto:")
        amount= float(input("Enter the amount:"))

        expense= {
            "date": date,
            "categary": categary,
            "discription": discription,
            "amount": amount
        }

        expenseList.append(expense)

        print("\n DONE Bro. Expense is added succesfully")

# VIEW ALL EXPENSES

    elif choise == 2:
        if( len(expenseList)==0):
            print("No Expense Added. Jao pahle kharch karo.")
        else:
            print("==== Ye y apka sara expense ====")
            count=1
            for eachkharch in expenseList:
                print(f"Kharcha Number {count} -> {eachkharch["date"]}, {eachkharch["categary"]}, {eachkharch["discription"]}, {eachkharch["amount"]} ")
                count= count+1

# VIEW TOTAL SPENDING

    elif choise == 3:
        total=0
        for eachkharch in expenseList:
            total = total + eachkharch["amount"]
        
        print("\nTOTAL KHARCH =",total)

# EXIT
    
    elif choise == 4:
        print("Dhanyawad aapne system use kiya ")
        break

    else:
        print("INVALID CHOISE")
