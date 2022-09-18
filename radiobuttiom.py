import tkinter
from tkinter import ttk
class RadioButton:
    def __init__(self, root,list_options):
        self.list_options = list_options
        self.root = root
        self.option = tkinter.StringVar()
        self.view = tkinter.StringVar()
        self.view.set("Select Option")
        self.frames()
        self.radio_buttons()
        self.reset_button()
        self.option_view()
    def frames(self):
        self.main_frame = ttk.Frame(self.root,padding=10)
        self.main_frame.grid(row=0, column=0)
    def run_window(self):
        self.root.mainloop()
    def radio_buttons(self):
        for i in range(len(self.list_options)):
            option_select = ttk.Radiobutton(self.root,text=self.list_options[i],variable=self.option,value=self.list_options[i],
                                            command=lambda:self.view.set(self.option.get()))
            option_select.grid(row=i, column=0,padx=10,pady=5,sticky='W')
    def reset_button(self):
        reset = ttk.Button(self.root,text="reset",command=lambda:[self.view.set("Select Option"),self.option.set(None)])
        reset.grid(row=len(self.list_options),column=0,padx=20,pady=5,sticky='W E')
    def option_view(self):
        view = ttk.Label(self.root,textvariable=self.view)
        view.grid(row=4,column=1,padx=10,pady=5,sticky='W E')
if __name__ == '__main__':
    idioms = ['English', 'French', 'German', 'Spanish', 'Chinese', 'Japanese', 'Russian']
    root = tkinter.Tk()
    control = RadioButton(root,idioms)
    control.run_window()
