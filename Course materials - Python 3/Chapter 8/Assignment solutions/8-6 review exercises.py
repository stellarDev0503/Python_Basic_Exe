# 8.6 review exercises

from random import randint


# Simulate the toss of a die
print(randint(1, 6))


# Simulate 10,000 throws of dice and display the average result
trials = 10000
total = 0
for trial in range(0, trials):
    total += randint(1, 6)
avg_result = total / trials
print("The average result of {} throws was {}".format(trials, avg_result))
