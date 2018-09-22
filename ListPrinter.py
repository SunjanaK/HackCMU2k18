#
# from tkinter import *
#
# def draw(canvas, width, height):

#     for word in listy:
#         for letter in word:
#             canvas.create_text(200, 100, text=letter,
#                         font="Helvetica 26 bold underline")
#
# def runDrawing(width=300, height=300):
#     root = Tk()
#     root.resizable(width=False, height=False) # prevents resizing window
#     canvas = Canvas(root, width=width, height=height)
#     canvas.configure(bd=0, highlightthickness=0)
#     canvas.pack()
#     draw(canvas, width, height)
#     root.mainloop()
#
#
# runDrawing(400, 200)


from tkinter import *  # from tkinter import *

listy = ["cat"]

root = Tk()
t = Text(root)
for word in listy:
    for letter in word:
        t.insert(END, letter + " ")
t.pack()
root.mainloop()
