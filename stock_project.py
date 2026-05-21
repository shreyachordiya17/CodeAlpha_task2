stocks = {
    "GOOGLE": 200,
    "AMZN": 150,
    "MSFT": 320,
    "NFLX": 400,
    "META": 290,
    "NVDA": 450,
    "IBM": 140,
    "ORCL": 130,
    "INTC": 120,
    "AMD": 170,
    "SAP": 160,
    "UBER": 75,
    "ADBE": 500,
    "PYPL": 95,
    "SHOP": 85,
    "SONY": 110,
    "DELL": 145,
    "HP": 90,
    "ASUS": 210,
    "LENOVO": 180,
    "TCS": 4200,
    "INFY": 1550,
    "WIPRO": 530,
    "HCL": 1250,
    "RELIANCE": 2900,
    "TATASTEEL": 170,
    "ITC": 450,
    "SBIN": 820
}

print("------ STOCK PORTFOLIO TRACKER ------")

print("\nAvailable Stocks:\n")

for stock in stocks:
    print(stock, ":", stocks[stock])

stock_name = input("\nEnter Stock Name: ").upper()

quantity = int(input("Enter Quantity: "))

if stock_name in stocks:

    stock_price = stocks[stock_name]

    total = stock_price * quantity

    print("\n------ INVESTMENT DETAILS ------")

    print("Stock Name :", stock_name)
    print("Price Per Share :", stock_price)
    print("Quantity :", quantity)
    print("Total Investment Value =", total)

else:
    print("\nStock not available")