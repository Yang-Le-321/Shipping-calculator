import sys

# User input
weight = input("what is the weight of your package in pounds? ")
if weight == "":
  print("You need to give the weight of the package" )
  sys.exit()
else:
  weight = float(weight)
  if weight <=0:
    print("You have to put a weight larger than 0.")
    sys.exit()
  
# Ground shipping
if weight >0 <=2:
  cost_ground = weight * 1.5 + 20
elif weight >2 <=6:
  cost_ground = weight * 3.0 + 20
elif weight >6 <=10:
  cost_ground = weight * 4.0 + 20
elif weight >10: 
  cost_ground = weight * 4.75 + 20  
else: 
  print("not applicable")
print("Ground shipping $", cost_ground)

# Ground shipping premium
if weight >0:
  cost_ground_premium = 125.00
else: 
  print("not applicable")
print("Ground Shipping Premium $", cost_ground_premium)

# Drone shipping
if weight >0 <=2:
  cost_drone = weight * 4.5
elif weight >2 <=6:
  cost_drone = weight * 9.0 
elif weight >6 <=10:
  cost_drone = weight * 12.0
elif weight >10: 
  cost_drone = weight * 14.2  
else: 
  print("not applicable")
print("Drone shipping $", cost_drone)

