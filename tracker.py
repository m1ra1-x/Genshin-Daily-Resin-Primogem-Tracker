import json
import os
from datetime import datetime, timedelta 

class GenshinTracker:
    def _init_(self, filename="tracker_data_json'):
              self.filename = filename
              self.data = self.load_data()

    def load_data (self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Data if file is corrupted or missing
            return {
                "last_resin_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "current_resin": 0,
                "primogems": 0,
                "goal_primogems": 16000
            }

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)

    def update_resin(self):
        last_update = datetime.strptime(self.data['last_resin_update'], %Y-%m-%d %H:5M:%S")
        now = datatime.now()

        diff = now - last_update
        minutes_elapsed = diff.total_seconds() // 60
        resin_gained = int(minutes_elapsed // 8)

        if resin_gained > 0:
            self.data['current_resin'] = min(160, self.data['current_resin'] + resin_gained)
            remaining_minutes = minutes_elapsed % 8
            new_time = now - timedelta (minutes=remaining_minutes)
            self.data['last_resin_update'] = new_time.strftime("%Y-%m-%d %H:%M:%S")
            self.save_data()
            return resin_gained
        return 0

    def update_primogems(self, amount):
        self.data['primogems'] += amount
        self.save_data()

    def get_status(self):
        gained = self.update_resin()
        resin = self.data['current_resin']
        pems = self.data['primogems']
        goal = self.data['goal_primogems']

        progress = (pems / goal) * 100 if goal > 0 else 0

        status = (
            f"Current Resin: {resin]/160 "
            f"({'+' if gained > 0 else ''}{gained} regenerated since last check)\n"
            f"Primogems: {pems} / {goal}\n"
            f"Savings Progress: {progress:.2f}%\n"
        )
        return status 

    def main():
        tracker = GenshinTracker()

        while True:
            print("\n1. View Status\n2. Update Resin (Spend)\n3. Add/Subtract Primogems\n4. Set Goal\n5. Exit")
            Choice = input("Select an Option: ")

            if choice == '1':
                print(tracker.get_status())
            elif choice == '2':
                try:
                    
