import csv

STOCKS = {
"AAPL"	:   185.30,
"MSFT"  :	420.95,
"TSLA"  :	255.15,
"AMZN"  :	178.60,
"GOOGL" :	145.22,
"NVDA"  :	920.00
}

opt_out = True
stock_price = []
stock_list = []
sum = 0.0

print("Fetching stock prices...")
for stock in STOCKS:
    print(stock + " : " + str(STOCKS[stock]))

while opt_out:
    stock_input = input("Enter stock symbol: ").upper()
    if stock_input not in STOCKS:
        print("Invalid stock symbol.")
        continue
    stock_amount = float(input("Enter stock amount: "))
    if stock_input in STOCKS:
        price = STOCKS[stock_input] * stock_amount
        sum += price
        stock_price.append(price)
        stock_list.append(stock_input)
    opt = input("Would you like to add another stock? (y/n): ").lower()
    if opt == "y":
        opt_out = True
    else:
        opt_out = False

stock_dict = dict(zip(stock_list, stock_price))


with open("stock_list.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Symbol", "Price"])
    for s in stock_dict:
        writer.writerow([s, stock_dict[s]])
    writer.writerow(["Total sum = " , str(sum)])

try:
    with open("stock_list.csv", "r") as csvfile:
        data = csv.reader(csvfile)
        print("Your Stock List:")
        for row in data:
            print("{:<10} {:<10}".format(*row))
except FileNotFoundError:
    with open("stock_list.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Symbol", "Price"])
        for s in stock_dict:
            writer.writerow([s, stock_dict[s]])
        writer.writerow("Total sum = " + str(sum))







