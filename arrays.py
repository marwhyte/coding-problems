new_list = [1, 2, 3]

# Search is O(N)
# offset of base memory (since it is contiguious)
# also why it crashes for out of bounds
result = new_list[0]
if 1 in new_list: print(True)

# Insert
# The way array resize works is that it increased array size by multiple
# To not have to resize every time. (0, 4, 8, 16, 25, 35, 46 ...)
    # True Insert O(N) - has to shift to the right
new_list.insert(2, 7)

    # Append O(1)
new_list.append(2)
    # Extend O(K) where K is the nubmers we are adding
new_list.extend([4, 5, 6])

# Delete O(N) - has to shift to the left
new_list.remove(2) # 
new_list.pop(0) # index

# How to delete all occurances
new_list = [x for x in new_list if x != 4]

print(new_list)
