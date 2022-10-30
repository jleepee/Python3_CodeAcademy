
weight = 41.5

#Ground shipping Attempt 1
#if weight <= 2:
 # print('Standard Ground:' , weight * 4 + 20.00)
#elif weight > 2 and weight <= 6:
 # print('Standard Ground:' , weight * 3 + 20.00)
#elif weight > 6 and weight <= 10:
 # print('Standard Ground:' , weight * 4 + 20.00)
#else:
 # print('Standard Ground:' , weight * 4.75 + 20)

#Premium groud shipping
premium = 125.00
print('Premium Ground: $' , premium)

#Ground shipping attempt 2
ground1 = 0
ground2 = 0
ground3 = 0
ground4 = 0

if weight <= 2:
  ground1 = weight * 4 + 20.00
elif weight > 2 and weight <= 6:
  ground2 = weight * 3 + 20.00
elif weight > 6 and weight <= 10:
  ground3 = weight * 4 + 20.00
else:
  ground4 = weight * 4.75 + 20

standard_ground = ground1 + ground2 + ground3 + ground4

print('Standard Ground: $' , standard_ground)


#Drone Shipping
drone1 = 0
drone2 = 0
drone3 = 0
drone4 = 0

if weight <= 2:
  drone1 = weight * 4.50
elif weight > 2 and weight <= 6:
  drone2 = weight * 9.00
elif weight > 6 and weight <= 10:
  drone3 = weight * 12.00
else:
  drone4 = weight * 14.25

drone_shipping = drone1 + drone2 + drone3 + drone4

print('Drone Shipping: $' , drone_shipping)
