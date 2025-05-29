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

        gif_path = '//home/mohamad/myenv/Multi_App/Lgine.gif'
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
        title_bar.place(relx=0,rely=0, relwidth=0.07, relheight=1)
        Icon=Image.open('//home/mohamad/myenv/Multi_App/Icon.jpg')
        icon=CTkImage(Icon,size=(90,90))
        Icon_BTN= CTkButton(title_bar,text='',width=40,height=40,image=icon)
        Icon_BTN.grid(row=0,column=0,padx=10)
        Icon=Image.open('//home/mohamad/myenv/Multi_App/Icon.jpg')
        icon=CTkImage(Icon,size=(90,90))
        Home_BTN= CTkButton(title_bar,text='🏠',font=("Arial",20),width=30,height=30)
        Home_BTN.grid(row=4,column=0,padx=10)
        Icon=Image.open('//home/mohamad/myenv/Multi_App/Icon.jpg')
        icon=CTkImage(Icon,size=(90,90))
        Ai_BTN= CTkButton(title_bar,text='💬',font=("Arial",20),width=30,height=30)
        Ai_BTN.grid(row=5,column=0,padx=10)
        Icon=Image.open('//home/mohamad/myenv/Multi_App/Icon.jpg')
        icon=CTkImage(Icon,size=(90,90))
        Nothif_BTN= CTkButton(title_bar,text='🔔',font=("Arial",20),width=30,height=30)
        Nothif_BTN.grid(row=6,column=0,padx=10)
        Icon=Image.open('//home/mohamad/myenv/Multi_App/Icon.jpg')
        icon=CTkImage(Icon,size=(90,90))
        Browers_BTN= CTkButton(title_bar,text='🔍',font=("Arial",20),width=30,height=30)
        Browers_BTN.grid(row=7,column=0,padx=10)
        Dot_BTN= CTkButton(title_bar,text='H',font=("Arial",30),width=40,height=40)
        Dot_BTN.grid(row=10,column=0,padx=10)
        YourAcont_BTN= CTkButton(title_bar,text='H',font=("Arial",30),width=40,height=40)
        YourAcont_BTN.grid(row=11,column=0,pady=10,padx=10)
        #################################################################################
        Sc_bar=CTkFrame(window,fg_color='#b3b3b3')
        Sc_bar.place(relx=0.075,rely=0.003,relwidth=0.92,relheight=0.04)
        btn_ex=CTkButton(Sc_bar,text='❌',command=lambda:window.destroy(),fg_color="#001AFF")
        btn_ex.place(relx=0.95,rely=0.1,relwidth=0.05,relheight=0.8)
        is_maximized = [False]
        prev_geometry = [None]

        def toggle_maximize():
            if not is_maximized[0]:
                prev_geometry[0] = window.geometry()
                window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}+0+0")
                is_maximized[0] = True
            else:
                window.geometry(prev_geometry[0])
                is_maximized[0] = False
        btn_full=CTkButton(Sc_bar,text='🔲',command=lambda:toggle_maximize(),fg_color="#001AFF")
        btn_full.place(relx=0.9,rely=0.1,relwidth=0.05,relheight=0.8)
        btn_min=CTkButton(Sc_bar,text='➖',command=lambda:window.iconify(),fg_color="#001AFF")
        btn_min.place(relx=0.85,rely=0.1,relwidth=0.05,relheight=0.8)
        #####################################################################################
        Sc_bar2=CTkScrollableFrame(window,fg_color='#c4c4c4')
        Sc_bar2.place(relx=0.075,rely=0.045,relwidth=0.327,relheight=0.94)
        ######################################################################################
        Sc_bar3=CTkScrollableFrame(window,fg_color='#c4c4c4')
        Sc_bar3.place(relx=0.405,rely=0.045,relwidth=0.59,relheight=0.94)

        window.mainloop() 

if __name__ == '__main__':
    Main()
