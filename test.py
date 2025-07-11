#PROJECT BY: "THE CODE CARTEL"
                                        #STORE:"PIPELINE TECH CO."
stock = {
    'keyboard': [29.99, 0],
    'mouse': [19.99, 0],
    'monitor': [149.99, 0],
    'laptop': [799.99, 0],
    'webcam': [59.99, 0],
    'usb cable': [9.99, 0],
    'headphones': [89.99, 0],
    'external hard drive': [129.99, 0],
    'gaming chair': [199.99, 0],
    'nutella': [4.99, 0]  # 🥄 Non-tech treat!
}
if all(quantity <= 0 for money, quantity in stock.values()):
    print("The shop is completely out of stock!")
else:
    pass
