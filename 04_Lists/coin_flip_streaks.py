# import random

# numberOfStreaks = 0
# for experimentNumber in range(10000):
#     # Code that creates a list of 100 'heads' or 'tails' values.
#     result = [random.randint(0, 1) for i in range(100)]

#     # Code that checks if there is a streak of 6 heads or tails in a row.
#     for i in range(len(result)):
#         # if result[i] == 1:
#         streak = True
#         if i + 6 < 101:
#             for l in range(i, i + 6):
#                 if result[i] == result[l]:
#                     pass
#                 else:
#                     streak = False

#             if streak:
#                 numberOfStreaks += 1
#                 break

# print("Chance of streak: %s%%" % (numberOfStreaks / 100))

# gpt4o:


import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    # Generate a list of 100 'heads' (1) or 'tails' (0) values
    result = [random.randint(0, 1) for i in range(100)]

    # Check for streaks of 6 heads or tails
    streak_count = 1  # Start counting streak from 1
    for i in range(1, len(result)):
        if (
            result[i] == result[i - 1]
        ):  # Check if the current flip matches the previous flip
            streak_count += 1  # Increase the streak count
        else:
            streak_count = 1  # Reset streak count if they are not the same

        if streak_count == 6:  # If a streak of 6 is found
            numberOfStreaks += 1
            break  # Stop checking further since we found a streak

# Calculate and print the percentage of experiments that had a streak
print("Chance of streak: %.2f%%" % (numberOfStreaks / 10000 * 100))
