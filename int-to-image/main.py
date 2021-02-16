from PIL import Image, ImageColor
import random

f = open('input.txt')
work = f.read()
f.close()
wlen = len(work)
print("==[ int to image ]==")
print("Key length: " + str(wlen))
stripe = wlen // 1000
print("Stripe length: " + str(stripe))
cwork = (wlen // stripe)

create = Image.new('RGB', (stripe, cwork), color='#FFFFFF')
create.save('task.png')

for row in range(cwork):
    rowdraw = Image.open("task.png")
    for index in range(stripe):
        indx = row * stripe + index
        r = [random.randint(0, 9), work[indx]]
        g = [random.randint(0, 9), random.randint(0, 9)]
        b = [random.randint(0, 9), random.randint(0, 9)]
        color = "#" + str(r[0]) + str(r[1]) + str(g[0]) + str(g[1]) + str(b[0]) + str(b[1])
        rowdraw.putpixel((index, row), ImageColor.getrgb(color))
    rowdraw.save('task.png')
