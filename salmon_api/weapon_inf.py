import csv
from dataclasses import dataclass

import numpy as np


@dataclass
class WeaponInf:
    def __init__(self, csv_path: str):
        self._csv_path = csv_path
        self._data: dict = self._load_data()

    def _load_data(self):
        data = {}
        with open(self._csv_path, "r") as f:
            dreader = csv.DictReader(f)
            for row in dreader:
                data[row["name"]] = {**row}
        return data

    def get_weapon_data(self, weapon_name: str) -> dict:
        return self._data[weapon_name]

    def calculate_deviation(self, score: int) -> int:
        np_scores = np.array([int(d["score"]) for d in self._data.values()])
        mean = np.mean(np_scores)
        std = np.std(np_scores)
        deviation = (score - mean) / std
        return int(50 + deviation * 10)
