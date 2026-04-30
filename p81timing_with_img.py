from PIL import Image
import time

t = time.localtime()

h = t.tm_hour
m = t.tm_min
s = t.tm_sec


if h < 12:
    print(h, ":", m, ":", s, "AM - Good Morning")
    file = "morning.jpg"

elif h < 16:
    print(h, ":", m, ":", s, "PM - Good Afternoon")
    file = "afternoon.jpg"

elif h < 20:
    print(h, ":", m, ":", s, "PM - Good Evening")
    file = "evening.jpg"

else:
    print(h, ":", m, ":", s, "PM - Good Night")
    file="night.jpg"

img = Image.open(file)
img.show()