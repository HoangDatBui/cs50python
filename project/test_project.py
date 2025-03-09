from project import AddObstacle, Map, CheckObstacles, FindingPath

def main():
    test_add_obstacle()
    test_draw_map()
    test_check_obstacles()
    test_find_path()

def test_add_obstacle():
    obstacles = []
    add_ob = AddObstacle(obstacles)

    add_ob.add_guard("add guard 5 5")
    assert len(obstacles) == 1
    assert obstacles[0].x == 5 and obstacles[0].y == 5

    add_ob.add_fence("add fence 10 10 north 3")
    assert len(obstacles) == 2
    assert obstacles[1].x == 10 and obstacles[1].y == 10
    assert obstacles[1].orientation == "north" and obstacles[1].length == 3

def test_draw_map():
    obstacles = []
    add_ob = AddObstacle(obstacles)
    map_obj = Map(obstacles)

    add_ob.add_guard("add guard 1 1")
    add_ob.add_fence("add fence 2 2 east 3")
    map_obj.draw_map("map 0 0 5 5")


def test_check_obstacles():
    obstacles = []
    add_ob = AddObstacle(obstacles)
    check_ob = CheckObstacles(obstacles)

    add_ob.add_guard("add guard 5 5")
    check_ob.check("check 4 4")


def test_find_path():
    obstacles = []
    add_ob = AddObstacle(obstacles)
    path = FindingPath(obstacles)

    add_ob.add_guard("add guard 2 2")
    path.find_path("path 0 0 4 4")

if __name__ == "__main__":
    main()
