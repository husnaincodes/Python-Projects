import math
from scipy.stats import norm

# Given values
x_bar = 10.455
sigma = 7.7
n = 44
confidence = 0.90

# Z critical value
z = norm.ppf(1 - (1 - confidence) / 2)

# Standard error
SE = sigma / math.sqrt(n)

# Margin of error
ME = z * SE

# Confidence interval
lower = x_bar - ME
upper = x_bar + ME

print("Z value:", z)
print("Margin of Error:", ME)
print("90% Confidence Interval:", (lower, upper))