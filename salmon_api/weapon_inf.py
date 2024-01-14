import csv
from dataclasses import dataclass

import numpy as np

class UnknownWeaponError(Exception):
    pass

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
        try:
            return self._data[weapon_name]
        except KeyError:
            if weapon_name == 'ランダム':
                median_score = np.median([int(d["score"]) for d in self._data.values()])
                return {
                    'name' : 'ランダム',
                    'hi' : 3.5,
                    'nuri' : 3.5,
                    'kidou' : 3.5,
                    'zako' : 3.5,
                    'tower' : 3.5,
                    'bakudan' : 3.5,
                    'hashira' : 3.5,
                    'score': median_score
                }
            raise UnknownWeaponError(f'weapon_name: {weapon_name}')

    def calculate_deviation(self, score: int) -> int:
        array= [int(d["score"]) for d in self._data.values()]
        mean = np.mean(array)
        std = np.std(array)
        deviation = (score - mean) / std
        return int(50 + deviation * 10)
