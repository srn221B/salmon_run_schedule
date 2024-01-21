import csv
import os
from datetime import datetime
from pathlib import Path
from typing import List

from message.message import MessageData

CSV_HEADER = [
    [
        "start_date",
        "end_date",
        "stage",
        "weapons_name1",
        "weapons_name2",
        "weapons_name3",
        "weapons_name4",
        "hyouka",
        "boss",
        "hiryoku",
        "nuri",
        "kidou",
        "zako",
        "tower",
        "bakudan",
        "hashira",
    ]
]


class CsvMessage:
    def __init__(self, csv_dir_path: str):
        self.csv_dir_path = csv_dir_path

    def write(self, message_data_list: List[MessageData]) -> str:
        current_year = datetime.now().year
        current_month = datetime.now().month
        target_filepath = str(Path(self.csv_dir_path, f"{current_year}{current_month}.csv"))
        print(f"target_filepath: {target_filepath}")
        if not os.path.exists(os.path.dirname(target_filepath)):
            raise Exception("dir_path is not exists")
        if not os.path.exists(target_filepath):
            with open(target_filepath, "w") as f:
                writer = csv.writer(f)
                writer.writerows(CSV_HEADER + [vars(m).values() for m in message_data_list])
        else:
            with open(target_filepath, "a") as f:
                writer = csv.writer(f)
                writer.writerows([vars(m).values() for m in message_data_list])
