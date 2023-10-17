from kivy.app import App
from kivy.uix.screenmanager import Screen


class PhotoshopApp(App):
    pass


class Display(Screen):
    def loadImage(self,image):
        self.ids.image.source = image
    def sepia(self,image):




PhotoshopApp().run()