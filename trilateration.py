import math
import numpy as np
from scipy.optimize import minimize

# Define the polar and equatorial radii of the Earth in kilometers
earthRp = 6356.8  # Polar radius
earthRe = 6378.1  # Equatorial radius

# Define the coordinates of points A, B, and C
LatA = float(input("Latitude of known point A: "))
LonA = float(input("Longitude of known point A: "))
DistA = float(input("Distance from point A to the unknown point (km): "))
print("\r")
LatB = float(input("Latitude of known point B: "))
LonB = float(input("Longitude of known point B: "))
DistB = float(input("Distance from point B to the unknown point (km): "))
print("\r")
LatC = float(input("Latitude of known point C: "))
LonC = float(input("Longitude of known point C: "))
DistC = float(input("Distance from point C to the unknown point (km): "))
print("\r")

# Convert coordinates to radians
LatA_rad = math.radians(LatA)
LonA_rad = math.radians(LonA)
LatB_rad = math.radians(LatB)
LonB_rad = math.radians(LonB)
LatC_rad = math.radians(LatC)
LonC_rad = math.radians(LonC)

# Function to calculate the cost function
def cost_function(point):
    x, y, z = point
    # Estimated distances to points A, B, and C
    est_dist_A = np.sqrt((earthRe * math.cos(LatA_rad) * math.cos(LonA_rad) - x) ** 2 +
                         (earthRe * math.cos(LatA_rad) * math.sin(LonA_rad) - y) ** 2 +
                         (earthRp * math.sin(LatA_rad) - z) ** 2)
    est_dist_B = np.sqrt((earthRe * math.cos(LatB_rad) * math.cos(LonB_rad) - x) ** 2 +
                         (earthRe * math.cos(LatB_rad) * math.sin(LonB_rad) - y) ** 2 +
                         (earthRp * math.sin(LatB_rad) - z) ** 2)
    est_dist_C = np.sqrt((earthRe * math.cos(LatC_rad) * math.cos(LonC_rad) - x) ** 2 +
                         (earthRe * math.cos(LatC_rad) * math.sin(LonC_rad) - y) ** 2 +
                         (earthRp * math.sin(LatC_rad) - z) ** 2)
    # Cost function: sum of squares of differences between measured and estimated distances
    return (est_dist_A - DistA) ** 2 + (est_dist_B - DistB) ** 2 + (est_dist_C - DistC) ** 2

# Initial point for optimization
initial_point = [0, 0, 0]

# Perform optimization to find the position of the point
result = minimize(cost_function, initial_point, method='Nelder-Mead')

# Optimized point coordinates
x_opt, y_opt, z_opt = result.x

# Convert back to latitude and longitude
lat_opt = math.degrees(math.asin(z_opt / earthRp))
lon_opt = math.degrees(math.atan2(y_opt, x_opt))

print("Latitude:", lat_opt)
print("Longitude:", lon_opt)
