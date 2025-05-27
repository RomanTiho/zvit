from utils.data_manager import DataManager

class Hotel:
    def __init__(self):
        self.data_manager = DataManager()

        # Load data from JSON files or use defaults
        self.rooms = self.data_manager.load_data('rooms_dict')
        if not self.rooms:
            self.rooms = {
                f"{i}": {
                    "type": "Стандарт",
                    "price": 1000,
                    "status": "вільний",
                    "cleaning_status": "чистий",
                    "maintenance": False,
                    "equipment": ["TV", "Кондиціонер", "Міні-бар", "Wi-Fi"],
                    "description": "Зручний номер з усіма необхідними зручностями"
                } for i in range(101, 111)
            }
            self.rooms.update({
                f"{i}": {
                    "type": "Люкс",
                    "price": 2000,
                    "status": "вільний",
                    "cleaning_status": "чистий",
                    "maintenance": False,
                    "equipment": ["TV", "Кондиціонер", "Міні-бар", "Wi-Fi", "Джакузі", "Міні-кухня"],
                    "description": "Розкішний номер з додатковими зручностями"
                } for i in range(201, 206)
            })
            self.save_rooms()

        self.bookings = self.data_manager.load_data('bookings_dict')
        self.guests = self.data_manager.load_data('guests_dict')

        self.services = self.data_manager.load_data('services_dict')
        if not self.services:
            self.services = {
                "Сніданок": {"price": 200, "type": "Харчування", "description": "Континентальний сніданок"},
                "Обід": {"price": 300, "type": "Харчування", "description": "Триразове харчування"},
                "Вечеря": {"price": 250, "type": "Харчування", "description": "Спеціальне меню"},
                "Спа": {"price": 500, "type": "Відпочинок", "description": "Масаж та спа-процедури"},
                "Пральня": {"price": 150, "type": "Побутові", "description": "Прання та прасування"},
                "Трансфер": {"price": 400, "type": "Транспорт", "description": "Трансфер з/до аеропорту"},
                "Конференц-зал": {"price": 1000, "type": "Бізнес", "description": "Оренда конференц-залу"},
                "Room Service": {"price": 350, "type": "Харчування", "description": "Доставка їжі в номер"},
                "Екскурсія": {"price": 600, "type": "Розваги", "description": "Екскурсія по місту"}
            }
            self.save_services()

        self.maintenance_schedule = self.data_manager.load_data('maintenance_schedule_dict')
        self.cleaning_schedule = self.data_manager.load_data('cleaning_schedule_dict')

    def save_rooms(self):
        """Save rooms data to JSON"""
        self.data_manager.save_data('rooms_dict', self.rooms)

    def save_bookings(self):
        """Save bookings data to JSON"""
        self.data_manager.save_data('bookings_dict', self.bookings)

    def save_guests(self):
        """Save guests data to JSON"""
        self.data_manager.save_data('guests_dict', self.guests)

    def save_services(self):
        """Save services data to JSON"""
        self.data_manager.save_data('services_dict', self.services)

    def save_maintenance_schedule(self):
        """Save maintenance schedule to JSON"""
        self.data_manager.save_data('maintenance_schedule_dict', self.maintenance_schedule)

    def save_cleaning_schedule(self):
        """Save cleaning schedule to JSON"""
        self.data_manager.save_data('cleaning_schedule_dict', self.cleaning_schedule)

    def save_all(self):
        """Save all data to JSON files"""
        self.save_rooms()
        self.save_bookings()
        self.save_guests()
        self.save_services()
        self.save_maintenance_schedule()
        self.save_cleaning_schedule() 