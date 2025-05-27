import customtkinter as ctk
from models.hotel import Hotel
from views.login_view import LoginView
from views.rooms_view import RoomsView
from views.booking_view import BookingsView
from views.guests_view import GuestsView
from views.services_view import ServicesView


class HotelApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.hotel = Hotel()
        self.current_user = None
        self.current_role = None

        self.title("Система управління готелем")
        self.geometry("1200x800")

        self.colors = {
            "primary": "#2c5282",
            "secondary": "#1a365d",
            "accent": "#d97706",
            "success": "#047857",
            "warning": "#d97706",
            "danger": "#991b1b",
            "bg_dark": "#1a1a1a",
            "bg_light": "#2d2d2d",
            "text": "#ffffff"
        }

        ctk.set_appearance_mode("dark")

        self.main_container = ctk.CTkFrame(self, fg_color=self.colors["bg_dark"])
        self.main_container.pack(fill="both", expand=True, padx=10, pady=10)

        self.login_view = LoginView(self.main_container, self._handle_login, self.colors)
        self.rooms_view = None
        self.bookings_view = None
        self.guests_view = None
        self.services_view = None

        self.protocol("WM_DELETE_WINDOW", self._on_closing)

        self.show_login_screen()

    def _on_closing(self):
        self.hotel.save_all()
        self.destroy()

    def show_login_screen(self):
        self.login_view.show()

    def _handle_login(self, username, role):
        self.current_user = username
        self.current_role = role
        self.show_main_screen()

    def show_main_screen(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

        sidebar = ctk.CTkFrame(self.main_container, width=250, fg_color=self.colors["secondary"])
        sidebar.pack(side="left", fill="y", padx=5, pady=5)
        sidebar.pack_propagate(False)

        user_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        user_frame.pack(fill="x", padx=15, pady=20)

        role_color = self.colors["accent"] if self.current_role == "manager" else self.colors["success"]

        title_label = ctk.CTkLabel(user_frame,
                                   text="👤 Профіль користувача",
                                   font=("Roboto", 16, "bold"),
                                   text_color=self.colors["text"])
        title_label.pack(pady=(0, 5))

        user_label = ctk.CTkLabel(user_frame,
                                  text=f"{self.current_user}",
                                  font=("Roboto", 14))
        user_label.pack()

        role_label = ctk.CTkLabel(user_frame,
                                  text=f"({self.current_role})",
                                  font=("Roboto", 12),
                                  text_color=role_color)
        role_label.pack()

        separator = ctk.CTkFrame(sidebar, height=2, fg_color=self.colors["bg_light"])
        separator.pack(fill="x", padx=15, pady=10)

        buttons_data = [
            ("🏠 Огляд номерів", self.show_rooms_view, self.colors["primary"]),
            ("📅 Бронювання", self.show_booking_view, self.colors["success"]),
            ("👥 Гості", self.show_guests_view, self.colors["warning"]),
            ("🛍 Послуги", self.show_services_view, self.colors["accent"])
        ]

        for text, command, color in buttons_data:
            btn = ctk.CTkButton(sidebar, text=text, command=command,
                                font=("Roboto", 14),
                                fg_color=color,
                                hover_color=self.colors["bg_light"],
                                height=40)
            btn.pack(pady=5, padx=15, fill="x")

        save_btn = ctk.CTkButton(sidebar, text="💾 Зберегти",
                                 command=self.hotel.save_all,
                                 font=("Roboto", 14),
                                 fg_color=self.colors["success"],
                                 hover_color="#03543f",
                                 height=40)
        save_btn.pack(pady=5, padx=15, fill="x")

        logout_btn = ctk.CTkButton(sidebar, text="↩ Вийти",
                                   command=self.show_login_screen,
                                   font=("Roboto", 14),
                                   fg_color=self.colors["danger"],
                                   hover_color="#7f1d1d",
                                   height=40)
        logout_btn.pack(pady=20, padx=15, fill="x", side="bottom")

        content_container = ctk.CTkFrame(self.main_container, fg_color=self.colors["bg_dark"])
        content_container.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        self.content_frame = ctk.CTkScrollableFrame(content_container, fg_color=self.colors["bg_light"])
        self.content_frame.pack(side="left", fill="both", expand=True)

        self.rooms_view = RoomsView(self.content_frame, self.hotel, self.current_role, self.colors)
        self.bookings_view = BookingsView(self.content_frame, self.hotel, self.current_role, self.colors)
        self.guests_view = GuestsView(self.content_frame, self.hotel, self.colors)
        self.services_view = ServicesView(self.content_frame, self.hotel, self.current_role, self.colors)

        self.show_rooms_view()

    def show_rooms_view(self):
        self.rooms_view.show()

    def show_booking_view(self):
        self.bookings_view.show()

    def show_guests_view(self):
        self.guests_view.show()

    def show_services_view(self):
        self.services_view.show()


if __name__ == "__main__":
    app = HotelApp()
    app.mainloop()