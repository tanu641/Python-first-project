menu = {
    'pizza':100,
    'Pasta': 80,
    'Burger':80,
    'Salad':70,
    'Coffee':120
}
#Greet
print("welcome to my Restorent")
print("pizza: Rs100\nPasta: Rs80\nBurger: Rs80\nSalad: Rs70\nCoffee: Rs120")


order_total = 0
#100 + 80 = 180


item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0+50
    print(f"Your item {item_1} has been added to your order ")
else:
    print(f"Ordered item{item_1 } is not available yet")   


another_order = input("Do you want to add another item ? (Yes/No)")
if another_order == "yes":
    item_2 = input ("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print (" Item {item_2} has been added to order")
    else:
        print(f"Orderd item{item_2} is not available!")    

    print(f"The total amount of items to pay is {order_total}")     


