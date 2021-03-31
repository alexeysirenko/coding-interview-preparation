class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        currHor = 0
        currVer = 0
        angle = 360

        def goTo(currHor, currVer, angle, command):
            if command == 'G':
                if angle == 360 or angle == 0: # north
                    currVer += 1
                elif angle == 90: # east
                    currHor += 1
                elif angle == 180: #south
                    currVer -= 1
                elif angle == 270: # west
                    currHor -= 1

            elif command == 'L':
                angle = (angle - 90) % 360
            elif command == 'R':
                angle = (angle + 90) % 360
            return (currHor, currVer, angle)

        #for _ in range(4):
        for command in instructions:
            currHor, currVer, angle = goTo(currHor, currVer, angle, command)
            #print(command, 'x=', currHor, 'y=', currVer, 'angle=', angle)

        # same position as start or not facing north
        # or just returns to the (0, 0) after the 4 iterations
        return (currHor == 0 and currVer == 0) or 0 < angle < 360

