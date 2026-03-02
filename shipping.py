weight = 12.75
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.0 + 20
  # more calculation
elif weight <= 10:
  cost_ground = weight * 4.0 + 20
  # more calculation
else:
  cost_ground = weight * 4.75 + 20
  # last calculation
  print("Ground Shipping $",cost_ground)
cost_ground_premium = 125.00
print("Ground Shipping Premium $", cost_ground_premium)
if weight <= 2:
  cost_drone = weight * 4.5 + 0
elif weight <= 6:
  cost_drone = weight * 9.0 + 0
  # more calculation
elif weight <= 10:
  cost_drone = weight * 12.0 + 0
  # more calculation
else:
  cost_drone = weight * 14.25 + 0
  # last calculation
  print("Drone Shipping $",cost_drone)