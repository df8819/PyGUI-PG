from ttkbootstrap import Style
from tkinter import ttk


class ThemeChooserApp:
    def __init__(self, root):
        self.root = root
        self.style = Style()
        self.root.title("Theme Chooser")

        self.create_widgets()

    def create_widgets(self):
        self.theme_menu = ttk.Combobox(self.root, state="readonly", values=self.style.theme_names())
        self.theme_menu.set(self.style.theme_use())
        self.theme_menu.pack(padx=10, pady=10)

        self.apply_theme_button = ttk.Button(self.root, text="Apply Theme", command=self.apply_theme)
        self.apply_theme_button.pack(padx=10, pady=10)

    def apply_theme(self):
        new_theme = self.theme_menu.get()
        self.style.theme_use(new_theme)


def main():
    style = Style(theme='superhero')
    root = style.master
    root.geometry("400x150")
    app = ThemeChooserApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
