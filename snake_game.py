import curses
from random import randint

# Setup window
curses.initscr()
win = curses.newwin(20, 60, 0, 0)  # Creates a new window
win.keypad(1)  # Enable arrow keys
curses.noecho()  # Do not display input
curses.curs_set(0)  # Hide cursor
win.border(0)
win.nodelay(1)  # Non-blocking input

# Snake and food settings
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)

win.addch(food[0], food[1], '#')

# Game logic variables
score = 0
ESC = 27
key = curses.KEY_RIGHT  # Initial movement direction

# Game loop
while key != ESC:
    win.addstr(0, 2, 'Score: ' + str(score) + ' ')
    win.timeout(150 - (len(snake) // 5 + len(snake) // 10) % 120)  # Increase speed

    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    # Calculate new coordinates of the head of the snake
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1
    
    snake.insert(0, (y, x))

    # Check if snake eats food
    if snake[0] == food:
        score += 1
        food = ()
        while food == ():
            food = (randint(1, 18), randint(1, 58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '#')
    else:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    # Check if snake collides with itself or the border
    if (y == 0 or y == 19 or x == 0 or x == 59 or snake[0] in snake[1:]):
        break

    win.addch(snake[0][0], snake[0][1], '*')

curses.endwin()
print("Final Score: " + str(score))

