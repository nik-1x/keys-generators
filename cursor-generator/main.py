import pyautogui

key = 0

# settings
nl = 33
k = 4

while True:
    pos = pyautogui.position()
    x, y = pos.x, pos.y

    if (x and y) != 0:
        key += (x*2 * y*2) ** k

    # use only for user security, not for game chances
    percentage = len(str(key))/(nl/100)

    if percentage == 100:
        print(str(percentage)+" %")
        print("Generation finished, key: ", key)
        break
    else:
        print(str(percentage)+" %")
