import customtkinter as ctk

class LoginView:
    def __init__(self, parent, on_login, colors):
        self.parent = parent
        self.on_login = on_login
        self.colors = colors
        self.frame = None

    def show(self):
        if self.frame:
            self.frame.destroy()

        self.frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.frame.pack(expand=True, padx=20, pady=20)

        login_container = ctk.CTkFrame(self.frame, fg_color=self.colors["bg_light"])
        login_container.pack(expand=True, padx=20, pady=20)

        title = ctk.CTkLabel(login_container,
                             text="👤 Вхід в систему",
                             font=("Roboto", 24, "bold"),
                             text_color=self.colors["text"])
        title.pack(pady=20)

        self.username_entry = ctk.CTkEntry(login_container,
                                           placeholder_text="Логін",
                                           font=("Roboto", 14),
                                           fg_color=self.colors["bg_dark"],
                                           border_color=self.colors["primary"],
                                           width=300)
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(login_container,
                                           placeholder_text="Пароль",
                                           show="*",
                                           font=("Roboto", 14),
                                           fg_color=self.colors["bg_dark"],
                                           border_color=self.colors["primary"],
                                           width=300)
        self.password_entry.pack(pady=10)

        self.role_var = ctk.StringVar(value="receptionist")
        role_frame = ctk.CTkFrame(login_container, fg_color="transparent")
        role_frame.pack(pady=20)

        receptionist_radio = ctk.CTkRadioButton(role_frame,
                                                text="Рецепціоніст",
                                                variable=self.role_var,
                                                value="receptionist",
                                                font=("Roboto", 12),
                                                fg_color=self.colors["primary"],
                                                border_color=self.colors["primary"])
        receptionist_radio.pack(side="left", padx=10)

        manager_radio = ctk.CTkRadioButton(role_frame,
                                           text="Менеджер",
                                           variable=self.role_var,
                                           value="manager",
                                           font=("Roboto", 12),
                                           fg_color=self.colors["primary"],
                                           border_color=self.colors["primary"])
        manager_radio.pack(side="left", padx=10)

        login_button = ctk.CTkButton(login_container,
                                     text="Увійти",
                                     command=self._handle_login,
                                     font=("Roboto", 14, "bold"),
                                     fg_color=self.colors["primary"],
                                     hover_color=self.colors["secondary"],
                                     width=200)
        login_button.pack(pady=20)

    def _handle_login(self):
        username = self.username_entry.get()
        if username:
            self.on_login(username, self.role_var.get())