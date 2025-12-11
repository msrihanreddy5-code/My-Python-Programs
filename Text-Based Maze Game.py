maze = [
    "#########",
    "#P     E#",
    "#########"
]

player_x = 1
player_y = 1

while True:
    for row in maze:
        print(row)

    move = input("Move (WASD): ").lower()

    new_x, new_y = player_x, player_y
    if move == "w": new_y -= 1
    if move == "s": new_y += 1
    if move == "a": new_x -= 1
    if move == "d": new_x += 1

    if maze[new_y][new_x] == "#":
        continue
    if maze[new_y][new_x] == "E":
        print("You Win!")
        break

    maze[player_y] = maze[player_y].replace("P", " ")
    player_x, player_y = new_x, new_y
    maze[player_y] = maze[player_y][:player_x] + "P" + maze[player_y][player_x+1:]
