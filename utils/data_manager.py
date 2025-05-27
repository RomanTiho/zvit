import json
import os

class DataManager:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self._ensure_data_directory()

    def _ensure_data_directory(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def save_data(self, filename, data):
        try:
            filepath = os.path.join(self.data_dir, f"{filename}.json")
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            print(f"Помилка при збереженні даних у файл {filename}: {str(e)}")
            return False

    def load_data(self, filename):
        try:
            filepath = os.path.join(self.data_dir, f"{filename}.json")
            if not os.path.exists(filepath):
                return {} if filename.endswith('_dict') else []

            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Помилка при завантаженні даних з файлу {filename}: {str(e)}")
            return {} if filename.endswith('_dict') else []