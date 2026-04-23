# This is a sample Python script.
import tkinter as tk
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

UNITCONVERTER = {
            "km": 1000,
            "m": 1,
            "cm": 0.01,
            "mm": 0.001
        }

def convert():

    try:
        value = float(entry.get())

        from_unit = from_var.get()
        to_unit = To_var.get()



        meters = value * UNITCONVERTER[from_unit]
        result = meters / UNITCONVERTER[to_unit]

        result_label.config(text = f"Convert {from_unit} to {to_unit} = {result}")

    except ValueError:
        result_label.config(text = "Please enter a valid value")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Unit Converter")

    # unit to convert
    from_frame = tk.LabelFrame(root, text="Unit To Convert", padx=10, pady=10)
    from_frame.pack(padx=20, pady=10, fill="x")

    from_var = tk.StringVar()
    from_var.set("km")


    #for unit in units:
     #   button = tk.Radiobutton(from_frame, text=unit, variable=from_var, value=unit)
      #  button.pack(anchor=tk.W)

    # converted unit
    To_frame = tk.LabelFrame(root, text="Unit To Convert", padx=10, pady=10)
    To_frame.pack(padx=20, pady=10, fill="x")

    To_var = tk.StringVar()
    To_var.set("m")

    # entry frame
    entry_frame = tk.Frame(root)
    entry_frame.pack(pady=10)

    tk.Label(entry_frame, text="Please enter value").pack(side="left", padx=5)
    entry = tk.Entry(entry_frame, width=15)
    entry.pack(side="left")

    # initialize button
    for unit, cm in UNITCONVERTER.items():
        frombutton = tk.Radiobutton(from_frame, text=unit, variable=from_var, value=unit)
        frombutton.pack(anchor=tk.W)
        Tobutton = tk.Radiobutton(To_frame, text=unit, variable=To_var, value=unit)
        Tobutton.pack(anchor=tk.W)

    tk.Button(root, text="Convertion", command=convert, bg="lightblue", width=15).pack()

    result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
    result_label.pack(pady=10)

    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
