import settings
import copy


def bfs(maze_origin, start, end):
    # return: 前置节点表 prev: 从终点向前倒推出路径。二维列表,基本元素是元组，存放前置结点
    maze = copy.deepcopy(maze_origin)  # 从maze_origin深拷贝一份到maze

    prev = []  # 根据maze的尺寸初始化prev，每个结点初始化为(-1,-1)
    rows = len(maze)  # 行数
    cols = len(maze[0])  # 列数
    for i in range(rows):
        temp = []
        for j in range(cols):
            temp.append((-1, -1))
        prev.append(temp)
    openlist = []
    openlist.append(start)
    maze[start[0]][start[1]] = settings.wall_char

    # bfs
    while len(openlist) != 0:
        current = openlist.pop(0)  # 从openlist将队首元素出队->current
        if current == end:  # 如果current为终点end，则循环结束
            break

        dx = [-1, 1, 0, 0]  # 上，下，左，右
        dy = [0, 0, -1, 1]
        if (0 <= current[0] < cols) and (0 <= current[1] < rows):  # 当前结点current的四周不超出迷宫的范围
            for k in range(3):  # 按照上-下-左-右的顺序依次扩展current四周的结点
                if maze[current[0] + k][current[1] + k] != settings.wall_char:  # 四周结点不是障碍字符
                    openlist.append(([current[0] + k], [current[1] + k]))  # 就入队openlist成为带扩展的结点
                    maze[current[0] + k][current[1] + k] = settings.wall_char  # maze表对应的位置设置成障碍字符
                    prev[current[0] + k][current[1] + k] = current  # prev表对应的位置更新成当前位置
    return prev
