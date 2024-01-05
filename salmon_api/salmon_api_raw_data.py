from dataclasses import dataclass
from datetime import datetime
from typing import List

from salmon_api.weapon_inf import WeaponInf


@dataclass
class RawWeapon:
    name: str
    hi: str
    nuri: str
    kidou: str
    zako: str
    tower: str
    bakudan: str
    hashira: str
    score: str


@dataclass
class Weapons:
    def __init__(self, raw_weapons: List[RawWeapon]):
        self._raw_weapons: List[RawWeapon] = raw_weapons
        self.name_list: List[str] = []
        self.hiryoku_list: List[float] = []
        self.nuri_list: List[float] = []
        self.kidou_list: List[float] = []
        self.zako_list: List[float] = []
        self.tower_list: List[float] = []
        self.bakudan_list: List[float] = []
        self.hashira_list: List[float] = []
        self.score_list: List[float] = []
        self._load()

    def _load(self):
        for w in self._raw_weapons:
            self.name_list.append(w.name)
            self.hiryoku_list.append(float(w.hi))
            self.nuri_list.append(float(w.nuri))
            self.kidou_list.append(float(w.kidou))
            self.zako_list.append(float(w.zako))
            self.tower_list.append(float(w.tower))
            self.bakudan_list.append(float(w.bakudan))
            self.hashira_list.append(float(w.hashira))
            self.score_list.append(float(w.score))

    def __len__(self):
        return len(self._weapons)


@dataclass
class SalmonAPIRawData:
    _start_time: str
    _end_time: str
    _stage: str
    _boss: dict
    _weapons: List[dict]
    _weapon_inf: WeaponInf

    @property
    def start_time(self):
        st_dt = datetime.fromisoformat(self._start_time)
        return f"{st_dt.year}-{st_dt.month}-{st_dt.day} {st_dt.hour}:00"

    @property
    def end_time(self):
        et_dt = datetime.fromisoformat(self._start_time)
        return f"{et_dt.year}-{et_dt.month}-{et_dt.day} {et_dt.hour}:00"

    @property
    def stage(self):
        return self._stage["name"]

    @property
    def boss(self) -> str:
        return self._boss[0]["name"]

    @property
    def weapons(self) -> Weapons:
        return Weapons([RawWeapon(**self._weapon_inf.get_weapon_data(weapon["name"])) for weapon in self._weapons])

    def get_deviation(self, total_score: int) -> int:
        return self._weapon_inf.calculate_deviation(total_score)
