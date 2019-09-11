'''
Name - Login App
File name - LoginApp.py
Author - Mandeep Dhaliwal
Description - Python program for creating an application using KIVY for displaying a Login form  and background .
              click on submit button to remove login form and click again on image to display login form.
              Login is not validated.
'''

# Importing kivy modules

from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import *
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.layout import Layout #used for giving layout to childrens using widget

#Root or base widget containing all other widgets
class RootWidget(BoxLayout):
    pass

#Using canvas for background of the app
class CustomLayout(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(CustomLayout, self).__init__(**kwargs)

        with self.canvas.before:
            Color(1, 1, 1, 1)  # white; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    #size and position canvas for window size changes
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

#Main class of the application
class MainApp(App):
    
    b=BoxLayout(orientation='vertical' ,size=(700,500),spacing=10)       # BoxLayout containing Login Form
    
    # Text Input for username
    
    t1=TextInput(multiline=False,hint_text='Username',font_size=100,
              size_hint_y=None,
              height=200,use_bubble=True,background_color=(1,1,1,0.5))
    
    # Text input for password
    
    t2=TextInput(multiline=False,hint_text='Password',font_size=100,
              size_hint_y=None,
              height=200,use_bubble=True,background_color=(1,1,1,0.5),password=True)
    
    # Form submit button
    
    btn=Button(text='SUBMIT', font_size=40 , bold=True, background_color=(0,1,1,1))
    
    def __init__(self,**kwargs):
        super(MainApp,self).__init__(**kwargs)# to use build function and not cover or stop any important functionality of class
        self.btn.on_press=self.ch
    
    # Positioning Login form to center
    
    def upd(self,obj ,value):
        self.b.pos=(obj.center_x-350,obj.center_y-250)
        
    # similar to above
    
    def upd2(self,obj ):
        self.b.pos=(obj.center_x,obj.center_y)
        
    # Called on press of 'submit' button , removes form and display only background
    
    def ch(self):
        self.b.clear_widgets()
        self.b.add_widget(Button(text="",on_press=self.bck,background_color=(1,1,1,0)))
    
    #Called on click on the background to re-display the form     
    
    def bck(self,instance):
        self.b.clear_widgets()
        self.b.add_widget(self.t1)
        self.b.add_widget(self.t2)
        self.b.add_widget(self.btn)
    
    #Build function to execute root widget
    
    def build(self):
        
        wgt=Widget()
        root = CustomLayout()    
        #self.upd2(root)
        root.bind(size=self.upd)
        #self.b.bind(on_touch_move=self.bck)
        self.b.add_widget(self.t1)
        self.b.add_widget(self.t2)
        self.b.add_widget(self.btn)
        wgt.add_widget(self.b)
        root.add_widget(Image(source='panda.jpg',anim_delay=0.09))
        root.add_widget(wgt)
        
        return root

if __name__ == '__main__':
    MainApp().run()  # Run Application 