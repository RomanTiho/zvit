import customtkinter as ctk

class BookingsView:
    def __init__(self, parent, hotel, current_role, colors):
        self.parent = parent
        self.hotel = hotel
        self.current_role = current_role
        self.colors = colors
        self.frame = None

    def show(self):
        if self.frame:
            self.frame.destroy()

        self.frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.frame.pack(fill="both", expand=True, padx=10, pady=10)

        header = ctk.CTkFrame(self.frame, fg_color=self.colors["secondary"], height=80)
        header.pack(fill="x", pady=(0, 20))
        header.pack_propagate(False)

        title = ctk.CTkLabel(header,
                             text="📅 Бронювання номерів",
                             font=("Roboto", 24, "bold"),
                             text_color=self.colors["text"])
        title.pack(expand=True)

        form_frame = ctk.CTkFrame(self.frame, fg_color=self.colors["bg_light"])
        form_frame.pack(fill="x", padx=10, pady=10)

        form_title = ctk.CTkLabel(form_frame,
                                  text="✏️ Нове бронювання",
                                  font=("Roboto", 16, "bold"),
                                  text_color=self.colors["text"])
        form_title.pack(pady=10)

        room_var = ctk.StringVar()
        available_rooms = [room for room, data in self.hotel.rooms.items()
                           if data["status"] == "вільний"]

        room_label = ctk.CTkLabel(form_frame,
                                  text="Виберіть номер:",
                                  font=("Roboto", 14),
                                  text_color=self.colors["text"])
        room_label.pack(pady=(10, 5))

        self.room_menu = ctk.CTkOptionMenu(form_frame,
                                           values=available_rooms,
                                           variable=room_var,
                                           font=("Roboto", 12),
                                           fg_color=self.colors["primary"],
                                           button_color=self.colors["secondary"],
                                           button_hover_color=self.colors["primary"])
        self.room_menu.pack(pady=5)

        self.guest_name = ctk.CTkEntry(form_frame,
                                       placeholder_text="Ім'я гостя",
                                       font=("Roboto", 12),
                                       fg_color=self.colors["bg_dark"],
                                       border_color=self.colors["primary"],
                                       width=300)
        self.guest_name.pack(pady=5)

        self.guest_phone = ctk.CTkEntry(form_frame,
                                        placeholder_text="Телефон",
                                        font=("Roboto", 12),
                                        fg_color=self.colors["bg_dark"],
                                        border_color=self.colors["primary"],
                                        width=300)
        self.guest_phone.pack(pady=5)

        dates_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        dates_frame.pack(pady=5)

        self.check_in = ctk.CTkEntry(dates_frame,
                                     placeholder_text="Дата заїзду (YYYY-MM-DD)",
                                     font=("Roboto", 12),
                                     fg_color=self.colors["bg_dark"],
                                     border_color=self.colors["primary"],
                                     width=200)
        self.check_in.pack(side="left", padx=5)

        self.check_out = ctk.CTkEntry(dates_frame,
                                      placeholder_text="Дата виїзду (YYYY-MM-DD)",
                                      font=("Roboto", 12),
                                      fg_color=self.colors["bg_dark"],
                                      border_color=self.colors["primary"],
                                      width=200)
        self.check_out.pack(side="left", padx=5)

        submit_btn = ctk.CTkButton(form_frame,
                                   text="✅ Забронювати",
                                   command=self._make_booking,
                                   font=("Roboto", 14, "bold"),
                                   fg_color='#09966e',
                                   hover_color=self.colors["success"],
                                   width=200)
        submit_btn.pack(pady=15)

        bookings_label = ctk.CTkLabel(self.frame,
                                      text="📋 Поточні бронювання",
                                      font=("Roboto", 18, "bold"),
                                      text_color=self.colors["text"])
        bookings_label.pack(pady=20)

        bookings_frame = ctk.CTkScrollableFrame(self.frame,
                                                fg_color="transparent")
        bookings_frame.pack(fill="both", expand=True, padx=10, pady=10)

        for room, booking in self.hotel.bookings.items():
            booking_info = ctk.CTkFrame(bookings_frame,
                                        fg_color=self.colors["bg_light"])
            booking_info.pack(fill="x", padx=10, pady=5)

            info_text = f"🏠 Номер {room} - 👤 {booking['guest']}\n"
            info_text += f"📞 Телефон: {booking['phone']}\n"
            info_text += f"📅 Заїзд: {booking['check_in']}, Виїзд: {booking['check_out']}"

            info_label = ctk.CTkLabel(booking_info,
                                      text=info_text,
                                      font=("Roboto", 12),
                                      text_color=self.colors["text"])
            info_label.pack(side="left", padx=15, pady=10)

            if self.current_role == "manager":
                delete_btn = ctk.CTkButton(booking_info,
                                           text="❌ Видалити",
                                           command=lambda r=room: self._delete_booking(r),
                                           font=("Roboto", 12),
                                           fg_color=self.colors["danger"],
                                           hover_color="#c41e2f",
                                           width=100)
                delete_btn.pack(side="right", padx=15, pady=10)

    def _make_booking(self):
        room = self.room_menu.get()
        if room and self.guest_name.get() and self.check_in.get() and self.check_out.get():
            self.hotel.rooms[room]["status"] = "зайнятий"
            self.hotel.bookings[room] = {
                "guest": self.guest_name.get(),
                "phone": self.guest_phone.get(),
                "check_in": self.check_in.get(),
                "check_out": self.check_out.get()
            }
            self.show()

    def _delete_booking(self, room):
        if room in self.hotel.bookings:
            del self.hotel.bookings[room]
            self.hotel.rooms[room]["status"] = "вільний"
            self.show()