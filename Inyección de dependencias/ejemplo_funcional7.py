import csv
import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve(strict=True).parent


class App:

    def read(self, file_name):
        temperatures_by_hour = {}
        with open(Path(BASE_DIR).joinpath(file_name), 'r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                hour = datetime.datetime.strptime(row[0], '%d/%m/%Y %H:%M').isoformat()
                temperature = float(row[2])
                temperatures_by_hour[hour] = temperature

        return temperatures_by_hour
