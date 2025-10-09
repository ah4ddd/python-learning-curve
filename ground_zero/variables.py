# Step 1: Post information (variables)
post_title = "Python Post"
likes = 40
comments = 15
shares = 5

# Step 2: Calculate total engagement (expression)
total_engagement = likes + comments + shares

# Step 3: Display post summary (using string concatenation)
print("Post Summary:")
print("Title: " + post_title)
print("Likes: " + str(likes))       # convert numbers to strings to concatenate
print("Comments: " + str(comments))
print("Shares: " + str(shares))
print("Total Engagement: " + str(total_engagement))

# Step 4: dynamic update
new_likes = 10
likes = likes + new_likes
total_engagement = likes + comments + shares  # recalc after update

print("\nAfter new likes:")
print("Likes: " + str(likes))
print("Total Engagement: " + str(total_engagement))
