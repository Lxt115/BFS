from bfs import bfs
import settings


def make_maze_path(prev, start, end):
    """
    :param prev: 前置节点表: 从终点向前倒推出路径。二维列表,基本元素是元组,存放前置结点
    :param start: 起点,元组 (a,b)
    :param end: 终点,元组 (a,b)
    :return: 迷宫路径: path。元组列表 [(a,b),(c,d),...,]
    """
    path = []
    # 根据prev和end，从终点向前倒推
    current = end
    while current != start:
        path.insert(0,current)
        current = prev[current[0]][current[1]]
    path.insert(0,start)
    return path


def make_maze_result(maze_origin, path):
    """
    :param maze_origin: 迷宫地图，二维列表: 基本元素是字符,迷宫字符
    :param path: 迷宫路径，元组列表 [(a,b),(c,d),...,]
    :return: 带有↑↓←→的迷宫地图 maze。二维列表: 基本元素是字符,迷宫字符和上下左右字符
    """
    maze = copy.deepcopy(maze_origin)
    for i in range(len(path) - 1):
        # 根据path更新带有↑，↓，←，→的maze
        if path[i][0] == path[i-1][0]:
            if path[i][1] == path[i-1][1] - 1:
                maze[path[i][0]][path[i][1]] = '←'
            else:
                maze[path[i][0]][path[i][1]] = '→'
        if path[i][1] == path[i-1][1]:
            if path[i][0] == path[i-1][0] + 1:
                maze[path[i][0]][path[i][1]] = '↓'
            else:
                maze[path[i][0]][path[i][1]] = '↑'
    return maze


maze = []  # list of list
start = (-1, -1)
end = (-1, -1)

with open(settings.filename) as file:
    # 将file按行读取到maze中，并且更新起点start，终点end
    for i, line in enumerate(file):
        maze.append(list(line.strip()))
        if line.find(settings.start_char) != -1:
            start = (i, line.find(settings.start_char))
        if line.find(settings.end_char) != -1:
            end = (i, line.find(settings.end_char))

prev = bfs(maze, start, end)
path = make_maze_path(prev, start, end)
length = len(path)
print('\n\n【Steps】:', length)
print('\n【Path】:')

print('-' * 85)
for i in range(1, length + 1):
    print(path[i - 1], end="\t")
    if i % 10 == 0:
        print()
print()
print('-' * 85)

print('\n【result】:')
maze_result = make_maze_result(maze, path)
for line in maze_result:
    print(''.join(line))