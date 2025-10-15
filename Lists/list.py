items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # 10 items total

first_half = items[1:4]   # Gets items 0,1,2,3,4
second_half = items[5:10]  # Gets items 5,6,7,8,9

print("First half:", first_half)
print("Second half:", second_half)

word = "incredible"
print(word[2:7])  # indexes 2,3,4,5,6 → 'cred' + 'i'?
# indexes 2 to 6 included, 7 excluded
