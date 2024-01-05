from typing import List

import requests
from salmon_api.salmon_api_raw_data import SalmonAPIRawData, WeaponInf


class SalmonAPI:
    def __init__(self, scraping_url: str, weapon_inf_csv_filepath: str):
        self.scraping_url = scraping_url
        self.weapon_inf_csv_filepath = weapon_inf_csv_filepath

    def get_3days_raw_data(self) -> List[SalmonAPIRawData]:
        result = []
        res = requests.get(self.scraping_url)
        res_json = res.json()
        try:
            for r in res_json["results"][0:3]:
                result.append(
                    SalmonAPIRawData(
                        r["start_time"],
                        r["end_time"],
                        r["stage"],
                        r["boss"],
                        r["weapons"],
                        WeaponInf(self.weapon_inf_csv_filepath),
                    )
                )
            return result
        except Exception as e:
            raise Exception(f"api format error {res_json}: {e}")
