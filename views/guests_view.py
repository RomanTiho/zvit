import customtkinter as ctk

class GuestsView:
    def __init__(self, parent, hotel, colors):
        self.parent = parent
        self.hotel = hotel
        self.colors = colors
        self.frame = None

    def show(self):
        if self.frame:
            self.frame.destroy()

        self.frame = ctk.CTkScrollableFrame(self.parent, fg_color="transparent")
        self.frame.pack(fill="both", expand=True, padx=10, pady=10)

        header = ctk.CTkFrame(self.frame, fg_color=self.colors["secondary"], height=80)
        header.pack(fill="x", pady=(0, 20))
        header.pack_propagate(False)

        title = ctk.CTkLabel(header,
                             text="👥 Гості готелю",
                             font=("Roboto", 24, "bold"),
                             text_color=self.colors["text"])
        title.pack(expand=True)

        for room, booking in self.hotel.bookings.items():
            guest_frame = ctk.CTkFrame(self.frame, fg_color=self.colors["bg_light"])
            guest_frame.pack(fill="x", padx=10, pady=5)

            info_frame = ctk.CTkFrame(guest_frame, fg_color="transparent")
            info_frame.pack(fill="both", expand=True, padx=15, pady=10)

            name_label = ctk.CTkLabel(info_frame,
                                      text=f"👤 {booking['guest']}",
                                      font=("Roboto", 16, "bold"),
                                      text_color=self.colors["text"])
            name_label.pack(anchor="w")

            room_label = ctk.CTkLabel(info_frame,
                                      text=f"🏠 Номер: {room}",
                                      font=("Roboto", 14),
                                      text_color=self.colors["text"])
            room_label.pack(anchor="w")

            phone_label = ctk.CTkLabel(info_frame,
                                       text=f"📞 Телефон: {booking['phone']}",
                                       font=("Roboto", 14),
                                       text_color=self.colors["text"])
            phone_label.pack(anchor="w")

            dates_label = ctk.CTkLabel(info_frame,
                                       text=f"📅 {booking['check_in']} - {booking['check_out']}",
                                       font=("Roboto", 14),
                                       text_color=self.colors["accent"])
            dates_label.pack(anchor="w")