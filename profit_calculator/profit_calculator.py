import matplotlib.pyplot as plt

points_per_day = 5 # how many points you make per day
point_value = 50 # value of 1 point = 50 for ES futures
num_trading_days = 15 # how many days of the month do you trade
balance = 15000 # number of your starting balance
balance_for_one_contract = 14000 # how much you need to trade one contract. different brokers have different values

num_months_to_forecast = 12 # forecast profit

balance_list = []
used_contracts_list = []
print("starting balance:", balance)
starting_balance = balance

for i in range(num_months_to_forecast):
    for _ in range(num_trading_days):
        num_contracts = int(balance / balance_for_one_contract)
        balance += points_per_day * point_value * num_contracts
        used_contracts_list.append(num_contracts)
        balance_list.append(balance)
    print("Month", str(i+1)+":", balance)
    
print("If you do", points_per_day, "points on", num_trading_days, "days of every month, with a point value of", point_value,", you will have", balance, "after", num_months_to_forecast, "months!")
print("If you need a balance of", balance_for_one_contract,"for every contract, your new balance will allow you to trade with", used_contracts_list[-1], "contracts!")
plt.title("num contracts used")
plt.plot(used_contracts_list)
plt.show()
plt.title("balance")
plt.plot(balance_list)
plt.show()