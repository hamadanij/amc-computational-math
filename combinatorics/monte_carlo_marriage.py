import random

def is_valid(arr):
    for i in range(len(arr)):
        if abs(i - arr[i]) > 1:
            return False
    return True

n = 5
trials = 1000000
hits = 0
nums = list(range(n))

#count valid matches
for _ in range(trials):
    random.shuffle(nums)
    if is_valid(nums):
        hits = hits + 1

sim_prob = hits / trials
true_prob = 8 / 120  # For n=5, there are 8 valid ways out of 120 total ways

print("Simulating trials...")
print("Simulated Hits:", hits)
print("Simulated Probability:", sim_prob)
print("True Math Probability:", true_prob)
