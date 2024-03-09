from tkinter import *
import numpy as np
import random
import os
size_x=10
size_y=10
root = Tk( )
root.geometry("330x530")
explord=[]
front=[]
flag=0
goal=0
class node:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.right=0
        self.parent=0
        self.left=0
        self.up=0
        self.down=0
    def ckeck(v):
        print(v)
        if v in explord:
            return False
        return True
    def solve(map,x,y): 
        first=node(x,y)
        first.parent=-1
        explord.append(str(first.x)+str(first.y))
        front.append(first)  
        gfirst=first
        while len(front)>0:
         first=front.pop(0)
    #right
         if first!=0:
          if first.y+1<size_y:
            if map[first.x][first.y+1]!=0 and node.ckeck(str(first.x)+str(first.y+1))==True:
                first.right=node(first.x,first.y+1)
                first.right.parent=first
                if map[first.right.x][first.right.y]==8:
                    return first
                front.append(first.up)
                explord.append(str(first.x)+str(first.y+1))
    #left
          if first.y-1>=0 :
            if map[first.x][first.y-1]!=0 and node.ckeck(str(first.x)+str(first.y-1))==True:
                first.left=node(first.x,first.y-1)
                first.left.parent=first
                if map[first.left.x][first.left.y]==8: 
                    return first
                front.append(first.left)
                explord.append(str(first.x)+str(first.y-1))
         
    #up
          if first.x-1>=0:
            if map[first.x-1][first.y]!=0 and node.ckeck(str(first.x-1)+str(first.y))==True:
                first.up=node(first.x-1,first.y)
                first.up.parent=first
                if map[first.up.x][first.up.y]==8:
                   return first
                front.append(first.up)
                explord.append(str(first.x-1)+str(first.y))
    #down
          if first.x+1<size_x :
            if map[first.x+1][first.y]!=0 and node.ckeck(str(first.x+1)+str(first.y))==True:
                first.down=node(first.x+1,first.y)
                first.down.parent=first
                if map[first.down.x][first.down.y]==8:
                    return first
                front.append(first.down)
                explord.append(str(first.x+1)+str(first.y))
        return -2

def main():
    print(chr(27) + "[2J")
    flag=0
    explord.clear()
    front.clear()
    map=np.random.randint(0,2,size=(size_x,size_y))
    sx=random.randint(0,size_x-1)
    sy=random.randint(0,size_x-1)
    map[sx][sy]=7
    map[random.randint(0,size_x-1)][random.randint(0,size_y-1)]=8
    flag=node.solve(map,sx,sy)
    if flag!=0 and flag!=None and flag!=-2:
     print("----------------",flag.x,flag.y)
     while True:
         if flag!=0:
            if map[flag.x][flag.y]!=7 and map[flag.x][flag.y]!=8:
                map[flag.x][flag.y]=5
            flag=flag.parent
            if flag==-1 or flag==None or flag==0:
               break
    else:
      print("----------------","javab nist") 
    for r in range(size_x):
      for c in range(size_y):
        if map[r][c]==0:
            Label(root, text=chr(9608),font=("arial",15),borderwidth=5,padx=4 ).grid(row=r+20,column=c+20)
        if map[r][c]==1:
            Label(root, text=str('-'),font=("arial",18),borderwidth=5,padx=4).grid(row=r+20,column=c+20)
        if map[r][c]==5:
            Label(root, text=str('+'),font=("arial",18),borderwidth=5,padx=4 ,fg='red').grid(row=r+20,column=c+20)
        if map[r][c]==7:
            Label(root, text=str('S'),font=("arial",15),borderwidth=5,padx=4).grid(row=r+20,column=c+20)
        if map[r][c]==8:
            Label(root, text=str('G'),font=("arial",15),borderwidth=5,padx=4).grid(row=r+20,column=c+20)
         
    B = Button(root, text ="refresh",bg="red", command = main)
    B.place(x=140,y=400)
    root.mainloop()
if __name__=="__main__":
    main()
   