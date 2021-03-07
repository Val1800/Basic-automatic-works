# Basic-automatic-works

#Spam
import pyautogui as p
import time

msg = input("¿Qué Mensaje desea enviar?\n")

n = int(input("¿Cuántas copias del mensaje quiere enviar?\n"))
time.sleep(5.0)
for x in range(n):
    p.write(msg)
    p.press("enter")
    
    
#Square
import pyautogui as p
import time

time.sleep(7.0)
distance = 200
while distance > 0:
    p.drag(distance, 0, duration=0.5)   # move right
    distance -= 5
    p.drag(0, distance, duration=0.5)   # move down
    p.drag(-distance, 0, duration=0.5)  # move left
    distance -= 5
    p.drag(0, -distance, duration=0.5)  # move up
    

#Upage
import pyautogui as p
import time

time.sleep(10.0)
p.hotkey("ctrl","n")
p.write("http://www.konradlorenz.edu.co/")
p.press("enter")

#playvideo
import pyautogui as p
import time

time.sleep(7.0)
p.hotkey("ctrl","t")
p.write("https://www.youtube.com/watch?v=Mr9kC2k6jZY&ab_channel=OsidePenguinz")
p.press("enter")

time.sleep(7.0)
for x in range(3):
    p.press("right")
    time.sleep(4.0)
    
#Circle
import pyautogui as p
import time

R = 300
# measuring screen size
(x,y) = p.size()
# locating center of the screen 
(X,Y) = p.position(x/2,y/2)
# offsetting by radius 
p.moveTo(X+R,Y)

while R > 0:
    for i in range(360):
        # setting pace with a modulus 
        if i%6==0:
            p.dragTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
    R -= 10
