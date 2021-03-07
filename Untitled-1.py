
import pyautogui as p
import time

"""
#Spam
msg = input("¿Qué Mensaje desea enviar?\n")

n = int(input("¿Cuántas copias del mensaje quiere enviar?\n"))
time.sleep(5.0)
for x in range(n):
    p.write(msg)
    p.press("enter")
"""
"""
#Square
time.sleep(7.0)
distance = 200
while distance > 0:
    p.drag(distance, 0, duration=0.5)   # move right
    distance -= 5
    p.drag(0, distance, duration=0.5)   # move down
    p.drag(-distance, 0, duration=0.5)  # move left
    distance -= 5
    p.drag(0, -distance, duration=0.5)  # move up
 """   


#Upage
time.sleep(10.0)
p.hotkey("ctrl","n")
p.write("http://www.konradlorenz.edu.co/")
p.press("enter")

"""
#Playvideo
time.sleep(7.0)
p.hotkey("ctrl","t")
p.write("https://www.youtube.com/watch?v=AsrzqSJd8jo&ab_channel=PeriodistaGen%C3%A9rico")
p.press("enter")

time.sleep(7.0)
for x in range(3):
    p.press("right")
    time.sleep(4.0)
"""
"""
#Circle
time.sleep(5.0)
import math

# Radius 
R = 300
# measuring screen size
(x,y) = p.size()
# locating center of the screen 
(X,Y) = p.position(x/4,y/2)
# offsetting by radius 
p.moveTo(X+R,Y)

while R > 0:
    for i in range(360):
        # setting pace with a modulus 
        if i%6==0:
            p.dragTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
    R -= 10
    """
"""
(X,Y) = p.position(x/4 + x/2,y/2)
# offsetting by radius 
p.drag(button='right')
p.moveTo(X+R,Y)
R = 300
while R > 0:
    for i in range(360):
        # setting pace with a modulus 
        if i%6==0:
            p.dragTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
    R -= 10
"""