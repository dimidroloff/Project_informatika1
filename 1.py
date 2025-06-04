from tkinter import *
from tkinter import ttk, messagebox
from math import pi
from tkinter import PhotoImage
from PIL import Image, ImageTk  # Нужно установить Pillow: pip install pillow
import ttkbootstrap as tb

from tkinter import messagebox

def show_about():
    messagebox.showinfo(
        "О программе",
        "Программа для оценки объема фигур\n\n"
        "Автор: Панов Дмитрий\n"
        "Группа: К405с9-3\n"
        "Год: 2025\n\n"
        "github: https://github.com/dimidroloff"
    )

def show_technology():
    messagebox.showinfo(
        "О Технологиях",
        "В проекте были использованы:\nPython 3.8\n"
        "Tkinter\n"
        "Pillow 10.4.0\n"
        "ttkbootstrap 1.13.9"
    )

def show_formuls():
    messagebox.showinfo(
        "О формулах",
        "V куб = \t\tabc\n"
        "V пирамида = \t1/3 * Sосн * h\n"
        "V конус = \t1/3 * π * r²\n"
        "V цилиндр = \tπ * r² * h\n"
        "V шар = \t\t4/3 * π * r³"
    )

def create_entry(placeholder, showed=False):
    ret = ttk.Entry(root, width=25)
    add_placeholder(ret, placeholder)
    if showed:
        ret.pack(anchor=N, padx=6, pady=6)
    return ret


def add_placeholder(entry, placeholder):
    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, END)
            entry.config(foreground='black')

    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(foreground='gray')

    entry.insert(0, placeholder)
    entry.config(foreground='gray')
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


def update_choice(event):
    btn.pack_forget()
    label.pack_forget()
    selection = choice.get()
    all_entries = cubes + pyramids + cones + balls + cylinders
    for i in all_entries:
        i.pack_forget()
    if selection == objects[0]:
        for i in cubes:
            i.pack(anchor=N, padx=6, pady=6)
    elif selection == objects[1]:
        for i in pyramids:
            i.pack(anchor=N, padx=6, pady=6)
    elif selection == objects[2]:
        for i in cones:
            i.pack(anchor=N, padx=6, pady=6)
    elif selection == objects[3]:
        for i in balls:
            i.pack(anchor=N, padx=6, pady=6)
    elif selection == objects[4]:
        for i in cylinders:
            i.pack(anchor=N, padx=6, pady=6)
    btn.pack(anchor=N, padx=6, pady=25)
    image = images.get(selection)
    if image:
        image_label.config(image=image)
        image_label.image = image  # сохранить ссылку

    label.pack(anchor=N, padx=6, pady=6)
    label["foreground"] = "black"
    label["text"] = "Введите данные и нажмите на кнопку"


def get_value(obj):
    ret = eval(obj.get().replace(",", "."))
    if ret < 0:
        raise ValueError("Неверный ввод или отрицательное число")
    return ret


def enter():
    selection = choice.get()
    label["foreground"] = "black"
    try:
        if selection == objects[0]:
            # Vкуб = а + б + с
            v = get_value(cube1) * get_value(cube2) * get_value(cube3)
            res = f"Объем {objects[0].lower()}а = {v:.2f}"

        elif selection == objects[1]:
            # V пирамиды = Sосн * h * 1/3
            v = get_value(pyramid1) * get_value(pyramid2) * 1 / 3
            res = f"Объем {objects[1].lower()[:-1]}ы = {v:.2f}"

        elif selection == objects[2]:
            # V конуса = 1/3 * pi * r^2 * h
            v = get_value(cone1) ** 2 * get_value(cone2) * 1 / 3 * pi
            res = f"Объем {objects[2].lower()}а = {v:.2f}"

        elif selection == objects[3]:
            # V шара = 4/3 * pi * r^3
            v = get_value(ball1) ** 3 * 4 / 3 * pi
            res = f"Объем {objects[3].lower()}а = {v:.2f}"

        elif selection == objects[4]:
            # V цилиндра = pi * r^2 * h
            v = get_value(cylinder1) ** 2 * pi * get_value(cylinder2)
            res = f"Объем {objects[4].lower()}а = {v:.2f}"

        else:
            res = "Ошибка в выборе"
            label["foreground"] = "red"
            label["text"] = res
            messagebox.showerror("Ошибка", "Проверьте корректность введённых данных.")

    except Exception:
        res = "Неверный ввод или отрицательное число"
        label["foreground"] = "red"
        label["text"] = res
        messagebox.showerror("Ошибка", "Проверьте корректность введённых данных.")

    label["text"] = res

# Создаем окно
root = tb.Window(themename="simplex")  # другие темы: "litera", "cosmo", "darkly", "cyborg", "flatly" и т.д. journal
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 300
window_height = 500
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.title("Вычисление объема")
icon = PhotoImage(file="logo.png")  # PNG-иконка
root.iconphoto(False, icon)

menu = Menu(root)
root.config(menu=menu)

info_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Справка", menu=info_menu)
info_menu.add_command(label="О программе", command=show_about)
info_menu.add_command(label="Технология", command=show_technology)
info_menu.add_command(label="Формулы", command=show_formuls)

# Вычисление по enter
root.bind('<Return>', lambda event: enter())

image_label = Label(root)
image_label.pack(anchor=N, pady=10)

# Словарь с картинками (грузим 1 раз)
images = {
    "Куб": ImageTk.PhotoImage(Image.open("cube.jpg").resize((120, 120))),
    "Пирамида": ImageTk.PhotoImage(Image.open("pyramid.jpg").resize((120, 120))),
    "Конус": ImageTk.PhotoImage(Image.open("cone.jpg").resize((120, 120))),
    "Шар": ImageTk.PhotoImage(Image.open("ball.jpg").resize((120, 120))),
    "Цилиндр": ImageTk.PhotoImage(Image.open("cylinder.jpg").resize((120, 120))),
}
image = images.get("Куб")
if image:
    image_label.config(image=image)
    image_label.image = image  # сохранить ссылку

objects = ["Куб", "Пирамида", "Конус", "Шар", "Цилиндр"]
objects_var = StringVar(value=objects[0])

choice = ttk.Combobox(textvariable=objects_var, values=objects, width=20, state="readonly")
choice.pack(anchor=N, pady=20)
choice.bind("<<ComboboxSelected>>", update_choice)

# Vкуб = а * б * с
cubes = []
cube1 = create_entry("Длина куба (a)", True)
cube2 = create_entry("Ширина куба (b)", True)
cube3 = create_entry("Высота куба (c)", True)
cubes.extend([cube1, cube2, cube3])

# V пирамиды = Sосн * h * 1/3
pyramids = []
pyramid1 = create_entry("Площадь основания (Sосн)")
pyramid2 = create_entry("Высота пирамиды (h)")
pyramids.extend([pyramid1, pyramid2])

# V конуса = 1/3 * pi * r^2 * h
cones = []
cone1 = create_entry("Радиус основания (r)")
cone2 = create_entry("Высота пирамиды (h)")
cones.extend([cone1, cone2])

# V шара = 4/3 * pi * r^3
balls = []
ball1 = create_entry("Радиус шара (r)")
balls.extend([ball1])

# V цилиндра = pi * r^2 * h
cylinders = []
cylinder1 = create_entry("Радиус цилиндра (r)")
cylinder2 = create_entry("Высота цилиндра (h)")
cylinders.extend([cylinder1, cylinder2])

# кнопка
btn = ttk.Button(text="Вычислить объем", command=enter)
btn.pack(anchor=N, padx=6, pady=25)

# Информация
label = ttk.Label(text="Введите данные и нажмите на кнопку")
label.pack(anchor=N, padx=6, pady=6)

root.mainloop()
