from random import randint

from PIL import Image
from PIL import ImageDraw
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
                pixels[x,y] = (int(red1),int(green1),int(blue1))

        img.save(image + "sepia.png")
        self.loadImage(image + "sepia.png")

    def greyscale(self,image):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                lighting = (pixels[x,y][0] + pixels[x,y][1] + pixels[x,y][2])//3
                pixels[x,y] = (int(lighting), int(lighting), int(lighting))

        img.save(image + "greyscale.png")
        self.loadImage(image + "greyscale.png")

    def inverse(self, image):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = 255 - pixels[x,y][0]
                green = 255 - pixels[x,y][1]
                blue = 255 - pixels[x,y][2]
                pixels[x,y] = (int(red),int(green),int(blue))

        img.save(image + "inverted.png")
        self.loadImage(image + "inverted.png")

    def pointillism(self, image):
        img = Image.open(image)
        pixels = img.load()
        canvas = Image.new("RGB", (img.size[0], img.size[1]),'white')
        for i in range(5000):
            x = randint(0,img.size[0]-1)
            y = randint(0,img.size[1]-1)
            size = randint(3,5)
            ellipsebox = [(x,y),(x+size,y+size)]
            draw = ImageDraw.Draw(canvas)
            draw.ellipse(ellipsebox, fill=(pixels[x,y][0],pixels[x,y][1],pixels[x,y][2]))
            del draw

        canvas.save(image + ' pointillism.png')
        self.loadImage(image + ' pointillism.png')

    def line_drawing(self,image):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if x != img.size[0]-1:
                    if pixels[x+1,y][0] > int(pixels[x,y][0]) + 5 or pixels[x+1,y][0] < int(pixels[x,y][0] - 5):
                        isEdge = True
                    elif pixels[x+1,y][1] > int(pixels[x,y][1]) + 5 or pixels[x+1,y][1] < int(pixels[x,y][1] - 5):
                        isEdge = True
                    elif pixels[x+1,y][2] > int(pixels[x,y][2]) + 5 or pixels[x+1,y][2] < int(pixels[x,y][2] - 5):
                        isEdge = True
                    else:
                        isEdge = False
                    if isEdge:
                        pixels[x,y] = (0,0,0)
                    else:
                        pixels[x,y] = (255,255,255)

        img.save(image + "outline.png")
        self.loadImage(image + "outline.png")


    def pixelate(self,image):
        img = Image.open(image)
        pixels = img.load()
        for y in range(1, img.size[1], 10):
            for x in range(1, img.size[0], 10):
                red = pixels[x,y][0]
                green = pixels[x,y][1]
                blue = pixels[x,y][2]
                for y2 in range(y, y+10):
                    for x2 in range(x, x+10):
                        if y2 + 1 <= img.size[1] and x2 + 1 <= img.size[0]:
                            pixels[x2,y2] = (red,green,blue)

        img.save(image + 'pixelated.png')
        self.loadImage(image + 'pixelated.png')

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