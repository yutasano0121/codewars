"""
Task
 	Your task is to escape from the carpark using only the staircases provided to reach the exit. You may not jump over the edge of the levels (you’re not Superman!) and the exit is always on the far right of the ground floor.
Rules
 	1. You are passed the carpark data as an argument into the function.
2. Free carparking spaces are represented by a 0
3. Staircases are represented by a 1
4. Your parking place (start position) is represented by a 2
5. The exit is always the far right element of the ground floor.
6. You must use the staircases to go down a level.
7. You will never start on a staircase.
8. The start level may be any level of the car park.
9. Each floor will have only one staircase apart from the ground floor which will not have any staircases.
Returns
 	Return an array of the quickest route out of the carpark
R1 = Move Right one parking space.
L1 = Move Left one parking space.
D1 = Move Down one level.
Example
Initialise
carpark = [[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 0]]
Working Out
You start in the most far right position on level 1
You have to move Left 4 places to reach the staircase => "L4"
You then go down one flight of stairs => "D1"
To escape you have to move Right 4 places => "R4"
Result
result = ["L4", "D1", "R4"]
"""


def escape(carpark):
    out = []  # output list
    floor_num = len(carpark)  # number of floors

    for i in range(floor_num):
        if 2 in carpark[i]:
            start_floor = i  # floor of the starting location
            loc = carpark[start_floor].index(2)  # starting location
            break

    stair_num = 0  # number of consecutive stairs
    for i in range(start_floor, floor_num):
        floor = carpark[i]  # current floor

        if i == floor_num - 1:  # ground floor
            exit = len(floor) - 1
            if loc == exit:
                return out
            else:
                out.append("R" + str(exit - loc))
                return out

        stair = floor.index(1)

        if stair_num > 0:  # when located at a staircase
            if stair == loc:
                stair_num += 1
                out[-1] = 'D' + str(stair_num)
                continue
            else:
                stair_num = 0

        if loc > stair:
            out.append('L' + str(loc - stair))
        else:
            out.append('R' + str(stair - loc))
        out.append('D1')  # down a staircase

        stair_num = 1
        loc = stair
