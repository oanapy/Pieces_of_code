# Exersarea lucrului cu kivy
# Reprezinta aplicarea cunostintelor din sedinta 7 a cursului Python 007
# Oana Popa 15/11/15

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class LoginScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20
        self.button1 = Button(text='Am plecat')
        self.button1.size_hint_x = 0.3
        self.add_widget(self.button1)
        self.button1.background_color = (0, 0, 1, 1)
        self.button2 = Button(text='Am venit')
        self.button2.size_hint_x = 0.3
        self.add_widget(self.button2)
        self.button2.background_color = (0, 0, 1, 1)
        self.button1.bind(on_press=self.Ruleaza_la_activare_b1)
        self.button2.bind(on_press=self.Ruleaza_la_activare_b2)
        self.label1 = Label(text="Press the button!")
        self.add_widget(self.label1)

    def Ruleaza_la_activare_b1(self, event):
        print self.button1.text

    def Ruleaza_la_activare_b2(self, event):
        print self.button2.text


class MyFirstAppApp(App):

    def build(self):
        x = LoginScreen()
        return x


if __name__ == '__main__':
    MyFirstAppApp().run()

