# Hide and Seek Game
## Video Demo:  (https://youtu.be/sRstZ9tSq7A)
## Project Overview

This project is a text-based hide and seek game. It allows users to place obstacles on a map, check safe locations, and find paths between two points while avoiding obstacles. The game is run through a command-line interface where users can input various commands to interact with the game world.

## Files and Their Functions

### project.py

This is the main file of the project. It contains all the classes and functions needed to run the game. Here's what each main part does:

- `Obstacle`, `Fence`, and `Guard` classes: These define the obstacles in the game. Each obstacle has a position and can check if it blocks a certain location.

- `AddObstacle` class: This handles adding new obstacles to the game. It can add guards and fences based on user input.

- `Map` class: This creates and displays a text-based map of the game area, showing where obstacles are located.

- `CheckObstacles` class: This checks if a given location is safe and tells the user which directions they can move safely.

- `Astar` and `FindingPath` classes: These work together to find a safe path between two points on the map, avoiding all obstacles.

- `main()` function: This runs the game loop, taking user input and calling the appropriate functions based on the commands given.

### test_project.py

This file contains tests for the main functions in the game. It checks if:

- Obstacles are added correctly
- The map is drawn as expected
- The obstacle checking function works properly
- The path finding function can find a correct path

Each test function runs a part of the game and compares the output to what we expect to see if everything is working correctly.

## Design Choices

1. Command-line Interface: We chose to make this a text-based game to keep it simple and focus on the core game logic rather than graphics.

2. Obstacle Types: We included two types of obstacles (guards and fences) to add variety to the game. Guards block a single point, while fences can block multiple points in a line.

3. A* Pathfinding: We used the A* algorithm for finding paths because it's efficient and widely used for this kind of problem.

4. Separate Classes: We split the game into several classes to keep the code organized. Each class has a specific job, which makes the code easier to understand and change if needed.

## How to Use

To play the game:

1. Run `python project.py` in your command line.
2. Follow the on-screen instructions to add obstacles, check locations, or find paths.
3. Type 'exit' to end the game.

To run the tests:

1. Run `pytest test_project.py` in your command line.
2. The test results will be printed, showing if each part of the game is working as expected.

This project demonstrates basic game logic, pathfinding, and object-oriented programming in Python. It can be expanded with more features like different obstacle types, larger maps, or even a simple GUI in the future.
