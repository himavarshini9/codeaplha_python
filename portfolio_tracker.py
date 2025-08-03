# Stock Portfolio Tracker - Internship Task

# Hardcoded stock prices (USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 145,
    "MSFT": 310
}

# Dictionary to store user's portfolio
portfolio = {}

print("📊 Welcome to the Stock Portfolio Tracker!")
print("Available stocks: ", ', '.join(stock_prices.keys()))

# Input from user
while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("⚠️ Stock not found. Please enter a valid symbol.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❗ Please enter a valid number.")

# Calculate total investment
total_investment = 0
print("\n📋 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} shares × ${price} = ${investment}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Optional: Save to a text file
save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_summary.txt", "w") as file:
        file.write("📋 Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            file.write(f"{stock}: {qty} shares × ${price} = ${investment}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}")
    print("✅ Summary saved to 'portfolio_summary.txt'")
