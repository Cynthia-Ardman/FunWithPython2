shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


# Write your code below!
def compute_bill(food):
    total = 0

    for key in food:
        if stock[key] > 0:
            total += prices[key]
            stock[key] -= 1
            print("the stock for %s is now " + str(stock[key])) % key
    else:
        print("%s is out of stock") % key

    print("The total is " + str(total))


bill_do = (compute_bill(shopping_list))
bill_do