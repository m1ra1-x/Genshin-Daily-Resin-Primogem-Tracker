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
        
    
