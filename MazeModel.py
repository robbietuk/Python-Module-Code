"""
Exercise: a Maze Model.
Work with a partner to design a data structure to represent a maze using dictionaries and lists.

Each place in the maze has a name, which is a string.
Each place in the maze has one or more people currently standing at it, by name.
Each place in the maze has a maximum capacity of people that can fit in it.
From each place in the maze, you can go from that place to a few other places, using a direction like 'up', 'north', or 'sideways'
Create an example instance, in a notebook, of a simple structure for your maze:

The front room can hold 2 people. James is currently there. You can go outside to the garden, or upstairs to the bedroom, or north to the kitchen.
From the kitchen, you can go south to the front room. It fits 1 person.
From the garden you can go inside to front room. It fits 3 people. Sue is currently there.
From the bedroom, you can go downstairs to the front room. You can also jump out of the window to the garden. It fits 2 people.
Make sure that your model:

Allows empty rooms
Allows you to jump out of the upstairs window, but not to fly back up.
Allows rooms which people can't fit in.
"""

myHouse = {
    'frontRoom': {
        'capacity': 2,
        'occupants': ['James'],
        'exits': {
            'upstairs': 'bedroom',
            'outside': 'garden',
            'north': 'kitchen'
        }
    },

    "kitchen": {
        'capacity': 1,
        'occupants': [],
        'exits': {'south': 'frontRoom'}
    },

    'garden': {
        'capacity': 3,
        'occupants': ['Sue'],
        'exits': {'inside': 'frontRoom'}
    },

    'bedroom': {
        'capacity': 2,
        'occupants': [],
        'exits': {'downstairs': 'frontRoom',
                  'jump!': 'garden'
                  }
    }
}
