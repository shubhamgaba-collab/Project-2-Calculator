
import tkinter as tk
from tkinter import ttk

# ---------------------------
# MAIN CALCULATOR CLASS
# ---------------------------

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator - NextHikes IT Solutions")
        self.root.geometry("380x550")
        self.root.resizable(False, False)

        self.expression = ""
        self.dark_mode = False
        self.history_list = []

        # Main frames
        self.create_display()
        self.create_buttons()
        self.create_history_panel()
        self.bind_keyboard()

        # Default theme
        self.apply_light_theme()


    # ---------------------------
    # DISPLAY SCREEN
    # ---------------------------
    def create_display(self):
        self.display = tk.Entry(self.root, font=("Arial", 24), bd=5, relief="sunken", justify="right")
        self.display.pack(fill="x", padx=10, pady=15)


    # ---------------------------
    # BUTTON SECTION
    # ---------------------------
    def create_buttons(self):
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        button_texts = [
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","-"],
            ["0",".","=","+"],
        ]

        self.btn_refs = []  # store button refs for theme changing

        for row in button_texts:
            row_frame = tk.Frame(btn_frame)
            row_frame.pack()
            
            for btn in row:
                button = tk.Button(
                    row_frame,
                    text=btn,
                    width=8,
                    height=3,
                    font=("Arial", 14),
                    command=lambda x=btn: self.on_button_click(x)
                )
                button.pack(side="left", padx=5, pady=5)
                self.btn_refs.append(button)

        # Clear Button
        clear_btn = tk.Button(btn_frame, text="C", width=34, height=2,
                             font=("Arial", 14), command=self.clear_screen)
        clear_btn.pack(pady=10)
        self.btn_refs.append(clear_btn)

        # Theme Switch Button
        theme_btn = tk.Button(btn_frame, text="Toggle Theme", width=34, height=2,
                             font=("Arial", 14), command=self.toggle_theme)
        theme_btn.pack(pady=5)
        self.btn_refs.append(theme_btn)


    # ---------------------------
    # HISTORY PANEL
    # ---------------------------
    def create_history_panel(self):
        tk.Label(self.root, text="History", font=("Arial", 14, "bold")).pack()

        self.history_box = tk.Listbox(self.root, height=6, font=("Arial", 12))
        self.history_box.pack(fill="both", padx=10, pady=5)


    # ---------------------------
    # BUTTON CLICK LOGIC
    # ---------------------------
    def on_button_click(self, value):
        if value == "=":
            self.calculate()
        else:
            self.expression += value
            self.update_screen()


    def update_screen(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)


    def clear_screen(self):
        self.expression = ""
        self.update_screen()


    # ---------------------------
    # CALCULATE RESULT
    # ---------------------------
    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.history_list.append(self.expression + " = " + result)
            self.history_box.insert(tk.END, self.history_list[-1])

            self.expression = result
            self.update_screen()

        except Exception:
            self.expression = ""
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")


    # ---------------------------
    # KEYBOARD SUPPORT
    # ---------------------------
    def bind_keyboard(self):
        self.root.bind("<Key>", self.key_handler)

    def key_handler(self, event):
        if event.char.isdigit() or event.char in "+-*/.":
            self.expression += event.char
            self.update_screen()
        elif event.keysym == "Return":
            self.calculate()
        elif event.keysym == "BackSpace":
            self.expression = self.expression[:-1]
            self.update_screen()


    # ---------------------------
    # THEME SWITCHING
    # ---------------------------
    def toggle_theme(self):
        if self.dark_mode:
            self.apply_light_theme()
        else:
            self.apply_dark_theme()

        self.dark_mode = not self.dark_mode


    def apply_dark_theme(self):
        self.root.configure(bg="#1c1c1c")
        self.display.configure(bg="#333", fg="white", insertbackground="white")

        for button in self.btn_refs:
            button.configure(bg="#444", fg="white", activebackground="#666")

        self.history_box.configure(bg="#333", fg="white")


    def apply_light_theme(self):
        self.root.configure(bg="white")
        self.display.configure(bg="white", fg="black", insertbackground="black")

        for button in self.btn_refs:
            button.configure(bg="lightgray", fg="black", activebackground="darkgray")

        self.history_box.configure(bg="white", fg="black")


# ---------------------------
# RUN THE APPLICATION
# ---------------------------
root = tk.Tk()
app = AdvancedCalculator(root)
root.mainloop()
