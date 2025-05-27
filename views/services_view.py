import customtkinter as ctk

class ServicesView:
    def __init__(self, parent, hotel, current_role, colors):
        self.parent = parent
        self.hotel = hotel
        self.current_role = current_role
        self.colors = colors
        self.frame = None

    def show(self):
        if self.frame:
            self.frame.destroy()

        self.frame = ctk.CTkFrame(self.parent, fg_color='transparent')
        self.frame.pack(fill='both', expand=True, padx=10, pady=10)

        header_frame = ctk.CTkFrame(self.frame, fg_color=self.colors["secondary"], height=100)
        header_frame.pack(fill="x", padx=5, pady=(0, 20))
        header_frame.pack_propagate(False)

        title = ctk.CTkLabel(header_frame, text='🛍 Послуги готелю',
                             font=('Roboto', 24, 'bold'),
                             text_color=self.colors["text"])
        title.pack(expand=True)

        services_frame = ctk.CTkScrollableFrame(self.frame, fg_color='transparent')
        services_frame.pack(fill='both', expand=True, padx=5, pady=5)

        service_types = {}
        for service, data in self.hotel.services.items():
            if data["type"] not in service_types:
                service_types[data["type"]] = []
            service_types[data["type"]].append((service, data))

        type_icons = {
            'Харчування': '🍽',
            'Відпочинок': '💆‍♂️',
            'Побутові': '🧹',
            'Транспорт': '🚗',
            'Бізнес': '💼',
            'Розваги': '🎭'
        }

        for service_type, services in service_types.items():
            type_frame = ctk.CTkFrame(services_frame, fg_color=self.colors["bg_dark"])
            type_frame.pack(fill='x', padx=10, pady=5)

            icon = type_icons.get(service_type, '📌')
            type_label = ctk.CTkLabel(type_frame,
                                      text=f'{icon} {service_type}',
                                      font=('Roboto', 18, 'bold'),
                                      text_color=self.colors["accent"])
            type_label.pack(pady=10, padx=15, anchor='w')

            services_container = ctk.CTkFrame(type_frame, fg_color='transparent')
            services_container.pack(fill='x', padx=15, pady=(0, 10))

            for service, data in services:
                service_frame = ctk.CTkFrame(services_container,
                                             fg_color=self.colors["bg_light"],
                                             corner_radius=10)
                service_frame.pack(fill='x', pady=5)

                info_frame = ctk.CTkFrame(service_frame, fg_color='transparent')
                info_frame.pack(side='left', fill='x', expand=True, padx=15, pady=10)

                name_label = ctk.CTkLabel(info_frame,
                                          text=service,
                                          font=('Roboto', 14, 'bold'),
                                          text_color=self.colors["text"])
                name_label.pack(anchor='w')

                price_label = ctk.CTkLabel(info_frame,
                                           text=f"💰 {data['price']} грн",
                                           font=('Roboto', 12),
                                           text_color=self.colors["success"])
                price_label.pack(anchor='w')

                desc_label = ctk.CTkLabel(info_frame,
                                          text=data['description'],
                                          font=('Roboto', 12),
                                          text_color=self.colors["text"])
                desc_label.pack(anchor='w')

                if self.current_role == "receptionist":
                    order_btn = ctk.CTkButton(service_frame,
                                              text="Замовити",
                                              command=lambda s=service: self._order_service(s),
                                              font=("Roboto", 12),
                                              fg_color=self.colors["primary"],
                                              hover_color=self.colors["secondary"],
                                              width=100)
                    order_btn.pack(side="right", padx=15)

    def _order_service(self, service):
        window = ctk.CTkToplevel(self.parent)
        window.title(f"Замовлення послуги: {service}")
        window.geometry("400x400")
        window.configure(fg_color=self.colors["bg_dark"])

        title = ctk.CTkLabel(window,
                             text=f"🛍 Замовлення послуги\n{service}",
                             font=("Roboto", 18, "bold"),
                             text_color=self.colors["text"])
        title.pack(pady=20)

        room_frame = ctk.CTkFrame(window, fg_color="transparent")
        room_frame.pack(fill="x", padx=20)

        room_label = ctk.CTkLabel(room_frame,
                                  text="Виберіть номер:",
                                  font=("Roboto", 14),
                                  text_color=self.colors["text"])
        room_label.pack(anchor="w", pady=(0, 5))

        room_var = ctk.StringVar()
        occupied_rooms = [room for room, data in self.hotel.rooms.items()
                          if data["status"] == "зайнятий"]

        room_menu = ctk.CTkOptionMenu(room_frame,
                                      values=occupied_rooms,
                                      variable=room_var,
                                      font=("Roboto", 12),
                                      fg_color=self.colors["secondary"],
                                      button_color=self.colors["primary"],
                                      button_hover_color=self.colors["accent"])
        room_menu.pack(fill="x")

        price_frame = ctk.CTkFrame(window, fg_color=self.colors["bg_light"])
        price_frame.pack(fill="x", padx=20, pady=20)

        service_price = self.hotel.services[service]["price"]
        price_label = ctk.CTkLabel(price_frame,
                                   text=f"Вартість послуги: {service_price} грн",
                                   font=("Roboto", 14),
                                   text_color=self.colors["success"])
        price_label.pack(pady=10)

        def confirm():
            room = room_var.get()
            if room:
                window.destroy()

        confirm_btn = ctk.CTkButton(window,
                                    text="Підтвердити замовлення",
                                    command=confirm,
                                    font=("Roboto", 14),
                                    fg_color=self.colors["success"],
                                    hover_color=self.colors["primary"])
        confirm_btn.pack(pady=20)