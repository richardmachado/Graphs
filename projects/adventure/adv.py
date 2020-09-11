from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

#!!!!!!!!!!!!!!!!!!!!!!!!!!MY CODE!!!!!!
#? Using queue for BFS
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#!!!!!!!!!!!!!!!!!!!MY CODE!!!!!!!!!!!!
#? dict to hold graph rooms or moves
traversal_graph = {}
#? while loop - while the length of the traversal graph is less than the total rooms
while len(traversal_graph) < len(room_graph):
    #? if the current room the player is in isn't in traversal graph yet
    if player.current_room.id not in traversal_graph:
        #? Add the room
        traversal_graph[player.current_room.id] = {}
        #? loop through all the exits
        for exits in player.current_room.get_exits():
            #? mark the exits with a question mark '?'
            traversal_graph[player.current_room.id][exits] = '?'

    #? now check for exits in the traversal graph dict
    if '?' in traversal_graph[player.current_room.id].values():
        #? make an empty list for the exit paths
        exit_paths = []

        #? loop through the current room's exits
        for i in player.current_room.get_exits():
            #? if the room still has an exit
            if traversal_graph[player.current_room.id][i] == '?':
                #? append any exits
                exit_paths.append(i)
    
        #? choose a random exit
        random_direction = random.choice(exit_paths)

        #? set the current room to be the previous room
        previous_room = player.current_room

        #? travel in a random direction
        player.travel(random_direction)

        #? set the player's current room id to the new direction id
        traversal_graph[previous_room.id][random_direction] = player.current_room.id
        #? add the random direction to the traversal path
        traversal_path.append(random_direction)

    #? this else statement was indented incorrectly, took me a minute to catch that
    else:
        #? create an empty queue
        q = Queue()

        #? add the id of the current room to the queue
        q.enqueue([player.current_room.id])

        #? create a set for visited rooms
        visited = set()

        #? while the queue is not empty, dequeue it
        while q.size() > 0:
            path = q.dequeue()
            last_room = path[-1]

            #? if that room hasn't been visited, add it to visited
            if last_room not in visited:
                visited.add(last_room)

                #? check for exits
                if '?' in traversal_graph[last_room].values():
                    #? offset it by -1 to so it starts with 0
                    for room in range(len(path) - 1):
                        for key, value in traversal_graph[path[room]].items():
                            if value == path[room + 1]:
                                direction = key
                        #traverse in that direction
                        player.travel(direction)
                        #? add that traversed direction to the traversal path
                        traversal_path.append(direction)
                    break
                
                else:
                    #? loop through the values in the last room
                    for exit in traversal_graph[last_room].values():
                        new_path = path + [exit]
                        #? add the new path to the queue
                        q.enqueue(new_path)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

