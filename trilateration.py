import math
import numpy as np
from scipy.optimize import minimize

earthR = 6371

LatA = float(input("Latitude of known point A: "))
LonA = float(input("Longitude of known point A: "))
DistA = float(input("Distance from point A to unknown point (km): "))
print("\r")
LatB = float(input("Latitude of known point B: "))
LonB = float(input("Longitude of known point B: "))
DistB = float(input("Distance from point B to unknown point (km): "))
print("\r")
LatC = float(input("Latitude of known point C: "))
LonC = float(input("Longitude of known point C: "))
DistC = float(input("Distance from point C to unknown point (km): "))
print("\r")

LatA_rad = math.radians(LatA)
LonA_rad = math.radians(LonA)
LatB_rad = math.radians(LatB)
LonB_rad = math.radians(LonB)
LatC_rad = math.radians(LatC)
LonC_rad = math.radians(LonC)

def cost_function(point):
    x, y, z = point
    est_dist_A = np.sqrt((earthR * math.cos(LatA_rad) * math.cos(LonA_rad) - x) ** 2 +
                         (earthR * math.cos(LatA_rad) * math.sin(LonA_rad) - y) ** 2 +
                         (earthR * math.sin(LatA_rad) - z) ** 2)
    est_dist_B = np.sqrt((earthR * math.cos(LatB_rad) * math.cos(LonB_rad) - x) ** 2 +
                         (earthR * math.cos(LatB_rad) * math.sin(LonB_rad) - y) ** 2 +
                         (earthR * math.sin(LatB_rad) - z) ** 2)
    est_dist_C = np.sqrt((earthR * math.cos(LatC_rad) * math.cos(LonC_rad) - x) ** 2 +
                         (earthR * math.cos(LatC_rad) * math.sin(LonC_rad) - y) ** 2 +
                         (earthR * math.sin(LatC_rad) - z) ** 2)
    return (est_dist_A - DistA) ** 2 + (est_dist_B - DistB) ** 2 + (est_dist_C - DistC) ** 2

initial_point = [0, 0, 0]

result = minimize(cost_function, initial_point, method='Nelder-Mead')

x_opt, y_opt, z_opt = result.x

lat_opt = math.degrees(math.asin(z_opt / earthR))
lon_opt = math.degrees(math.atan2(y_opt, x_opt))

print("Latitude:", lat_opt)
print("Longitude:", lon_opt)
