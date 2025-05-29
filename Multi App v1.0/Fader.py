from customtkinter import *
from PIL import Image

class Main:
    def __init__(self):
        run = CTk()
        width, height = 920, 680
        screen_width = run.winfo_screenwidth()
        screen_height = run.winfo_screenheight()
        x = int((screen_width - width) / 2)
        y = int((screen_height - height) / 2)
        run.geometry(f"{width}x{height}+{x}+{y}")
        run.overrideredirect(True)

        gif_path = "select.gif"
        gif = Image.open(gif_path)
        gif_frames = []

        for frame in range(gif.n_frames):
            gif.seek(frame)
            frame_image = CTkImage(gif.copy(), size=(width, height))
            gif_frames.append(frame_image)

        label = CTkLabel(run, text='')
        label.pack(expand=True)

        def animate_gif(frame=0):
            if frame < len(gif_frames):
                label.configure(image=gif_frames[frame])
                run.after(10, animate_gif, frame + 1)
            else:
                run.destroy()
                stand() 

        animate_gif()
        run.mainloop()

class stand():
    def __init__(self):
        window=CTk()
        height = window.winfo_screenheight()
        width = window.winfo_screenwidth()
        window.geometry(f"{width-10}x{height-85}+10+10")
        set_appearance_mode('light')
        window.overrideredirect(True)
        window.rowconfigure(0,weight=1)
        window.rowconfigure(1,weight=1)
        window.rowconfigure(2,weight=1)
        window.rowconfigure(3,weight=1)
        window.rowconfigure(4,weight=1)
        window.rowconfigure(5,weight=1)
        window.rowconfigure(6,weight=1)
        window.rowconfigure(7,weight=1)
        window.rowconfigure(8,weight=1)
        window.rowconfigure(9,weight=1)
        window.rowconfigure(10,weight=1)
        # window.columnconfigure(0,weight=1)
        # window.columnconfigure(1,weight=1)
        # window.columnconfigure(2,weight=1)
        # window.columnconfigure(3,weight=1)

        ###################################################################################
        title_bar = CTkFrame(window, height=height-85,width=width//20,fg_color="#001AFF")
        title_bar.rowconfigure(0,weight=1)
        title_bar.rowconfigure(1,weight=1)
        title_bar.rowconfigure(2,weight=1)
        title_bar.rowconfigure(3,weight=1)
        title_bar.rowconfigure(4,weight=1)
        title_bar.rowconfigure(5,weight=1)
        title_bar.rowconfigure(6,weight=1)
        title_bar.rowconfigure(7,weight=1)
        title_bar.rowconfigure(8,weight=1)
        title_bar.rowconfigure(9,weight=1)
        title_bar.rowconfigure(10,weight=1)
        title_bar.grid(row=0,column=0,rowspan=11,sticky="ns")
        Icon_BTN= CTkButton(title_bar,text='H',font=("Arial",30),width=40,height=40)
        Icon_BTN.grid(row=0,column=0,padx=10)
        Home_BTN= CTkButton(title_bar,text='🏠',font=("Arial",20),width=30,height=30)
        Home_BTN.grid(row=4,column=0,padx=10)
        Ai_BTN= CTkButton(title_bar,text='💬',font=("Arial",20),width=30,height=30)
        Ai_BTN.grid(row=5,column=0,padx=10)
        Nothif_BTN= CTkButton(title_bar,text='🔔',font=("Arial",20),width=30,height=30)
        Nothif_BTN.grid(row=6,column=0,padx=10)
        Browers_BTN= CTkButton(title_bar,text='🔍',font=("Arial",20),width=30,height=30)
        Browers_BTN.grid(row=7,column=0,padx=10)
        Dot_BTN= CTkButton(title_bar,text='H',font=("Arial",30),width=40,height=40)
        Dot_BTN.grid(row=10,column=0,padx=10)
        YourAcont_BTN= CTkButton(title_bar,text='H',font=("Arial",30),width=40,height=40)
        YourAcont_BTN.grid(row=11,column=0,pady=10,padx=10)
        #################################################################################
        # Sc_bar=CTkFrame(window,height=height-920,width=width/20)
        # Sc_bar.grid(row=0,column=1,columnspan=4,sticky='we')


        window.mainloop()

if __name__ == '__main__':
    Main()
