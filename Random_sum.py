import random
import numpy as np

# Number of times to pick 5 random numbers
num_trials = 5000000

# List to store the sums
sums = []

# Perform the trials
for _ in range(num_trials):
    # Pick 5 random numbers
    random_numbers = [random.randint(1, 69) for _ in range(5)]
    # Calculate the sum
    sum_of_numbers = sum(random_numbers)
    # Add the sum to the list
    sums.append(sum_of_numbers)

# Calculate the standard deviation of the sums
std_deviation = np.std(sums)

print("Standard Deviation:", std_deviation)