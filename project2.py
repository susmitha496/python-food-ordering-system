
restarunt=['Divya Pot Biryani','Kondareddy Biryani','Tadipatri Dhum Biryani']
items=[['chicken biryani','mutton pot biryani','chicken pot biryani'],['chicken biryani','paneer biryani','mushroom biryani','Nallibokka biryani'],
       ['biryani','egg biryani','fry piece biryani']]
prices=[[300,550,450],[300,289,299,500],[350,250,380]]
quantities=[[30,25,30],[30,20,15,10],[25,20,28]]
ordercount=0
running=True
while running:
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    choose=input("Enter your option: ")
    if choose=="1":
        print("========== ADMIN MODULE ==========")
        password=input("Enter admin password: ")
        if password=="abc@123":
            print("Login successful")
            admin_running=True
            while admin_running:
                print("1. View Restaurants")
                print("2. View Menu")
                print("3. Add Food Item")
                print("4. Update Food Price")
                print("5. Remove Food Item")
                print("6. Update Food Quantity")
                print("7. Add Restaurant")
                print("8. Remove Restaurant")
                print("9. View Completed Orders")
                print("10. Exit")
                option=input("Enter your choice: ")
                if option=="1":
                    print("="*20,"Restaurants","="*20)
                    print("Available Restaurants")
                    for i in range(len(restarunt)):
                        print(f"{i+1}. {restarunt[i]}")
                elif option=="2":
                    print("="*20,"Restaurants","="*20)
                    print("Available Restaurants")
                    for i in range(len(restarunt)):
                        print(f"{i+1}. {restarunt[i]}")
                    choice=int(input("Enter restaurant number: "))
                    if choice>=1 and choice<=len(restarunt):
                        index=choice-1
                        print("="*20,"MENU","="*20)
                        print(f"{'Food Item':<30}{'Price':>10}{'Qty':>8}")
                        for i in range(len(items[index])):
                            print(f"{i+1}. {items[index][i]:<27}{prices[index][i]:>10}{quantities[index][i]:>8}")
                    else:
                        print("Invalid restaurant number")
                elif option=="3":
                    print("Available Restaurants")
                    for i in range(len(restarunt)):
                        print(f"{i+1}. {restarunt[i]}")
                    choice=int(input("Enter restaurant number: "))
                    if choice>=1 and choice<=len(restarunt):
                        index=choice-1
                        item=input("Enter food item: ")
                        if item in items[index]:
                            print("Food item already exists")
                        else:
                            price=int(input("Enter price: "))
                            quantity=int(input("Enter quantity: "))
                            items[index].append(item)
                            prices[index].append(price)
                            quantities[index].append(quantity)
                            print("Food item added successfully")
                    else:
                        print("Invalid restaurant number")
                elif option=="4":
                    print("Available Restaurants")
                    for i in range(len(restarunt)):
                        print(f"{i+1}. {restarunt[i]}")
                    choice=int(input("Enter restaurant number: "))
                    if choice>=1 and choice<=len(restarunt):
                        index=choice-1
                        item=input("Enter food item: ")
                        found=False
                        for i in range(len(items[index])):
                            if items[index][i]==item:
                                price=int(input("Enter new price: "))
                                prices[index][i]=price
                                found=True
                                print("Food price updated successfully")
                                break
                        if not found:
                            print("Food item not available")
                    else:
                        print("Invalid restaurant number")
                elif option=="5":
                    print("Available Restaurants")
                    for i in range(len(restarunt)):
                        print(f"{i+1}. {restarunt[i]}")
                    choice=int(input("Enter restaurant number: "))
                    if choice>=1 and choice<=len(restarunt):
                        index=choice-1
                        item=input("Enter food item to remove: ")
                        if item in items[index]:
                            foodindex=items[index].index(item)
                            items[index].pop(foodindex)
                            prices[index].pop(foodindex)
                            quantities[index].pop(foodindex)
                            print("Food item removed")
                        else:
                            print("Food item not available")
                    else:
                        print("Invalid restaurant number")
                elif option=="6":
                    print("Available Restaurants")
                    for i in range(len(restarunt)):
                        print(f"{i+1}. {restarunt[i]}")
                    choice=int(input("Enter restaurant number: "))
                    if choice>=1 and choice<=len(restarunt):
                        index=choice-1
                        item=input("Enter food item: ")
                        found=False
                        for i in range(len(items[index])):
                            if items[index][i]==item:
                                quantity=int(input("Enter new quantity: "))
                                quantities[index][i]=quantity
                                found=True
                                print("Food quantity updated successfully")
                                break
                        if not found:
                            print("Food item not available")
                    else:
                        print("Invalid restaurant number")
                elif option=="7":
                    newrestaurant=input("Enter restaurant name: ")
                    if newrestaurant in restarunt:
                        print("Restaurant already exists")
                    else:
                        restarunt.append(newrestaurant)
                        items.append([])
                        prices.append([])
                        quantities.append([])
                        print("Restaurant added successfully")
                elif option=="8":
                    print("Available Restaurants")
                    for i in range(len(restarunt)):
                        print(f"{i+1}. {restarunt[i]}")
                    choice=int(input("Enter restaurant number: "))
                    if choice>=1 and choice<=len(restarunt):
                        index=choice-1
                        removed=restarunt.pop(index)
                        items.pop(index)
                        prices.pop(index)
                        quantities.pop(index)
                        print(removed,"removed successfully")
                    else:
                        print("Invalid restaurant number")
                elif option=="9":
                    print("="*40)
                    print("Complted orders:",ordercount)
                    print("="*40)
                elif option=="10":
                    print("Admin module completed")
                    admin_running=False
                else:
                    print("Invalid choice")
        else:
            print("Invalid password")
    elif choose=="2":
        print("========== USER MODULE ==========")
        user_running=True
        while user_running:
            print("Available Restaurants")
            for i in range(len(restarunt)):
                print(f"{i+1}. {restarunt[i]}")
            choice=int(input("Enter restaurant number: "))
            if choice<1 or choice>len(restarunt):
                print("Invalid restaurant number")
                continue
            index=choice-1
            additems=[]
            addprice=[]
            addquantity=[]
            if len(items[index])==0:
                print("No food items available")
                continue
            print("="*20,"MENU","="*20)
            print(f"{'Food Item':<30}{'Price':>10}{'Qty':>8}")
            for i in range(len(items[index])):
                print(f"{i+1}. {items[index][i]:<27}{prices[index][i]:>10}{quantities[index][i]:>8}")
            while True:
                item=int(input("Enter food item: "))
                if item>=1 and item<=len(items[index]):
                    foodindex=item-1
                    print("Item is available")
                    print("Price:",prices[index][foodindex])
                    print("Available:",quantities[index][foodindex])
                    quantity=int(input("How many parcels do you want: "))
                    if quantity>0 and quantity<=quantities[index][foodindex]:
                        additems.append(items[index][foodindex])
                        addprice.append(prices[index][foodindex])
                        addquantity.append(quantity)
                        amount=prices[index][foodindex]*quantity
                        quantities[index][foodindex]-=quantity
                        print("Added to cart")
                        print("Amount:",amount)
                    else:
                        print("Only",quantities[index][foodindex],"parcels are available")
                else:
                    print("Food item not available")
                another=input("Do you want another item? yes/no: ")
                if another.lower()=="no":
                    break
            if len(additems)>0:
                print("="*60)
                print(f"{'Item':<30}{'Price':>10}{'Qty':>8}{'Amount':>12}")
                print("-"*60)
                totalbill=0
                for i in range(len(additems)):
                    amount=addprice[i]*addquantity[i]
                    totalbill+=amount
                    print(f"{additems[i]:<30}{addprice[i]:>10}{addquantity[i]:>8}{amount:>12}")
                print("-"*60)
                print(f"{'Total Bill':<48}{totalbill:>12}")
                print("="*60)
                order=input("Do you want to place the order? yes/no: ")
                if order.lower()=="yes":
                    print("Order placed successfully!")
                    ordercount+=1
                    payment=input("Enter payment UPI/Cash: ")
                    if payment.lower()=="upi":
                        print("Payment successful")
                    elif payment.lower()=="cash":
                        print("Cash on delivery")
                    else:
                        print("Invalid payment")
                else:
                    print("Order cancelled")
            anotherrestarunt=input("Do you want order from another restaurnt(yes/no): ")
            if anotherrestarunt.lower()=="yes":
                continue
            elif anotherrestarunt.lower()=="no":
                break
    elif choose=="3":
        print("Thank you for using Food Ordering Management System")
        running=False
    else:
        print("Invalid option")
