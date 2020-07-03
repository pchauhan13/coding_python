creature_names = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']
print(list(filter(lambda x: x[0].lower() in 'aeiou', creature_names)))

aquarium_tanks = [11, False, 18, 21, "", 12, 34, 0, [], {}]
print(list(filter(None, aquarium_tanks)))