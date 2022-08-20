from cake import Cake
import tkinter
import math
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

gui = customtkinter.CTk()
gui.geometry("445x420")
gui.title("Layer cake calculator")

# FRAMES CONFIGURATION

frame_left = customtkinter.CTkFrame(master=gui,
                                    width=180,
                                    corner_radius=0)
frame_left.grid(row=0, column=0, sticky="nswe")

frame_right = customtkinter.CTkFrame(master=gui,
                                     width=180)
frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

# WELCOME label

welcome_label = customtkinter.CTkLabel(master=frame_left,
                                       text="Layer cake calculator",
                                       text_font=("Arial", 12)).grid(row=1,
                                                                     column=0,
                                                                     pady=10,
                                                                     padx=10)

# HOW MANY PORTIONS entry
portion_int = customtkinter.IntVar()
portion_label = customtkinter.CTkLabel(master=frame_left,
                                       text="How many portions?").grid(row=2, column=0)

portion_entry = customtkinter.CTkEntry(master=frame_left, width=100, textvariable=portion_int)
portion_entry.grid(row=3, column=0, padx=20, pady=5)

# PRICE entry
price_int = customtkinter.IntVar()
price_label = customtkinter.CTkLabel(master=frame_left, text="Price per person?").grid(row=4, column=0)

price_entry = customtkinter.CTkEntry(master=frame_left, width=100, textvariable=price_int)
price_entry.grid(row=5, column=0, padx=20, pady=5)

# WHICH FORM label

form_label = customtkinter.CTkLabel(master=frame_left, text="Which form?").grid(row=6,
                                                                                column=0)
form_combobox = customtkinter.CTkComboBox(master=frame_left,
                                          width=100,
                                          values=["Round", "Square", "Rectangle"])

form_combobox.grid(row=7,
                   column=0,
                   pady=5,
                   padx=20)

# MORE INFO

more_info_label = customtkinter.CTkLabel(master=frame_left, text="More info:").grid(row=8,
                                                                                    column=0,
                                                                                    pady=5)

# GLUTENFREE checkbox

gf_bool = customtkinter.BooleanVar()
gf_check = customtkinter.CTkCheckBox(master=frame_left,
                                     variable=gf_bool,
                                     text="Gluten free?")

gf_check.deselect()
gf_check.grid(row=9, column=0, sticky="w", padx=50, pady=8)

# BOX INCLUDED checkbox

box_bool = customtkinter.BooleanVar()
box_check = customtkinter.CTkCheckBox(master=frame_left,
                                      variable=box_bool,
                                      text="Box included?")
box_check.deselect()
box_check.grid(row=10, column=0, sticky="w", padx=50, pady=8)

# RIGHT FRAME
# OUTPUT WIDGETS


output_label = customtkinter.CTkLabel(master=frame_right,
                                      text="Output",
                                      text_font=("Arial", 12)).grid(row=1,
                                                                    column=0)

# Price output widgets

price_output_label = customtkinter.CTkLabel(master=frame_right, text="Price: ").grid(row=2,
                                                                                     padx=20,
                                                                                     pady=5, column=0)

price_frame = customtkinter.CTkFrame(master=frame_right,
                                     width=100)
price_frame.grid(row=3, column=0, sticky="s")

price_output_entry = customtkinter.CTkEntry(master=price_frame, width=50)
price_output_entry.grid(row=3,
                        column=0)

zl_label = customtkinter.CTkLabel(master=price_frame, width=10, text="zł").grid(row=3, column=1, padx=8, pady=5, )

# Cake size outputs

cake_size_output_label = customtkinter.CTkLabel(master=frame_right, text="Cake size")
cake_size_output_label.grid(row=4,
                            column=0,
                            pady=5)

layers_frame = customtkinter.CTkFrame(master=frame_right,
                                      width=100)
layers_frame.grid(row=5, column=0, sticky="s")

layer_1_label = customtkinter.CTkLabel(master=layers_frame, width=30, text="First layer:")
layer_1_label.grid(row=5,
                   column=0,
                   padx=8, pady=5)

layer_1_entry = customtkinter.CTkEntry(master=layers_frame, width=60)
layer_1_entry.grid(row=5,
                   column=1,
                   padx=5)
cm_1_label = customtkinter.CTkLabel(master=layers_frame,
                                    width=20,
                                    text="cm")
cm_1_label.grid(row=5,
                column=2,
                padx=5, pady=5,
                sticky="w")

layer_2_label = customtkinter.CTkLabel(master=layers_frame, width=30, text="Second layer:")
layer_2_label.grid(row=6,
                   column=0,
                   padx=8, pady=5)
layer_2_entry = customtkinter.CTkEntry(master=layers_frame, width=60)
layer_2_entry.grid(row=6,
                   column=1,
                   padx=5)

cm_label_2 = customtkinter.CTkLabel(master=layers_frame,
                                    width=20,
                                    text="cm")
cm_label_2.grid(row=6,
                column=2,
                padx=5, pady=5,
                sticky="w")

layer_3_label = customtkinter.CTkLabel(master=layers_frame, width=30, text="Third layer:")
layer_3_label.grid(row=7,
                   column=0,
                   padx=8, pady=5)
layer_3_entry = customtkinter.CTkEntry(master=layers_frame, width=60)
layer_3_entry.grid(row=7,
                   column=1,
                   padx=5)

cm_label_3 = customtkinter.CTkLabel(master=layers_frame,
                                    width=20,
                                    text="cm")
cm_label_3.grid(row=7,
                column=2,
                padx=5, pady=5,
                sticky="w")

error_output = ""

box_outputs = []  # list of outputs related with box price information (needed for "clear_func")

buttons_filled = False

def clear_button_func():
    output_entries = [price_output_entry, layer_1_entry, layer_2_entry, layer_3_entry]
    for output in output_entries:
        output.delete(0, tkinter.END)

    if box_outputs:
        for box_output in box_outputs:
            box_output.destroy()

    if error_output:
        error_output.destroy()


def enter_button_func():
    global buttons_filled
    global error_output

    if buttons_filled:
        clear_button_func()

    try:
        your_cake = Cake(int(portion_entry.get()),
                         int(price_entry.get()),
                         box_check.get(),
                         gf_check.get())
        assert int(portion_entry.get()) <= 75
    except ValueError:
        error_output = customtkinter.CTkLabel(master=frame_right, text_color="brown3", text="Please insert integer")
        error_output.grid(row=13,
                        column=0,
                        pady=5,
                        sticky="s")
    except AssertionError:
        error_output = customtkinter.CTkLabel(master=frame_right, text_color="brown3", text="75 portions is max")
        error_output.grid(row=13,
                        column=0,
                        pady=5,
                        sticky="s")


    price_output_entry.insert(0, your_cake.price_calc()[0])
    if your_cake.price_calc()[1] != 0:  # if price includes box
        box_output_label = customtkinter.CTkLabel(master=frame_right, text="Price includes price of box:")
        box_output_label.grid(row=13,
                              column=0,
                              pady=5,
                              sticky="s")
        box_output_entry = customtkinter.CTkEntry(master=frame_right)
        box_output_entry.grid(row=14,
                              column=0,
                              pady=5,
                              sticky="s")
        box_output_entry.insert(0, your_cake.price_calc()[1])
        box_outputs.append(box_output_entry)
        box_outputs.append(box_output_label)

    if form_combobox.get() == "Round":
        cake_size_output_label = customtkinter.CTkLabel(master=frame_right, text="Size of diameter(s):")
        cake_size_output_label.grid(row=4,
                                    column=0,
                                    pady=5)
        layer_1_entry.insert(0, your_cake.round_calc()[0])
        layer_2_entry.insert(0, your_cake.round_calc()[1])
        layer_3_entry.insert(0, your_cake.round_calc()[2])


    elif form_combobox.get() == "Square" or "Rectangle":
        cake_size_output_label = customtkinter.CTkLabel(master=frame_right, text="Size of side(s):")
        cake_size_output_label.grid(row=4,
                                    column=0,
                                    pady=5)
        if form_combobox.get() == "Square":
            layer_1_entry.insert(0, your_cake.square_calc()[0])
            layer_2_entry.insert(0, your_cake.square_calc()[1])
            layer_3_entry.insert(0, your_cake.square_calc()[2])
        else:
            layer_1_entry.insert(0, your_cake.rectangle_calc()[0])
            layer_2_entry.insert(0, your_cake.rectangle_calc()[1])
            layer_3_entry.insert(0, your_cake.rectangle_calc()[2])
    buttons_filled = True
    return buttons_filled


# BUTTON
enter_button = customtkinter.CTkButton(master=frame_left, width=100, text="Enter", command=enter_button_func).grid(
    row=11, column=0, padx=20, pady=15)
clear_button = customtkinter.CTkButton(master=frame_right, width=20, text="Clear", command=clear_button_func)
clear_button.place(x=120, y=340)
gui.bind('<Return>', lambda event: enter_button_func())  # When you press enter key

gui.mainloop()
# python test.py
