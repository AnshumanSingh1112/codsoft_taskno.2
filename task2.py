import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.create_widgets()

    def create_widgets(self):
        # Create and place widgets
        self.num1_label = tk.Label(self.root, text="Enter first number:")
        self.num1_label.grid(row=0, column=0, padx=10, pady=10)

        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10)

        self.num2_label = tk.Label(self.root, text="Enter second number:")
        self.num2_label.grid(row=1, column=0, padx=10, pady=10)

        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.grid(row=1, column=1, padx=10, pady=10)

        self.operation_label = tk.Label(self.root, text="Choose operation:")
        self.operation_label.grid(row=2, column=0, padx=10, pady=10)

        self.operation_var = tk.StringVar(value="add")
        self.operation_menu = tk.OptionMenu(self.root, self.operation_var, "add", "subtract", "multiply", "divide")
        self.operation_menu.grid(row=2, column=1, padx=10, pady=10)

        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = tk.Label(self.root, text="Result: ")
        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    raise ValueError("Cannot divide by zero")
                result = num1 / num2
            else:
                raise ValueError("Invalid operation")

            self.result_label.config(text=f"Result: {result}")

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
