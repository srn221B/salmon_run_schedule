import argparse
import os
from pathlib import Path
from typing import List

from message.cli_message import CliMessage
from message.csv_message import CsvMessage
from message.message import MessageData
from message.slack_message import SlackMessage
from message.tweet_message import TweetMessage
from notice.slack import Slack
from salmon_api.salmon_api import SalmonAPI, SalmonAPIRawData

################
#    設定       #
################
SCRAPING_URL = "https://spla3.yuu26.com/api/coop-grouping/schedule"
WEAPON_INF_CSV_FILENAME = "weapon_inf.csv"


class SalmonApiRawDataToMessageData:
    @staticmethod
    def convert_message_data_list(raw_data_list: List[SalmonAPIRawData]) -> List[MessageData]:
        message_data_list = []
        for r in raw_data_list:
            weapons = r.weapons
            message_data_list.append(
                MessageData(
                    start_date=r.start_time,
                    end_date=r.end_time,
                    stage=r.stage,
                    weapons_name=", ".join(weapons.name_list),
                    hyouka=r.get_deviation(int(sum(weapons.score_list) / len(weapons.score_list))),
                    boss=r.boss,
                    hiryoku=round(sum(weapons.hiryoku_list) / len(weapons.hiryoku_list), 1),
                    nuri=round(sum(weapons.nuri_list) / len(weapons.nuri_list), 1),
                    kidou=round(sum(weapons.kidou_list) / len(weapons.kidou_list), 1),
                    zako=round(sum(weapons.zako_list) / len(weapons.zako_list), 1),
                    tower=round(sum(weapons.tower_list) / len(weapons.tower_list), 1),
                    bakudan=round(sum(weapons.bakudan_list) / len(weapons.bakudan_list), 1),
                    hashira=round(sum(weapons.hashira_list) / len(weapons.hashira_list), 1),
                )
            )
        return message_data_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", help="通知先[slack or cli or tweet csv or all] 指定しない場合はall", default="all", type=str)
    args = parser.parse_args()
    notice_type = args.type

    if notice_type == "slack" or notice_type == "all":
        SLACK_TOKEN = os.environ["SLACK_TOKEN"]
        SLACK_CHANNEL = os.environ["SLACK_CHANNEL"]
    if notice_type == "csv" or notice_type == "all":
        CSV_DIR_PATH = os.environ["CSV_DIR_PATH"]
    RESOURCE_DIR_PATH = os.environ["RESOURCE_DIR_PATH"]

    weapon_inf_csv_filepath = str(Path(RESOURCE_DIR_PATH, WEAPON_INF_CSV_FILENAME))

    salmon_api = SalmonAPI(SCRAPING_URL, weapon_inf_csv_filepath)
    salmon_api_raw_data = salmon_api.get_3days_raw_data()
    message_data_list = SalmonApiRawDataToMessageData.convert_message_data_list(salmon_api_raw_data)

    if notice_type == "slack" or notice_type == "all":
        slack_message = SlackMessage.create(message_data_list)
        slack = Slack(SLACK_TOKEN, SLACK_CHANNEL)
        slack.post(slack_message)

    if notice_type == "cli" or notice_type == "all":
        cli_message = CliMessage.create(message_data_list)
        print(cli_message)

    if notice_type == "tweet" or notice_type == "all":
        cli_message = TweetMessage.create(message_data_list)
        print(cli_message)

    if notice_type == "csv" or notice_type == "all":
        csv_message = CsvMessage(CSV_DIR_PATH)
        csv_message.write(message_data_list)
