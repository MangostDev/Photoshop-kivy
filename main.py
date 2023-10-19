from random import random

from PIL.Image import Image
from PIL.ImageDraw import ImageDraw
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget


class PhotoshopApp(App):
    pass


class Display(Screen):
    #txtinput = ObjectProperty(None)
    #button = ObjectProperty(None)
    #image = ObjectProperty(None)
    def loadImage(self,image):
        self.ids.image.source = image
    def sepia(self,image):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = pixels[x,y][0]
                green = pixels[x,y][1]
                blue = pixels[x,y][2]
                red1 = (red*.393) + (green*.769) + (blue*.189)
                green1 = (red *.349) + (green*.686) + (blue*.168)
                blue1 = (red*.272) + (green*.534) + (blue*.131)
                pixels[x,y] = [red1,green1,blue1]

        img.save(image + "sepia.png")
        self.loadImage(self,image + "sepia.png")

    def greyscale(self,image):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                lighting = (pixels[x,y][0] + pixels[x,y][1] + pixels[x,y][2])//3
                pixels[x,y] = [lighting, lighting, lighting]

        img.save(image + "greyscale.png")
        self.loadImage(self, image + "sepia.png")

    def inverse(self, image):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = 255 - pixels[x,y][0]
                green = 255 - pixels[x,y][1]
                blue = 255 - pixels[x,y][2]
                pixels[x,y] = [red,green,blue]

    def pointillism(self, image):
        img = Image.open(image)
        pixels = img.load()
        canvas = Image.new("RGB", (img.size[0], img.size[1]),'white')
        for i in range(5000):
            x = random.randint(0,img.size[0]-1)
            y = random.randint(0,img.size[1]-1)
            size = random.randint(3,5)
            ellipsebox = [(x,y),(x+size,y+size)]
            draw = ImageDraw.Draw(canvas)
            draw.ellipse(ellipsebox, fill=(pixels[x,y][0],pixels[x,y][1],pixels[x,y][2]))
            del draw

        canvas.save(image + ' pointillism.png')

    #def on_touch_down(self, touch):
        #print("\nMouse Button Pressed")
    #    coords = touch.pos
    #   print("x coordinate: " + str(int(coords[0])) + " y coordinate: " + str(int(coords[1])))

    #def on_touch_move(self, touch):
        #print("\nMouse Moving")
        #coords = touch.pos
        #print("x coordinate: " + str(int(coords[0])) + " y coordinate: " + str(int(coords[1])))

    #def on_touch_up(self, touch):
    #    print("\nMouse Button Released")
    #    coords = touch.pos
    #    print("x coordinate: " + str(int(coords[0])) + " y coordinate: " + str(int(coords[1])))







PhotoshopApp().run()