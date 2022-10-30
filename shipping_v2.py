weight = 41.5
premium_ground = 125
ground_shipping = 0
drone_shipping = 0

#Ground Shipping Price
if weight <= 2.0:
  ground_shipping = weight * 1.5 + 20
elif weight > 2.0 and weight <= 6.0:
  ground_shipping = weight * 3.0 + 20
elif weight > 6.0 and weight <= 10.0:
  ground_shipping = weight * 4.0 + 20
else:
  ground_shipping = weight * 4.75 + 20

#Drone Shipping Price
if weight <= 2.0:
  drone_shipping = weight * 4.5
elif weight > 2.0 and weight <= 9.0:
  drone_shipping = weight * 3.0
elif weight > 6.0 and weight <= 12.0:
  drone_shipping = weight * 4.0
else:
  drone_shipping = weight * 14.25

print('Your package weighs:', weight)
print('\nAll Shipping Costs:')
print('Standard Ground Shipping Cost:', ground_shipping)
print('Premium Ground Shipping Cost:', premium_ground)
print('Drone Shipping Cost:', drone_shipping)

if ground_shipping < drone_shipping and ground_shipping < premium_ground:
  print('\n\nCheapest Method: Standard Ground Shipping\n' + 'Standard Ground Shipping Cost:', ground_shipping)
elif drone_shipping < ground_shipping and drone_shipping < premium_ground:
  print('\n\nCheapest Method: Drone Shipping\n' + 'Drone Shipping Cost:', drone_shipping)
else:
   print('\n\nCheapest Method: Premium Ground Shipping\n' + 'Premium Ground Shipping Cost:', premium_ground)
