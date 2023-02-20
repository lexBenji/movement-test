from getch import getch
from stdio import *

board = [
'11111111',
'10000001',
'10000001',
'10000001',
'10000001',
'10000001',
'100000B1',
'11111111'
]

facing = 'up'

y = 1
x = 1
py = y
px = x

br = [list(x) for x in board]

while True:
    write('\033c')
    br[py][x] = br[py][x].replace('2','0')
    br[y][px] = br[y][px].replace('2','0')
    br[y][x] = '2'
    writeln(facing)
    writeln(y,' ',x)

    if facing == 'up':
        if br[y-1][x] == '1':
            writeln('#')
        elif br[y-1][x] == 'B':
            writeln('B')
        else:
            writeln('/')
    elif facing == 'down':
        if br[y+1][x] == '1':
            writeln('#')
        elif br[y+1][x] == 'B':
            writeln('B')
        else:
            writeln('/')
    elif facing == 'left':
        if br[y][x-1] == '1':
            writeln('#')
        elif br[y][x-1] == 'B':
            writeln('B')
        else:
            writeln('/')
    elif facing == 'right':
        if br[y][x+1] == '1':
            writeln('#')
        elif br[y][x+1] == 'B':
            writeln('B')
        else:
            writeln('/')

    for i in br:
        for j in i:
            if j == '1':
                write('#')
            elif j == '0':
                write(' ')
            elif j == '2':
                write('@')
            elif j == 'B':
                write('B')
        writeln()

    key = getch().lower()

    if key == 'x':
        break
    elif key == 'w':
        if facing == 'up':
            if br[y - 1][x] == '1' or br[y-1][x] == 'B':
                pass
            else:
                py = y
                y = y - 1
        elif facing == 'down':
            if br[y + 1][x] == '1' or br[y+1][x] == 'B':
                pass
            else:
                py = y
                y = y + 1
        elif facing == 'right':
            if br[y][x + 1] == '1' or br[y][x+1] == 'B':
                pass
            else:
                px = x
                x = x + 1
        elif facing == 'left':
            if br[y][x - 1] == '1' or br[y][x-1] == 'B':
                pass
            else:
                px = x
                x = x - 1
    elif key == 's':
        if facing == 'up':
            if br[y + 1][x] == '1' or br[y+1][x] == 'B':
                pass
            else:
                py = y
                y = y + 1
        elif facing == 'down':
            if br[y - 1][x] == '1' or br[y-1][x] == 'B':
                pass
            else:
                py = y
                y = y - 1
        elif facing == 'right':
            if br[y][x - 1] == '1' or br[y][x-1] == 'B':
                pass
            else:
                px = x
                x = x - 1
        elif facing == 'left':
            if br[y][x + 1] == '1' or br[y][x+1] == 'B':
                pass
            else:
                px = x
                x = x + 1
    elif key == 'd':
        if facing == 'up':
            if br[y][x + 1] == '1' or br[y][x+1] == 'B':
                pass
            else:
                px = x
                x = x + 1
        elif facing == 'down':
            if br[y][x - 1] == '1' or br[y][x-1] == 'B':
                pass
            else:
                px = x
                x = x - 1
        elif facing == 'right':
            if br[y + 1][x] == '1' or br[y+1][x] == 'B':
                pass
            else:
                py = y
                y = y + 1
        elif facing == 'left':
            if br[y - 1][x] == '1' or br[y-1][x] == 'B':
                pass
            else:
                py = y
                y = y - 1
    elif key == 'a':
        if facing == 'up':
            if br[y][x - 1] == '1' or br[y][x-1] == 'B':
                pass
            else:
                px = x
                x = x - 1
        elif facing == 'down':
            if br[y][x + 1] == '1' or br[y][x+1] == 'B':
                pass
            else:
                px = x
                x = x + 1
        elif facing == 'right':
            if br[y - 1][x] == '1' or br[y-1][x] == 'B':
                pass
            else:
                py = y
                y = y - 1
        elif facing == 'left':
            if br[y + 1][x] == '1' or br[y+1][x] == 'B':
                pass
            else:
                py = y
                y = y + 1
    elif key == 'l':
        facing = 'right'
    elif key == 'h':
        facing = 'left'
    elif key == 'j':
        facing = 'down'
    elif key == 'k':
        facing = 'up'
