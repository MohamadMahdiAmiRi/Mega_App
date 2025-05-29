import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class ModernApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("اپلیکیشن مدرن طلایی - آبی")
        self.geometry("900x600")
        self.minsize(800, 500)

        # کانتینر اصلی
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # نوار کناری (Sidebar)
        self.sidebar = ctk.CTkFrame(self, width=200, fg_color="#162A4F", corner_radius=10)
        self.sidebar.grid(row=0, column=0, sticky="ns", padx=15, pady=15)

        self.logo_label = ctk.CTkLabel(self.sidebar, text="ModernApp", font=ctk.CTkFont(size=24, weight="bold"), text_color="#E1E6F0")
        self.logo_label.pack(pady=(20, 40))

        # دکمه‌های ناوبری با رنگ طلایی ملایم
        self.btn_dashboard = ctk.CTkButton(self.sidebar, text="داشبورد", fg_color="#F4C430", hover_color="#D9B419", corner_radius=12, command=self.show_dashboard)
        self.btn_dashboard.pack(fill="x", pady=10, padx=20)

        self.btn_settings = ctk.CTkButton(self.sidebar, text="تنظیمات", fg_color=None, hover_color="#D9B419", corner_radius=12, command=self.show_settings)
        self.btn_settings.pack(fill="x", pady=10, padx=20)

        self.btn_about = ctk.CTkButton(self.sidebar, text="درباره ما", fg_color=None, hover_color="#D9B419", corner_radius=12, command=self.show_about)
        self.btn_about.pack(fill="x", pady=10, padx=20)

        # فریم محتوای اصلی
        self.main_frame = ctk.CTkFrame(self, corner_radius=15)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)

        # نمایش پیش‌فرض داشبورد
        self.show_dashboard()

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_main_frame()

        header = ctk.CTkLabel(self.main_frame, text="داشبورد", font=ctk.CTkFont(size=28, weight="bold"), text_color="#E1E6F0")
        header.pack(pady=20)

        # کارت‌ها
        card_frame = ctk.CTkFrame(self.main_frame, fg_color="#0B1120", corner_radius=12)
        card_frame.pack(padx=20, pady=10, fill="x")

        for i in range(3):
            card = ctk.CTkFrame(card_frame, width=200, height=120, fg_color="#1C2C54", corner_radius=12)
            card.grid(row=0, column=i, padx=15, pady=15)
            card.grid_propagate(False)

            label = ctk.CTkLabel(card, text=f"کارت شماره {i+1}", font=ctk.CTkFont(size=16), text_color="#E1E6F0")
            label.place(relx=0.5, rely=0.4, anchor="center")

            value = ctk.CTkLabel(card, text=f"{(i+1)*123}", font=ctk.CTkFont(size=24, weight="bold"), text_color="#F4C430")
            value.place(relx=0.5, rely=0.7, anchor="center")

    def show_settings(self):
        self.clear_main_frame()

        header = ctk.CTkLabel(self.main_frame, text="تنظیمات", font=ctk.CTkFont(size=28, weight="bold"), text_color="#E1E6F0")
        header.pack(pady=20)

        def toggle_appearance():
            current = ctk.get_appearance_mode()
            new_mode = "light" if current == "dark" else "dark"
            ctk.set_appearance_mode(new_mode)

        toggle_btn = ctk.CTkButton(self.main_frame, text="تغییر حالت روشن/تاریک", command=toggle_appearance, corner_radius=12)
        toggle_btn.pack(pady=15)

    def show_about(self):
        self.clear_main_frame()

        header = ctk.CTkLabel(self.main_frame, text="درباره ما", font=ctk.CTkFont(size=28, weight="bold"), text_color="#E1E6F0")
        header.pack(pady=20)

        about_text = "این اپلیکیشن نمونه‌ای از طراحی مدرن با CustomTkinter است.\nطراحی شده توسط محمد."
        label = ctk.CTkLabel(self.main_frame, text=about_text, font=ctk.CTkFont(size=16), justify="center", text_color="#E1E6F0")
        label.pack(padx=40, pady=30)

if __name__ == "__main__":
    app = ModernApp()
    app.mainloop()
