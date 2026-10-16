import json
import os
from datetime import datetime, timedelta 

class GenshinTracker:
    def _init_(self, filename="tracker_data_json'):
              self.filename = filename
              self.data = self.load_data()

