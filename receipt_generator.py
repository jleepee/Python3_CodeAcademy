#Catalog
lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'
lovely_loveseat_price = 254.00
stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'
stylish_settee_price = 180.50
luxurious_lamp_description = 'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'
luxurious_lamp_price = 52.15

#Tax
sales_tax = .088

#First receipt
customer_one_total = lovely_loveseat_price + luxurious_lamp_price
customer_one_itemization = lovely_loveseat_description + luxurious_lamp_description
#Tax
customer_one_tax = customer_one_total * sales_tax
#Total with Tax
customer_one_total += customer_one_tax




#print(customer_one_tax)
#print(customer_one_total)
#print(333.091 - 26.941)

print("Customer One Items:")

print("Customer One Total:" , customer_one_total)
