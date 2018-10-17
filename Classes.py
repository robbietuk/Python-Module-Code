


class Room(object):
    def overful(self):
        return len(self.occupants) > self.capacity
    def full(self):
        return len(self.occupants) == self.capacity


myroom = Room()
myroom.name = "Kitchen"
myroom.capacity = 1
myroom.occupants = ["Bob"]



print(myroom.overful())
print(myroom.full())






