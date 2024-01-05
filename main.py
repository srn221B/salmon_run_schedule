import argparse
import os
from pathlib import Path
from typing import List

from message.cli_message import CliMessage
from message.message import MessageData
from message.slack_message import SlackMessage
from notice.slack import Slack
from salmon_api.salmon_api import SalmonAPI, SalmonAPIRawData

################
#    設定       #
################
SCRAPING_URL = "https://spla3.yuu26.com/api/coop-grouping/schedule"
WEAPON_INF_CSV_FILENAME = "weapon_inf.csv"


class SalmonApiRawDataToMessageData:
    @staticmethod
    def convert(raw_data: List[SalmonAPIRawData]) -> MessageData:
        current_data, next_data, next_next_data = raw_data[0], raw_data[1], raw_data[2]
        c_weapons, n_weapons, n_n_weapons = current_data.weapons, next_data.weapons, next_next_data.weapons
        return MessageData(
            current_start_date=current_data.start_time,
            current_end_date=current_data.end_time,
            current_stage=current_data.stage,
            current_weapons_name=", ".join(c_weapons.name_list),
            current_hyouka=current_data.get_deviation(int(sum(c_weapons.score_list) / len(c_weapons.score_list))),
            hiryoku=round(sum(c_weapons.hiryoku_list) / len(c_weapons.hiryoku_list), 1),
            nuri=round(sum(c_weapons.nuri_list) / len(c_weapons.nuri_list), 1),
            kidou=round(sum(c_weapons.kidou_list) / len(c_weapons.kidou_list), 1),
            zako=round(sum(c_weapons.zako_list) / len(c_weapons.zako_list), 1),
            tower=round(sum(c_weapons.tower_list) / len(c_weapons.tower_list), 1),
            bakudan=round(sum(c_weapons.bakudan_list) / len(c_weapons.bakudan_list), 1),
            hashira=round(sum(c_weapons.hashira_list) / len(c_weapons.hashira_list), 1),
            next_start_date=next_data.start_time,
            next_end_date=next_data.end_time,
            next_stage=next_data.stage,
            next_hyouka=next_data.get_deviation(int(sum(n_weapons.score_list) / len(n_weapons.score_list))),
            next_hiryoku=round(sum(n_weapons.hiryoku_list) / len(n_weapons.hiryoku_list), 1),
            next_nuri=round(sum(n_weapons.nuri_list) / len(n_weapons.nuri_list), 1),
            next_kidou=round(sum(n_weapons.kidou_list) / len(n_weapons.kidou_list), 1),
            next_zako=round(sum(n_weapons.zako_list) / len(n_weapons.zako_list), 1),
            next_tower=round(sum(n_weapons.tower_list) / len(n_weapons.tower_list), 1),
            next_bakudan=round(sum(n_weapons.bakudan_list) / len(n_weapons.bakudan_list), 1),
            next_hashira=round(sum(n_weapons.hashira_list) / len(n_weapons.hashira_list), 1),
            next_weapons_name=", ".join(n_weapons.name_list),
            next_next_start_date=next_next_data.start_time,
            next_next_end_date=next_next_data.end_time,
            next_next_stage=next_next_data.stage,
            next_next_hyouka=next_next_data.get_deviation(int(sum(n_n_weapons.score_list) / len(n_n_weapons.score_list))),
            next_next_hiryoku=round(sum(n_n_weapons.hiryoku_list) / len(n_n_weapons.hiryoku_list), 1),
            next_next_nuri=round(sum(n_n_weapons.nuri_list) / len(n_n_weapons.nuri_list), 1),
            next_next_kidou=round(sum(n_n_weapons.kidou_list) / len(n_n_weapons.kidou_list), 1),
            next_next_zako=round(sum(n_n_weapons.zako_list) / len(n_n_weapons.zako_list), 1),
            next_next_tower=round(sum(n_n_weapons.tower_list) / len(n_n_weapons.tower_list), 1),
            next_next_bakudan=round(sum(n_n_weapons.bakudan_list) / len(n_n_weapons.bakudan_list), 1),
            next_next_hashira=round(sum(n_n_weapons.hashira_list) / len(n_n_weapons.hashira_list), 1),
            next_next_weapons_name=", ".join(n_n_weapons.name_list),
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", help="通知先[slack or cli or all] 指定しない場合はall", default="all", type=str)
    args = parser.parse_args()
    notice_type = args.type

    if notice_type == "slack" or notice_type == "all":
        SLACK_TOKEN = os.environ["SLACK_TOKEN"]
        SLACK_CHANNEL = os.environ["SLACK_CHANNEL"]
    RESOURCE_DIR_PATH = os.environ["RESOURCE_DIR_PATH"]

    weapon_inf_csv_filepath = str(Path(RESOURCE_DIR_PATH, WEAPON_INF_CSV_FILENAME))

    salmon_api = SalmonAPI(SCRAPING_URL, weapon_inf_csv_filepath)
    salmon_api_raw_data = salmon_api.get_3days_raw_data()
    message_data = SalmonApiRawDataToMessageData.convert(salmon_api_raw_data)

    if notice_type == "slack" or notice_type == "all":
        slack_message = SlackMessage.create(message_data)
        slack = Slack(SLACK_TOKEN, SLACK_CHANNEL)
        slack.post(slack_message)

    if notice_type == "cli" or notice_type == "all":
        cli_message = CliMessage.create(message_data)
        print(cli_message)
