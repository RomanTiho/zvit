import customtkinter as ctk

class RoomsView:
    def __init__(self, parent, hotel, current_role, colors):
        self.parent = parent
        self.hotel = hotel
        self.current_role = current_role
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
                             text="🏠 Огляд номерів",
                             font=("Roboto", 24, "bold"),
                             text_color=self.colors["text"])
        title.pack(expand=True)

        for room_number, room_data in self.hotel.rooms.items():
            room_frame = ctk.CTkFrame(self.frame, fg_color=self.colors["bg_light"])
            room_frame.pack(fill="x", pady=5, padx=5)

            status_color = self.colors["success"] if room_data["status"] == "вільний" else self.colors["danger"]
            cleaning_color = self.colors["success"] if room_data["cleaning_status"] == "чистий" else self.colors[
                "warning"]

            info_frame = ctk.CTkFrame(room_frame, fg_color="transparent")
            info_frame.pack(side="left", padx=15, pady=10)

            room_number_label = ctk.CTkLabel(info_frame,
                                             text=f"Номер {room_number}",
                                             font=("Roboto", 16, "bold"),
                                             text_color=self.colors["text"])
            room_number_label.pack(anchor="w")

            room_type_label = ctk.CTkLabel(info_frame,
                                           text=room_data['type'],
                                           font=("Roboto", 14),
                                           text_color=self.colors["text"])
            room_type_label.pack(anchor="w")

            price_label = ctk.CTkLabel(info_frame,
                                       text=f"💰 {room_data['price']} грн",
                                       font=("Roboto", 14),
                                       text_color=self.colors["success"])
            price_label.pack(anchor="w")

            status_frame = ctk.CTkFrame(room_frame, fg_color="transparent")
            status_frame.pack(side="right", padx=15, pady=10)

            status_label = ctk.CTkLabel(status_frame,
                                        text=f"Статус: {room_data['status']}",
                                        font=("Roboto", 12),
                                        text_color=status_color)
            status_label.pack(anchor="e")

            cleaning_label = ctk.CTkLabel(status_frame,
                                          text=f"Прибирання: {room_data['cleaning_status']}",
                                          font=("Roboto", 12),
                                          text_color=cleaning_color)
            cleaning_label.pack(anchor="e")

            if self.current_role == "manager":
                buttons_frame = ctk.CTkFrame(room_frame, fg_color="transparent")
                buttons_frame.pack(side="right", padx=15, pady=10)

                maintenance_btn = ctk.CTkButton(buttons_frame,
                                                text="🔧 Тех. обслуговування",
                                                command=lambda r=room_number: self._schedule_maintenance(r),
                                                font=("Roboto", 12),
                                                fg_color=self.colors["primary"],
                                                hover_color=self.colors["secondary"])
                maintenance_btn.pack(pady=2)

                cleaning_btn = ctk.CTkButton(buttons_frame,
                                             text="🧹 Прибирання",
                                             command=lambda r=room_number: self._schedule_cleaning(r),
                                             font=("Roboto", 12),
                                             fg_color=self.colors["primary"],
                                             hover_color=self.colors["secondary"])
                cleaning_btn.pack(pady=2)

                details_btn = ctk.CTkButton(buttons_frame,
                                            text="📋 Деталі",
                                            command=lambda r=room_number: self._show_room_details(r),
                                            font=("Roboto", 12),
                                            fg_color=self.colors["primary"],
                                            hover_color=self.colors["secondary"])
                details_btn.pack(pady=2)

    def _schedule_maintenance(self, room):
        window = ctk.CTkToplevel(self.parent)
        window.title(f"Технічне обслуговування - Номер {room}")
        window.geometry("400x300")
        window.configure(fg_color=self.colors["bg_dark"])

        title = ctk.CTkLabel(window,
                             text=f"🔧 Технічне обслуговування\nНомер {room}",
                             font=("Roboto", 18, "bold"),
                             text_color=self.colors["text"])
        title.pack(pady=20)

        date_entry = ctk.CTkEntry(window,
                                  placeholder_text="Дата (YYYY-MM-DD)",
                                  font=("Roboto", 12),
                                  fg_color=self.colors["bg_light"],
                                  border_color=self.colors["primary"])
        date_entry.pack(pady=10)

        description_entry = ctk.CTkEntry(window,
                                         placeholder_text="Опис робіт",
                                         font=("Roboto", 12),
                                         fg_color=self.colors["bg_light"],
                                         border_color=self.colors["primary"])
        description_entry.pack(pady=10)

        def confirm():
            date = date_entry.get()
            description = description_entry.get()
            if date and description:
                self.hotel.maintenance_schedule[room] = {
                    "date": date,
                    "description": description
                }
                window.destroy()
                self.show()

        confirm_btn = ctk.CTkButton(window,
                                    text="Підтвердити",
                                    command=confirm,
                                    font=("Roboto", 14),
                                    fg_color=self.colors["success"],
                                    hover_color=self.colors["primary"])
        confirm_btn.pack(pady=20)

    def _schedule_cleaning(self, room):
        window = ctk.CTkToplevel(self.parent)
        window.title(f"Прибирання - Номер {room}")
        window.geometry("400x300")
        window.configure(fg_color=self.colors["bg_dark"])

        title = ctk.CTkLabel(window,
                             text=f"🧹 Прибирання\nНомер {room}",
                             font=("Roboto", 18, "bold"),
                             text_color=self.colors["text"])
        title.pack(pady=20)

        date_entry = ctk.CTkEntry(window,
                                  placeholder_text="Дата (YYYY-MM-DD)",
                                  font=("Roboto", 12),
                                  fg_color=self.colors["bg_light"],
                                  border_color=self.colors["primary"])
        date_entry.pack(pady=10)

        time_entry = ctk.CTkEntry(window,
                                  placeholder_text="Час (HH:MM)",
                                  font=("Roboto", 12),
                                  fg_color=self.colors["bg_light"],
                                  border_color=self.colors["primary"])
        time_entry.pack(pady=10)

        def confirm():
            date = date_entry.get()
            time = time_entry.get()
            if date and time:
                self.hotel.cleaning_schedule[room] = {
                    "date": date,
                    "time": time
                }
                window.destroy()
                self.show()

        confirm_btn = ctk.CTkButton(window,
                                    text="Підтвердити",
                                    command=confirm,
                                    font=("Roboto", 14),
                                    fg_color=self.colors["success"],
                                    hover_color=self.colors["primary"])
        confirm_btn.pack(pady=20)

    def _show_room_details(self, room):
        window = ctk.CTkToplevel(self.parent)
        window.title(f"Деталі номера {room}")
        window.geometry("500x400")
        window.configure(fg_color=self.colors["bg_dark"])

        title = ctk.CTkLabel(window,
                             text=f"📋 Деталі номера {room}",
                             font=("Roboto", 18, "bold"),
                             text_color=self.colors["text"])
        title.pack(pady=20)

        details_frame = ctk.CTkFrame(window, fg_color=self.colors["bg_light"])
        details_frame.pack(fill="both", expand=True, padx=20, pady=20)

        room_data = self.hotel.rooms[room]

        details_text = f"Номер: {room}\n"
        details_text += f"Тип: {room_data['type']}\n"
        details_text += f"Ціна: {room_data['price']} грн\n"
        details_text += f"Статус: {room_data['status']}\n"
        details_text += f"Прибирання: {room_data['cleaning_status']}\n"
        details_text += f"Тех. обслуговування: {'Потрібне' if room_data['maintenance'] else 'Не потрібне'}\n\n"
        details_text += f"Опис: {room_data['description']}\n\n"
        details_text += "Обладнання:\n"
        for item in room_data['equipment']:
            details_text += f"- {item}\n"

        details_label = ctk.CTkLabel(details_frame,
                                     text=details_text,
                                     font=("Roboto", 12),
                                     justify="left",
                                     text_color=self.colors["text"])
        details_label.pack(pady=20, padx=20)