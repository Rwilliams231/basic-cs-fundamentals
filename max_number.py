# max_number.py
# Finds the largest number in a list

nums = input("Enter numbers separated by spaces: ").split()
nums = [float(n) for n in nums]
print("Largest number:", max(nums))
