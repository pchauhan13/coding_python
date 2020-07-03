creature_names = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']
print(list(filter(lambda x: x[0].lower() in 'aeiou', creature_names)))

aquarium_tanks = [11, False, 18, 21, "", 12, 34, 0, [], {}]
print(list(filter(None, aquarium_tanks)))

aquarium_creatures = [
  {"name": "sammy", "species": "shark", "tank number": "11", "type": "fish"},
  {"name": "ashley", "species": "crab", "tank number": "25", "type": "shellfish"},
  {"name": "jo", "species": "guppy", "tank number": "18", "type": "fish"},
  {"name": "jackie", "species": "lobster", "tank number": "21", "type": "shellfish"},
  {"name": "charlie", "species": "clownfish", "tank number": "12", "type": "fish"},
  {"name": "olly", "species": "green turtle", "tank number": "34", "type": "turtle"}
]

def filter_set(aquarium_creatures, search_string):
    def iterator_func(x):
        for v in x.values():
            if search_string in v:
                return True
        return False
    return filter(iterator_func, aquarium_creatures)

print(list(filter_set(aquarium_creatures, "2")))