from tkinter import *
import random
import time

class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.score = 0
        self.x=starts[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False
        
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1] <=0:
            self.y=1
        if pos[3] >=self.canvas_height:
            self.y=-3
        if pos[3]>=self.canvas_height:
            self.hit_bottom=True
        if self.hit_paddle(pos)==True:
            self.canvas.create_text(30,20,text='Score: '+str(self.score),fill='white')
            self.score+=1            
            self.canvas.create_text(30,20,text='Score: '+str(self.score),fill='red')
            self.y=-3
        if pos[0] <=0:
            self.x=3
        if pos[2] >=self.canvas_width:
            self.x=-3

    def hit_paddle(self,pos):      
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2] >=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
        return False
        
class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x=0
        self.start_game = False
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        self.canvas.bind_all('<Button-1>',self.start)

    def turn_left(self,evt):
        self.x=-4

    def turn_right(self,evt):
        self.x=4

    def start(self, evt):
        self.start_game = True

    def draw(self):
        pass

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0] <=0:
            self.x=0
        elif pos[2] >=self.canvas_width:
            self.x=0
    
tk=Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()

tk.update()

paddle=Paddle(canvas,'blue')
ball=Ball(canvas,paddle,'red')

while 1:
    
    if ball.hit_bottom==False and paddle.start_game == True:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

