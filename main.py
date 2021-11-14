#!/usr/bin/env python
#_*_coding:utf-8_*_
import tkinter as tk
import pygame
from PIL import Image,ImageTk
import random
import numpy as np
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class MainWindow():
    _map = []
    _gameSize = 10
    _iconCount = _gameSize*_gameSize/4
    _iconWidth = 70
    _iconHeight = 70
    def __init__(self):
        #crete window
        self.window = tk.Tk()
        self.window.minsize(800,750)
        self.window.title("连连看小游戏-by Xuejiao")
        self.windowCenter(800,750)
        self.gameWidth = 800
        self.gameHeight = 750
        self.margin = 25
        self._icons=[]
        #
        self.addComponents()
#
        pygame.mixer.init()
        self.playMusic("audio/bg_music.mp3")

        #----
        self.background_im = False
        self.drawBackground()
        self.extractSmallIconList()
        self.window.mainloop()

    def playMusic(self,music,volume=0.5):
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play()

    def stopMusic(self):
        pygame.mixer.music.stop()

    '''0,1,2,...,24'''
    def initMap(self):
        records=[]
        for i in range(0,int(self._iconCount)):
            for j in range(0,4):
                records.append(i)
        random.shuffle(records)#匀速随机排序
        self._map = np.array(records).reshape(10,10)

    def drawBackground(self):
        self.background_im=ImageTk.PhotoImage(file="images/bg.png")
        self.canvas.create_image((0,0),anchor='nw',image=self.background_im)
    def windowCenter(self,width,height):
        screenwidth=self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        size = '%dx%d+%d+%d'%(width,height,screenwidth/2-width/2,screenheight/2-height/2)
        self.window.geometry(size)

    def addComponents(self):
        self.menubar=tk.Menu(self.window,bg="lightgrey",fg="black")
        self.file_menu = tk.Menu(self.menubar,bg='lightgrey',fg='black')
        self.file_menu.add_command(label='新游戏',command=self.file_menu_clicked,accelerator='Ctrl+N')
        self.menubar.add_cascade(label="游戏",menu=self.file_menu)
        self.window.configure(menu=self.menubar)
        self.canvas=tk.Canvas(self.window,bg="white",width=self.gameWidth,height=self.gameHeight)
        self.canvas.pack()

    def file_menu_clicked(self):
        self.stopMusic()
        self.initMap()
        print("游戏地图")
        print(self._map)
        self.drawMap()

    '''提取小头像图片到Icons'''
    def extractSmallIconList(self):
        imageSource = Image.open("images/animals.png")
        for index in range(0,int(self._iconCount)):
            region=imageSource.crop((index*self._iconWidth,0,(index+1)*self._iconWidth,self._iconHeight))
            self._icons.append(ImageTk.PhotoImage(region))

    def drawMap(self):
        for row in range(0,self._gameSize):
            for column in range(0,self._gameSize):
                x,y = self.getOriginCoordinate(row,column)
                self.canvas.create_image((x,y),image=self._icons[self._map[row][column]],anchor='nw')

    def getX(self,row):
        return self.margin+row*self._iconWidth

    def getY(self,column):
        return self.margin+column*self._iconHeight

    def getOriginCoordinate(self,row,column):
        return self.getX(row),self.getY(column)

    def getGamePoint(self,x,y):
        for row in range(0,self._gameSize):
            x1 = self.getX(row)
            x2 = self.getX(row+1)
            if x>=x1 and x<x2:
                point_row = row

        for column in range(0,self._gameSize):
            j1 = self.getY(column)
            j2 = self.getY(column+1)
            if y>=j1 and y<j2:
                point_column = column
        return Point(point_row, point_column)
        # my_frame=tk.Frame(self.window)
        # my_frame.pack(side=tk.TOP)
        #
        # my_button = tk.Button(my_frame,text="点我",command=self.button_clicked)
        # my_button.pack(side=tk.LEFT)
        #
        # my_canvas = tk.Canvas(my_frame,bg="white")
        # my_canvas.create_rectangle(50,50,150,150,outline='red',fill='blue',width=5)
        # my_canvas.pack(side=tk.RIGHT)
        #
        # my_apple=tk.Checkbutton(my_frame,text='苹果')
        # my_apple.pack(side=tk.TOP)
        #
        # name = tk.Label(my_frame,text="姓名")
        # name.pack(side=tk.LEFT)
        # name_value = tk.Entry(my_frame,bd=5)
        # name_value.pack(side=tk.RIGHT)
    def button_clicked(self):
        print("Button clicked")
class Point():
    def __init__(self,row,column):
        self.row = row
        self.column = column

    def isEqual(self,point):
        if self.row == point.row and self.column==point.column:
            return True
        else:
            return False
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MainWindow()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
