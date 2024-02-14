# Group Members
# ,, Edward Eckle,
import numpy as np
import matplotlib.pyplot as plt

nums = []
num_intervals = 10

fname: str = "Project_1/random.out"

with open(fname, "r") as file:
    for num in file.readlines():
        nums.append(eval(num))

counts, bins = np.histogram(nums, num_intervals)

fig, axs = plt.subplots()

axs.hist(bins[:-1], bins, weights=counts, width=0.09, align="mid")
axs.set_title("Pseudo Random Number Distribution")
plt.xticks(np.arange(0.0, 1.1, 0.1))

plt.show()

# X^2 test parameters
# X2 = 0
# Oi = 0
# Ei = size / num_intervals

# # Iterate through each interval
# for i in range(num_intervals):
#     interval = (i / num_intervals, (i + 1) / num_intervals)
#     Oi = 0
#     num_i = []
#     for num in nums:
#         if num >= interval[0] and num < interval[1]:
#             num_i.append(num)
#             Oi += 1
#     X2 += (Oi - Ei) ** 2 / Ei


# print("X^2 value:", X2)
