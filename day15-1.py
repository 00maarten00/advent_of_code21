#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/15/input
import parser as p
global maze
maze = p.singleparse("input15")
global end
end = (len(maze)-1,len(maze[0])-1)
global lowest_score
lowest_score = 0

def do_maze(pos, score):
    global lowest_score
    if lowest_score != 0 and lowest_score <= score + int(maze[pos[0]][pos[1]]):
        return
    if pos == (end):
        score = score + int(maze[pos[0]][pos[1]])
        if lowest_score == 0 or lowest_score > score:
            lowest_score = score
        print(lowest_score)
        return 
    if pos[0] < end[0]:
        do_maze((pos[0]+1,pos[1]),score + int(maze[pos[0]][pos[1]]))
    if pos[1] < end[1]:
        do_maze((pos[0],pos[1]+1),score + int(maze[pos[0]][pos[1]]))
    return score + int(maze[pos[0]][pos[1]])

start = (0,0)
do_maze(start,0)
print(lowest_score-int(maze[0][0]))
        