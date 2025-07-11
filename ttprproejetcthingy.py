#PROJECT BY: "THE CODE CARTEL"
                                        #STORE:"PIPELINE TECH CO."

# Greet the user
print('Welcome to Pipeline Tech Co.!')
print('Here is what we have in stock:\n ')

# Define the product catalog with prices and quantities
#stock={'keyboard':[29.99,10],'mouse':[19.99,15],'monitor':[149.99,15]}
stock = {
    'keyboard': [29.99, 10],
    'mouse': [19.99, 15],
    'monitor': [149.99, 15],
    'laptop': [799.99, 5],
    'webcam': [59.99, 8],
    'usb cable': [9.99, 25],
    'headphones': [89.99, 12],
    'external hard drive': [129.99, 6],
    'gaming chair': [199.99, 3],
    'nutella': [4.99, 100]  # 🥄 Non-tech treat!
}

total_spent = 0  # Track total purchase cost

loop=True

while loop:
    print ('Product','Price','Stock')
    print ('-----------------------')
    for rec in stock.items():
        print(rec[0],rec[1][0], rec[1][1] )
   
      # Ask user what they want to buy
    if all(quantity <= 0 for money, quantity in stock.values()):
        print("The shop is completely out of stock!")
        loop = False
    else:
        item=input("What would you like to buy?")
        if item.strip().lower() in stock:
            print ('cool!')
            #Error Handling    
            # Handle quantity input and order validation
            quantity= input(f"How many {item}s do you want? ")
            while not quantity.isnumeric():
                quantity=input('Please enter a valid number.')
            quantity=int(quantity)
            if quantity <= 0:
                print("Quantity must be greater than 0.")
            elif quantity > stock[item][1]:
                print("Not enough quantity in stock")
                go = input("Do you want to continue shopping? (yes/no): ").strip().lower()
                if go == "no":
                    loop=False
            else:
                print("Successful")
        
                stock[item][1] -= quantity
                item_cost = stock[item][0]
                result = item_cost * quantity
                total_spent += result  # Add current transaction to total
                print(f"The total cost is ${round(result,2)}")
                print(f"Your current total cost is ${round(total_spent,2)}")
        
                go = input("Do you want to continue shopping? (yes/no): ").strip().lower()
                if go == "no":
                    loop=False    
        else:
            print('product not found')
            go = input("Do you want to continue shopping? (yes/no): ").strip().lower()
            if go == "no":
                        loop=False
    
if total_spent!=0:
    print("\nThank you for shopping at Pipeline Tech Co.!")
    print(f"Your total is: ${round(total_spent, 2)}")
    
    payment = input("Please select a form of payment (cash/card/crypto): ").strip().lower()
    print(f"Processing {payment} payment... ✅")
    print("Transaction complete. Have a great day!")
