#Starting Variables
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0

#Find Total Price of all Haircuts
for i in prices:
  total_price += i
print("Total Price for All Haircuts:", total_price)

#Fine average price of haircuts
average_price = total_price / len(prices)
print("Average Price:", average_price)
print("Number of haricuts:", len(hairstyles))

#Reduce all prices by $5
new_prices = [i-5 for i in prices]
new_prices.sort()
print("New Prices:", new_prices)

#Find Total Revenue for the week
total_revenue = 0

#Loop through hairstyles creating a list with range same as hairstyles length [0,8]
#print(range(len(hairstyles)))
for i in range(len(hairstyles)):
#Multiply price by # of haircuts for each index [0,8]
  total_revenue += prices[i] * last_week[i]
print("Total Revenue Last Week:", total_revenue)

#Find Average daily revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue:", average_daily_revenue)

#Advertise haircuts under $30

#Try 1
#cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
#Try 2
#cuts_under_30 = [hairstyles[i] for i in range(0, (len(hairstyles) - 1)) if new_prices[i] < 30]

#CANT GET IT TO PRINT THE CORRECT HAIRCUTS. SHOULD BE ['bouffant', 'pixie', 'crew', 'bowl']

#Try 3
cuts_under_30 = []
#for i in range(len(prices)): 
#  if new_prices[i] < 30:
#    cuts_under_30.append(hairstyles[i]) 
print(cuts_under_30)
