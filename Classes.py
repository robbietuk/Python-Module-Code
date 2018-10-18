class Room(object):
    def __init__(self, name, exits, capacity, occupants=[]):
        self.name = name
        self.exits = exits
        self.occupants = occupants
        self.capacity = capacity

    def overfull(self):
        return len(self.occupants) > self.capacity

    def full(self):
        return len(self.occupants) == self.capacity


Kitchen = Room("Kitchen", {'Garden': 'North'}, 3, ['Bob'])

print(Kitchen.occupants)
