from tkinter import *
windows = Tk()
windows.title('Miles to Kilometer Convertor')
windows.minsize(width=300, height=150)
windows.config(pady=30)

def create_label(text_entered,x,y):
   label = Label(text=text_entered)
   label.place(x=x, y=y)



mile_entry = Entry(width=10)
mile_entry.place(x=130, y=0)


miles_lable = create_label('Miles',200,0)
lable_2 = create_label("Is equal to",60,60)

km_label = Label(text='0')
km_label.place(x=150, y=60)

label_4 = create_label("Km",200,60)


def convert():
    user_entry = mile_entry.get()
    print(user_entry)
    km = round(float(user_entry) * 1.61, 2)
    km_label.config(text=km)


button = Button(text="Calculate", command=convert)
button.place(x=140, y=100)
windows.mainloop()
