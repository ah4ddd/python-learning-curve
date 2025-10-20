history = ["Empires", "colonized", "lands", "for", "profit"]
modern_times = ["Corporations", "exploit", "workers", "globally"]
media = ["Propaganda", "spreads", "lies", "and", "fears"]
war = ["Weapons", "manufactured", "to", "fuel", "endless", "conflict"]
resistance = ["People", "rise", "against", "oppression", "eventually"]

separator = " 🔥 "
full_truth = separator.join(history + modern_times + media + war + resistance)

print("\n***BRUTAL TRUTH ABOUT POWER AND POLITICS***")
print(full_truth)

activism = ["Awareness", "Education", "Action"]
resistance.extend(activism)
print("\nExtended resistance list:")
print(resistance)

minor_events = ["Protests", "Boycotts"]
combined_events = resistance + minor_events
print("\nCombined events list:")
for event in combined_events:
    print(event)
