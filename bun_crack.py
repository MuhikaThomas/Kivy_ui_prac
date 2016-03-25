'''
mossein king
'''

import kivy

from kivy.app import App
from kivy.uix.progressbar import ProgressBar # Loading Bar in kivy
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.checkbox import CheckBox # check boxes
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
from kivy.lang import Builder # kivy lang

Builder.load_string('''
<customlayout>
    canvas.before:
        BorderImage:
            border: 10, 10, 10, 10
            texture: self.background_image.texture
            pos: self.pos
            size: self.size                 
                    ''')
#creating a background layout
class customlayout(GridLayout):
    background_image = ObjectProperty(Image(source='safricom-31.jpg', anim_delay=.1))
    #code

class bundles_crack(App):
    title='Bundles Crack' # window tittle
    
    def build(self):
        #Window.clearcolor = (0, 0, 0, 1)
        Window.size = (640, 387) # sizing kivy windows

        root = customlayout(rows=6, cols=1, size_hint=(1, 1)) # from kivy lang class for background
        img1 = Image(source ='safcom.png',size_hint=(1, None)) # Adding images in kivy app
        row1 = GridLayout(rows=1, cols=1, size_hint=(1, None))
        row1.add_widget(img1)
        
        row2 = GridLayout(rows=4, cols=2, size_hint=(1, None))
        #check boxes
        btn1 = CheckBox(size_hint=(None, None), height=20, color=[0, 128, 0, 1])
        lblchk1= Label(text='[b]500mb[/b]', markup=True, color=[0, 0, 0, 1], size_hint=(None, None), height=20)
        btn2 = CheckBox(size_hint=(None, None), height=20)
        lblchk2 = Label(text='[b]2gb[/b]',markup=True, color=[0, 0, 0, 1], size_hint=(None, None), height=20)
        btn3 = CheckBox(size_hint=(None, None), height=20)
        lblchk3 = Label(text='[b]4gb[/b]',markup=True, color=[0, 0, 0, 1], size_hint=(None, None), height=20)
        btn4 = CheckBox(size_hint=(None, None), height=20)
        lblchk4 = Label(text='[b]8gb[/b]',markup=True, color=[0, 0, 0, 1], size_hint=(None, None), height=20)
        row2.add_widget(btn1)
        row2.add_widget(lblchk1)
        row2.add_widget(btn2)
        row2.add_widget(lblchk2)
        row2.add_widget(btn3)
        row2.add_widget(lblchk3)
        row2.add_widget(btn4)
        row2.add_widget(lblchk4)
        
        row3 = GridLayout(rows=1, cols=2, size_hint=(1, None))
        lbl1 = Label(text='  [b]PHONE NUMBER[/b]',markup=True, color=[0, 0, 0, 1], size_hint=(0.3, None), height=30, halign='left', valign='middle')
        lbl1.bind(size=lbl1.setter('text_size'))
        txt1 = TextInput(multiline=False, size_hint=(0.7, None), height=30)
        row3.add_widget(lbl1)
        row3.add_widget(txt1)
        
        row4 = GridLayout(rows=1, cols=3)
        lbbl = Label(size_hint=(0.3, None), height=40)
        lbbbl= Label(size_hint=(0.3, None), height=40)
        btn = Button(text='Generate', color=[0, 128, 0, 1], size_hint=(0.4, None), height=40, halign='left')
        row4.add_widget(lbbl)
        row4.add_widget(btn)
        row4.add_widget(lbbbl)
        
        # loading bar in kivy
        pb = ProgressBar(max=200)
        pb.value=40
        
        row5 = Label(text=' Cytech@ 2016 computer solutions', size_hint=(1, None), height=20, halign='right')
        row5.bind(size=row5.setter('text_size'))#binding text in label helps in alignment
        
        root.add_widget(row1)
        root.add_widget(row2)
        root.add_widget(row3)
        root.add_widget(row4)
        root.add_widget(pb)
        root.add_widget(row5)
        
        return root
    
if __name__ == '__main__':
    bundles_crack().run()
    
