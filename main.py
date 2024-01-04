import os
from dataclasses import dataclass
from typing import List

import requests
from bs4 import BeautifulSoup
from slack_message import SlackMessage

SCRAPING_URL = "https://splatoon.caxdb.com/splatoon3/coop_schedule3.cgi"


@dataclass
class PostRawData:
    schedule_interval_start_date: str
    schedule_interval_start_hour: str
    schedule_interval_end_date: str
    schedule_interval_end_hour: str
    stage: str
    weapons: List[str]


class SalmonRunSchedule:
    def _check_format(self, base_contents: List[str]) -> None:
        try:
            if base_contents[5] != "ステージ" and base_contents[7] != "支給ブキ":
                raise Exception()
        except Exception as e:
            raise Exception(f"ソース情報フォーマットエラー: {e}")

    def get_current_post_raw_data(self) -> PostRawData:
        res = requests.get(SCRAPING_URL)
        soup = BeautifulSoup(res.text, "html.parser")
        base_contents = soup.find("li").get_text().split()
        self._check_format(base_contents)
        return PostRawData(
            base_contents[0], base_contents[1], base_contents[3], base_contents[4], base_contents[6], base_contents[8:]
        )


if __name__ == "__main__":
    SLACK_TOKEN = os.environ["SLACK_TOKEN"]
    SLACK_CHANNEL = os.environ["SLACK_CHANNEL"]
    print(f"slack_token: {SLACK_TOKEN}")
    print(f"slack_channel: {SLACK_CHANNEL}")

    salmon_run_schedule = SalmonRunSchedule()
    post_raw_data = salmon_run_schedule.get_current_post_raw_data()
    slack_message = SlackMessage(SLACK_TOKEN, SLACK_CHANNEL)
    weapons_text = ",".join(post_raw_data.weapons)
    text = (
        f":candy: *Current Schedule {post_raw_data.schedule_interval_start_date} {post_raw_data.schedule_interval_start_hour} - {post_raw_data.schedule_interval_end_date} {post_raw_data.schedule_interval_end_hour}* :candy: \n"
        + f"ステージ: {post_raw_data.stage}\n"
        + f"支給ブキ: {weapons_text}"
    )
    slack_message.post(text)
