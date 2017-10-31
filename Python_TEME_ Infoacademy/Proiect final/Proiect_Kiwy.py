# Proiect final - GUI
# Aplicarea cunostintelor din cele 8 sedinte de Python
# Oana Popa 21/11/2015

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.popup import Popup
import sys


class CustomLayout(FloatLayout):

    def __init__(self, **kwargs):
        # rewrite the __init__ with <<super>>
        super(CustomLayout, self).__init__(**kwargs)
        # add a background
        self.backg = Image(source="fundal.jpg")
        self.backg.opacity = 0.5
        self.add_widget(self.backg)
        # add the layout0 as child of the background
        self.layout0 = FloatLayout(size_hint=(None, None), size=(600, 500), padding=200)
        self.backg.add_widget(self.layout0)
        # add the sound widget and options
        self.sound = SoundLoader.load('JO_-_09_-_Fortitude.ogg')
        self.sound.play()
        self.sound.loop = True
        self.sound.volume = 0.5
        self.Menu(None)

    def Menu(self, Buton):
        # clear all the widgets from the page
        self.layout0.clear_widgets()
        # add the widget Carusel
        self.button1 = Button(text="Carusel", bold=True, background_color=(0, 0, 1, 1))
        self.button1.pos = (300, 380)
        self.button1.size_hint = (0.3, 0.1)
        self.button1.opacity = 0.7
        self.layout0.add_widget(self.button1)
        # add the widget Optiuni
        self.button2 = Button(text="Optiuni", bold=True, background_color=(0, 0, 1, 1))
        self.button2.pos = (300, 300)
        self.button2.size_hint = (0.3, 0.1)
        self.button2.opacity = 0.7
        self.layout0.add_widget(self.button2)
        # add the widget About
        self.button3 = Button(text="About", bold=True, background_color=(0, 0, 1, 1))
        self.button3.pos = (300, 220)
        self.button3.size_hint = (0.3, 0.1)
        self.button3.opacity = 0.7
        self.layout0.add_widget(self.button3)
        # add the widget About
        self.button4 = Button(text="Iesi", bold=True, background_color=(0, 0, 1, 1))
        self.button4.pos = (300, 140)
        self.button4.size_hint = (0.3, 0.1)
        self.button4.opacity = 0.7
        self.layout0.add_widget(self.button4)
        # bind the buttons with respective methods
        self.button1.bind(on_press=self.CatreCarusel)
        self.button2.bind(on_press=self.Optiuni)
        self.button3.bind(on_press=self.About)
        self.button4.bind(on_press=self.Iesi)

    def CatreCarusel(self, Buton):
        # clear all the widgets from the page
        self.layout0.clear_widgets()
        # define the carousel
        carousel = Carousel(direction='right')
        carousel.anim_move_duration = 1
        carousel.padding = 40
        carousel.loop = True
        carousel.size_hint = (0.7, 0.7)
        carousel.pos = (200, 120)
        self.layout0.add_widget(carousel)
        # create and add the Image widgets to the carousel
        image1 = Image(source="nature1.jpg")
        carousel.add_widget(image1)
        image2 = Image(source="nature2.jpg")
        carousel.add_widget(image2)
        image3 = Image(source="nature3.jpg")
        carousel.add_widget(image3)
        image4 = Image(source="nature4.jpg")
        carousel.add_widget(image4)
        label_final = Label(text="Am ajuns la finalul listei!", font_size=30)
        carousel.add_widget(label_final)
        # add the back button
        back_button = Button(text="Inapoi", bold=True, background_color=(0, 0, 1, 1))
        back_button.pos = (200, 100)
        back_button.size_hint = (0.7, 0.1)
        back_button.opacity = 0.7
        self.layout0.add_widget(back_button)
        # bind the back_button with the menu
        back_button.bind(on_press=self.Menu)

        return carousel

    def Optiuni(self, Buton):
        # clear all the widgets from the page
        self.layout0.clear_widgets()
        # create the switch widget
        self.switch1 = Switch(text="Muzica")
        self.switch1.active = True
        self.switch1.size_hint = (0.3, 0.2)
        self.switch1.pos = (300, 360)
        self.layout0.add_widget(self.switch1)
        # create the Label widget
        self.arata_volum = Label(text="volum: 50")
        self.arata_volum.size_hint = (0.3, 0.1)
        self.arata_volum.pos = (300, 260)
        self.layout0.add_widget(self.arata_volum)
        # create the Slider widget
        self.slide_muzica = Slider(min=0, max=100, value=50)
        self.slide_muzica.step = 5
        self.slide_muzica.size_hint = (0.3, 0.1)
        self.slide_muzica.pos = (300, 180)
        self.slide_muzica.orientation = "horizontal"
        self.layout0.add_widget(self.slide_muzica)
        # add the back button
        back_button = Button(text="Inapoi", bold=True, background_color=(0, 0, 1, 1))
        back_button.pos = (300, 120)
        back_button.size_hint = (0.3, 0.1)
        back_button.opacity = 0.7
        self.layout0.add_widget(back_button)
        # bind the button, slider  with respective methods
        self.switch1.bind(active=self.dezactiveaza_volum)
        self.slide_muzica.bind(value=self.valoare_volum)
        back_button.bind(on_press=self.Menu)

    def About(self, Buton):
        # add the close button
        close = Button(text="Inapoi", background_color=(0, 0, 1, 1))
        close.size_hint = (1, 0.1)
        # create the Label widget
        eticheta = Label(text="Multumiri Infoacademy", bold=True, font_size=24)
        # create the second layout
        layout1 = BoxLayout()
        layout1.orientation = "vertical"
        layout1.padding = 40
        # add the widgets to the second layout
        layout1.add_widget(eticheta)
        layout1.add_widget(close)
        # create a popup widget
        self.popup = Popup()
        self.popup.background = "fundal4_tema.jpg"
        self.popup.size_hint = (None, None)
        self.popup.size = (400, 400)
        self.popup.title = 'Cine a creat aplicatia?'
        self.popup.content = layout1
        self.popup.open()
        # bind the button with respective method
        close.bind(on_press=self.inchide_popup)

    def Iesi(self, Buton):
        # exit using the sys module
        sys.exit()

    def valoare_volum(self, x, y):
        # shows the volume
        self.arata_volum.text = "volum: " + str(int(self.slide_muzica.value))
        self.sound.volume = self.slide_muzica.value/100

    def dezactiveaza_volum(self, x, y):
        # for disabling the slider
        if not self.switch1.active:
            self.slide_muzica.disabled = True
            self.sound.stop()
        else:
            self.slide_muzica.disabled = False
            self.slide_muzica.value = 0
            self.sound.play()

        self.sound.volume = 0
        return self.layout0

    def inchide_popup(self, Buton):
        self.popup.dismiss()


class CarouselApp(App):

    def build(self):
        self.icon = "python1.ico"
        return CustomLayout()

if __name__ == '__main__':
    CarouselApp().run()
