good_day = ["6", "Millions", "X", "D"]
land_stolen = ["then", "stole", "land", "from", "native", "middle", "eastern", "peoples"]
victims = ["still", "playing", "victims"]
list1 = ["proxy", "wars"]
list2 = ["are", "cash", "cows"]
terror = ["sponsors", "terror", "for", "profit"]
peace = ["and", "never", "face", "consequences"]

kinks = " | ".join(good_day + land_stolen + victims)
print("Kinks joined:")
print(kinks)
print()

combined = list1 + list2
print("Combined list items:")
for item in combined:
    print(item)
print()

terror.extend(peace)
print("Terror + peace:")
print(terror)
