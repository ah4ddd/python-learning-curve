def area_of_rectangle(length, width):
    area = length * width
    return area

room_1_area = area_of_rectangle(10, 12)
room_2_area = area_of_rectangle(14, 16)
print(f"Area of Room 1: {room_1_area} square units")
print(f"Area of Room 2: {room_2_area} square units")
total_area = room_1_area + room_2_area
print(f"Total area of both rooms: {total_area} square units")
