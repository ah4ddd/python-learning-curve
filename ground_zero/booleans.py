# Step 1: Create variables
has_key = True
knows_password = False
is_door_locked = True

# Step 2: Basic comparisons
print("Door locked?", is_door_locked)            # Prints True
print("User has key?", has_key)                  # Prints True
print("User knows password?", knows_password)    # Prints False

# Step 3: Boolean expressions
can_open_door = has_key or knows_password        # True if has key OR knows password
cannot_open_door = not can_open_door            # Flip it

print("\nBoolean expressions:")
print("Can open door?", can_open_door)          # True
print("Cannot open door?", cannot_open_door)    # False

# Step 4: Combine with logical operators
full_access = (has_key and knows_password) or (not is_door_locked)
print("\nCombined logic:")
print("Full access granted?", full_access)      # True if both conditions or door unlocked

# Step 5: Update variable dynamically
knows_password = True
full_access = (has_key and knows_password) or (not is_door_locked)
print("\nAfter user learns password:")
print("Full access granted?", full_access)      # True
