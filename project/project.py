from typing import List, Optional
from abc import ABC, abstractmethod

# Obstacle classes
class Obstacle(ABC):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @property
    @abstractmethod
    def obstacle_type(self) -> str:
        pass

    @abstractmethod
    def is_obstructed(self, x: int, y: int) -> bool:
        pass

class Fence(Obstacle):
    def __init__(self, x: int, y: int, orientation: str, length: int):
        super().__init__(x, y)
        self.orientation = orientation
        self.length = length

    @property
    def obstacle_type(self) -> str:
        return "F"

    def is_obstructed(self, x: int, y: int) -> bool:
        if self.orientation == "north":
            return y >= self.y and y < self.y + self.length and x == self.x
        elif self.orientation == "east":
            return x >= self.x and x < self.x + self.length and y == self.y
        return False

class Guard(Obstacle):
    @property
    def obstacle_type(self) -> str:
        return "G"

    def is_obstructed(self, x: int, y: int) -> bool:
        return x == self.x and y == self.y

# AddObstacle class
class AddObstacle:
    def __init__(self, obstacles: List[Obstacle]):
        self.obstacles = obstacles

    def add_guard(self, input_str: str):
        try:
            words = input_str.split()
            if len(words) != 4:
                raise ValueError("Incorrect number of arguments.")

            x, y = int(words[2]), int(words[3])
            self.obstacles.append(Guard(x, y))
            print("Successfully added guard obstacle.")
        except ValueError as e:
            print(f"Error: {str(e)}")

    def add_fence(self, input_str: str):
        try:
            words = input_str.split()
            if len(words) != 6:
                raise ValueError("Incorrect number of arguments.")

            x, y = int(words[2]), int(words[3])
            orientation = words[4]
            length = int(words[5])

            if orientation not in ["east", "north"]:
                raise ValueError("Orientation must be 'east' or 'north'.")

            if length <= 0:
                raise ValueError("Length must be a valid integer greater than 0.")

            self.obstacles.append(Fence(x, y, orientation, length))
            print("Successfully added fence obstacle.")
        except ValueError as e:
            print(f"Error: {str(e)}")

# Map class
class Map:
    def __init__(self, obstacles: List[Obstacle]):
        self.obstacles = obstacles

    def add_obstacle(self, obstacle: Obstacle):
        self.obstacles.append(obstacle)

    def draw_map(self, input_str: str):
        try:
            words = input_str.split()

            if len(words) != 5:
                raise ValueError("Incorrect number of arguments.")

            start_x, start_y = int(words[1]), int(words[2])
            width, height = int(words[3]), int(words[4])

            if width <= 0 or height <= 0:
                raise ValueError("Width and height must be valid positive integers.")

            map_array = [['.' for _ in range(width)] for _ in range(height)]

            for obstacle in self.obstacles:
                for i in range(height):
                    for j in range(width):
                        if obstacle.is_obstructed(j + start_x, i + start_y):
                            map_array[height - 1 - i][j] = obstacle.obstacle_type[0]

            print("Here is a map of obstacles in the selected region:")
            for row in map_array:
                print(''.join(row))

        except Exception as e:
            print(f"Error: {str(e)}")

# CheckObstacles class
class CheckObstacles:
    def __init__(self, obstacles: List[Obstacle]):
        self.obstacles = obstacles

    def check(self, input_str: str):
        try:
            words = input_str.split()

            if len(words) != 3:
                raise ValueError("Incorrect number of arguments.")

            x, y = int(words[1]), int(words[2])

            is_occupied = False
            can_move = {
                "North": True,
                "South": True,
                "East": True,
                "West": True
            }

            for obstacle in self.obstacles:
                if obstacle.is_obstructed(x, y):
                    is_occupied = True
                    break

                if obstacle.is_obstructed(x, y + 1):
                    can_move["North"] = False
                if obstacle.is_obstructed(x, y - 1):
                    can_move["South"] = False
                if obstacle.is_obstructed(x + 1, y):
                    can_move["East"] = False
                if obstacle.is_obstructed(x - 1, y):
                    can_move["West"] = False

            if is_occupied:
                raise ValueError("Agent, your location is compromised. Abort mission.")
            elif not any(can_move.values()):
                raise ValueError("You cannot safely move in any direction. Abort mission.")
            else:
                print("You can safely take any of the following directions:")
                for direction, safe in can_move.items():
                    if safe:
                        print(direction)

        except Exception as e:
            print(f"Error: {str(e)}")

# Astar and FindingPath classes
class Location:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = None

class Astar:
    def __init__(self, obstacles: List[Obstacle]):
        self.obstacles = obstacles

    def find_path_using_astar(self, start_x: int, start_y: int, target_x: int, target_y: int) -> Optional[List[Location]]:
        open_list = []
        closed_list = []

        start = Location(start_x, start_y)
        target = Location(target_x, target_y)

        open_list.append(start)

        while open_list:
            current = min(open_list, key=lambda l: l.f)
            open_list.remove(current)
            closed_list.append(current)

            if current.x == target.x and current.y == target.y:
                return self.build_path(current)

            adjacent_squares = self.get_walkable_adjacent_squares(current.x, current.y)

            for adjacent in adjacent_squares:
                if any(l.x == adjacent.x and l.y == adjacent.y for l in closed_list):
                    continue

                if adjacent not in open_list:
                    adjacent.g = current.g + 1
                    adjacent.h = self.compute_h_score(adjacent.x, adjacent.y, target.x, target.y)
                    adjacent.f = adjacent.g + adjacent.h
                    adjacent.parent = current
                    open_list.append(adjacent)
                else:
                    existing = next(l for l in open_list if l.x == adjacent.x and l.y == adjacent.y)
                    if current.g + 1 < existing.g:
                        existing.g = current.g + 1
                        existing.f = existing.g + existing.h
                        existing.parent = current

        return None

    def get_walkable_adjacent_squares(self, x: int, y: int) -> List[Location]:
        proposed_locations = [
            Location(x, y - 1),
            Location(x, y + 1),
            Location(x - 1, y),
            Location(x + 1, y)
        ]
        return [l for l in proposed_locations if not self.is_obstructed(l.x, l.y)]

    def compute_h_score(self, x: int, y: int, target_x: int, target_y: int) -> int:
        return abs(target_x - x) + abs(target_y - y)

    def is_obstructed(self, x: int, y: int) -> bool:
        return any(obstacle.is_obstructed(x, y) for obstacle in self.obstacles)

    def build_path(self, current: Location) -> List[Location]:
        path = []
        while current:
            path.append(current)
            current = current.parent
        return list(reversed(path))

class FindingPath:
    def __init__(self, obstacles: List[Obstacle]):
        self.obstacles = obstacles
        self.astar = Astar(obstacles)

    def find_path(self, input_str: str):
        try:
            words = input_str.split()

            if len(words) != 5:
                raise ValueError("Incorrect number of arguments.")

            agent_x, agent_y = int(words[1]), int(words[2])
            objective_x, objective_y = int(words[3]), int(words[4])

            if agent_x == objective_x and agent_y == objective_y:
                print("Agent, you are already at the objective.")
                return

            if self.astar.is_obstructed(objective_x, objective_y):
                print("The objective is blocked by an obstacle and cannot be reached.")
                return

            path = self.astar.find_path_using_astar(agent_x, agent_y, objective_x, objective_y)

            if path:
                print("The following path will take you to the objective:")
                self.print_path(path)
            else:
                print("There is no safe path to the objective.")

        except Exception as e:
            print(f"Error: {str(e)}")

    def print_path(self, path: List[Location]):
        directions = []
        current_direction = ""
        distance = 0

        for i in range(1, len(path)):
            dx = path[i].x - path[i-1].x
            dy = path[i].y - path[i-1].y

            new_direction = ""
            if dx == 0 and dy == 1:
                new_direction = "north"
            elif dx == 0 and dy == -1:
                new_direction = "south"
            elif dx == -1 and dy == 0:
                new_direction = "west"
            elif dx == 1 and dy == 0:
                new_direction = "east"

            if new_direction == current_direction:
                distance += 1
            else:
                if distance > 0:
                    directions.append(f"Head {current_direction} for {distance} klick{'s' if distance > 1 else ''}.")
                current_direction = new_direction
                distance = 1

        if distance > 0:
            directions.append(f"Head {current_direction} for {distance} klick{'s' if distance > 1 else ''}.")

        for direction in directions:
            print(direction)

# Main program
def main():
    obstacles: List[Obstacle] = []
    add_ob = AddObstacle(obstacles)
    map_obj = Map(obstacles)
    check_ob = CheckObstacles(obstacles)
    path = FindingPath(obstacles)

    menu = (
        "Valid commands are:\n"
        "add guard <x> <y>: registers a guard obstacle\n"
        "add fence <x> <y> <orientation> <length>: registers a fence obstacle. Orientation must be 'east' or 'north'.\n"
        "check <x> <y>: checks whether a location and its surroundings are safe\n"
        "map <x> <y> <width> <height>: draws a text-based map of registered obstacles\n"
        "path <agent x> <agent y> <objective x> <objective y>: finds a path free of obstacles\n"
        "help: displays this help message\n"
        "exit: closes this program\n\n"
        "Enter command:"
    )

    print("Welcome to Hide-and-Seek")
    print(menu)
    response = input()

    while response != "exit":
        try:
            if response == "help":
                print(menu)
            elif response == "add":
                print("You need to specify an obstacle type.")
            elif response.startswith("add "):
                command = response.split()
                if len(command) >= 2:
                    if command[1] == "guard":
                        add_ob.add_guard(response)
                    elif command[1] == "fence":
                        add_ob.add_fence(response)
                    else:
                        print("Invalid obstacle type.")
            elif response.startswith("map "):
                map_obj.draw_map(response)
            elif response.startswith("check "):
                check_ob.check(response)
            elif response.startswith("path "):
                path.find_path(response)
            else:
                raise ValueError(f"Invalid option: {response}\nType 'help' to see a list of commands.")
        except Exception as ex:
            print(str(ex))

        print("Enter command: ")
        response = input()

    print("Thank you!")

if __name__ == "__main__":
    main()
