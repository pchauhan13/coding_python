friends = [ "Kevin", "Jim", "Karen" ]
print(friends[2])
print(friends[-1])
print(friends[1:])

lucky_numbers = [ 2, 34, 5, 543, 23]
friends.extend(lucky_numbers)
print(friends)

friends.append("Joe")
print(friends)

friends.insert(1, "Rachel")
print(friends)

friends.remove(2)
print(friends)

print(friends.index("Joe"))
# print(freinds.index(2))

print(friends.count("Jim"))

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

print(friends.pop())

friends.clear()
print(friends)
