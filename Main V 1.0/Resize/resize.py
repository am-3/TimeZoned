import tkinter as tk

# from PIL import ImageTk, Image

resize = tk.Tk()
resize.title('Resize your experience')
#resize.iconbitmap(path)
resize.geometry('400x400')

def get_new_size():
    mylabel = tk.Label(resize, text=str(hor_slide.get()) + 'x' + str(ver_slide.get())).pack()
    #root.geometry(str(hor_slide.get()) + 'x' + str(ver_slide.get()))
    return

hor_slide = tk.Scale(resize, from_=400, to=1920, orient='horizontal')
hor_slide.pack()

ver_slide = tk.Scale(resize, from_=400, to=1080)
ver_slide.pack()

btn = tk.Button(resize, text='Update Size', command=get_new_size).pack()



resize.mainloop()
