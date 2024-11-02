import random
import numpy as np
import matplotlib.pyplot as plt

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

# Plotting the histogram
plt.hist(sums, bins=range(6, 346, 1), density=True, alpha=0.75)
plt.xlabel('Sum of 5 Power Ball selection')
plt.ylabel('Frequency')
plt.title(f'Power Ball Standard Deviation: {std_deviation:.2f}')
plt.grid(True)
plt.show()
