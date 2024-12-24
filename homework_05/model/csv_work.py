from typing import List, Dict
import csv

DATA_FILE = 'data.csv'


class CSVWork:


    @staticmethod
    def write_csv(data: List[Dict[str, str]]):
        """Функция для записи данных в CSV файл"""
        fieldnames = ["id", "title", "date", "pic", "description"]
        with open(DATA_FILE, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)


    @staticmethod
    def read_csv() -> List[Dict[str, str]]:
        """Функция для чтения данных из CSV файла"""
        with open(DATA_FILE, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]

    @staticmethod
    def add_csv(data: Dict[str, str]):
        """Функция для добавления строки в CSV файл"""
        fieldnames = ["id", "title", "event_date", "pic", "description"]
        with open(DATA_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(data)

