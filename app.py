import flet as ft

class MyApp(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        self.button = ft.ElevatedButton(text="Click Me", on_click=self.on_button_click)
        return self.button

    def on_button_click(self, e):
        self.button.text = "Button Clicked!"
        self.update()
    
    def main(self, page):
        page.add(self)
        
    def run(self):
        ft.app(target=self.main)

if __name__ == '__main__':
    MyApp().run()  # تشغيل main مباشرة
