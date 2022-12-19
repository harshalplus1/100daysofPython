from turtle import Turtle, Screen
import random

s=Screen()
s.screensize(300,300)
user_=s.textinput(prompt='Choose your bet',title='Enter the color')
s.listen()
pos=[-100,-70,-40,-10,20]
t=[]
col=['blue','red','green','brown','pink']
for r in range(0,5):
    x=Turtle()
    x.color(col[r])
    t.append(x)
    t[r].penup()
    t[r].goto(-230,pos[r])
dis=[10,50,30,20,60]
c=[-230,-230,-230,-230,-230]
x=True
w=0
while(x):
    for r in range(0,5):
        l=random.randint(0,4)
        t[r].forward(dis[l])
        c[r]+=dis[l]
    if max(c)>=230:
        x=False
        m=max(c)
        for z in range(0,5):
            if c[z]==m:
                w=z
                print(f"Winner of the game {col[w]} turtle")
                break
        break
if col[w]==user_:
    print("Congratulations you won the bet")
else:
    print("You Lost")

s.exitonclick()

