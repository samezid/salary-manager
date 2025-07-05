# manager/ratio_loader.py

import json
import os

class RatioLoader:
    def __init__(self, file_path='data/ratios.json'):
        self.file_path = file_path

    def load_ratios(self):
        if not os.path.exists(self.file_path):
            print(f"[ERROR] File rasio tidak ditemukan di: {self.file_path}")
            return {}

        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data.get("default_ratios", {})
        except json.JSONDecodeError:
            print("[ERROR] File rasio tidak dapat dibaca (format JSON salah).")
            return {}
