from ttkbootstrap import Style
from tkinter import ttk
import tkinter as tk
import io
import sys


class PythonPlaygroundApp:
    def __init__(self, root):
        self.root = root
        self.style = Style()
        self.root.title("Python Playground")

        self.create_widgets()

    def create_widgets(self):
        # Command Selection Menu
        self.command_menu = ttk.Combobox(self.root, state="readonly", values=[
            "Zen of Python",
            "List Comprehension Example",
            "Hello World",
            # Add more commands here
        ])
        self.command_menu.set("Select a command")
        self.command_menu.grid(row=0, column=0, padx=10, pady=10)

        # Execute Button
        self.execute_button = ttk.Button(self.root, text="Execute", command=self.execute_command, style='success.TButton')
        self.execute_button.grid(row=0, column=1, padx=10, pady=10)

        # Clear Button
        self.clear_button = ttk.Button(self.root, text="Clear", command=self.clear_output, style='danger.TButton')
        self.clear_button.grid(row=0, column=2, padx=10, pady=10)

        # Output Area
        self.output_area = tk.Text(self.root, height=15, width=50)
        self.output_area.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Theme Selection Menu
        self.theme_menu = ttk.Combobox(self.root, state="readonly", values=self.style.theme_names())
        self.theme_menu.set(self.style.theme_use())
        self.theme_menu.grid(row=2, column=0, padx=10, pady=10)

        # Apply Theme Button
        self.apply_theme_button = ttk.Button(self.root, text="Apply Theme", command=self.apply_theme, style='info.TButton')
        self.apply_theme_button.grid(row=2, column=1, padx=10, pady=10)

    def execute_command(self):
        # Get the selected command
        command = self.command_menu.get()

        # Dictionary mapping commands to functions
        commands = {
            "Zen of Python": self.show_zen_of_python,
            "List Comprehension Example": self.list_comprehension_example,
            "Hello World": self.hello_world,
            # Add more commands and corresponding methods here
        }

        # Clear the output area
        self.clear_output()

        # Execute the corresponding method
        if command in commands:
            commands[command]()

    def clear_output(self):
        self.output_area.delete(1.0, tk.END)

    def show_zen_of_python(self):
        # Capture the Zen of Python using StringIO
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        import this
        sys.stdout = old_stdout

        # Display in the output_area
        self.output_area.insert(tk.END, new_stdout.getvalue())

    def list_comprehension_example(self):
        # Example of a list comprehension
        example = [x ** 2 for x in range(10)]
        self.output_area.insert(tk.END, str(example))

    def hello_world(self):
        # Hello World example
        self.output_area.insert(tk.END, "Hello, World!")

    def apply_theme(self):
        new_theme = self.theme_menu.get()
        self.style.theme_use(new_theme)


def main():
    style = Style(theme='cosmo')  # Initialize with a default theme
    root = style.master
    app = PythonPlaygroundApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
