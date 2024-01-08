from jinja2 import Template
from message.message import MessageData

TEMPLATE = (
    "-----\n"
    "【{{current_start_date}} - {{current_end_date}}のステージ情報】\n"
    "ステージ [{{current_stage}}]\n"
    "ボス [{{current_boss}}]\n"
    "支給ブキ [{{current_weapons_name}}]\n"
    "武器評価偏差値 [{{current_hyouka}}]\n"
    "（火力:{{hiryoku}}, 塗り:{{nuri}}, 機動力:{{kidou}}, 対雑魚:{{zako}}, 対タワー:{{tower}}, 対爆弾:{{bakudan}}, 耐柱:{{hashira}}）\n"
    "#サーモンラン\n"
    "-----\n"
    "【{{next_start_date}} - {{next_end_date}}のステージ情報】\n"
    "ステージ [{{next_stage}}]\n"
    "ボス [{{next_boss}}]\n"
    "支給ブキ [{{next_weapons_name}}]\n"
    "武器評価偏差値 [{{next_hyouka}}]\n"
    "（火力: {{next_hiryoku}}, 塗り: {{next_nuri}}, 機動力: {{next_kidou}}, 対雑魚: {{next_zako}}, 対タワー: {{next_tower}}, 対爆弾: {{next_bakudan}}, 耐柱: {{next_hashira}}）\n"
    "#サーモンラン\n"
    "-----\n"
    "【{{next_next_start_date}} - {{next_next_end_date}}のステージ情報】\n"
    "ステージ [{{next_next_stage}}]\n"
    "ボス [{{next_next_boss}}]\n"
    "支給ブキ [{{next_next_weapons_name}}]\n"
    "武器評価偏差値 [{{next_next_hyouka}}]\n"
    "（火力: {{next_next_hiryoku}}, 塗り: {{next_next_nuri}}, 機動力: {{next_next_kidou}}, 対雑魚: {{next_next_zako}}, 対タワー: {{next_next_tower}}, 対爆弾: {{next_next_bakudan}}, 耐柱: {{next_next_hashira}}）\n"
    "#サーモンラン\n"
)


class TweetMessage:
    @staticmethod
    def create(m: MessageData) -> str:
        template: Template = Template(source=TEMPLATE)
        return template.render(
            current_start_date=m.current_start_date,
            current_end_date=m.current_end_date,
            current_stage=m.current_stage,
            current_weapons_name=m.current_weapons_name,
            current_hyouka=m.current_hyouka,
            current_boss=m.boss,
            hiryoku=m.hiryoku,
            nuri=m.nuri,
            kidou=m.kidou,
            zako=m.zako,
            tower=m.tower,
            bakudan=m.bakudan,
            hashira=m.hashira,
            next_start_date=m.next_start_date,
            next_end_date=m.next_end_date,
            next_stage=m.next_stage,
            next_hyouka=m.next_hyouka,
            next_boss=m.next_boss,
            next_hiryoku=m.next_hiryoku,
            next_nuri=m.next_nuri,
            next_kidou=m.next_kidou,
            next_zako=m.next_zako,
            next_tower=m.next_tower,
            next_bakudan=m.next_bakudan,
            next_hashira=m.next_hashira,
            next_weapons_name=m.next_weapons_name,
            next_next_start_date=m.next_next_start_date,
            next_next_end_date=m.next_next_end_date,
            next_next_stage=m.next_next_stage,
            next_next_hyouka=m.next_next_hyouka,
            next_next_boss=m.next_next_boss,
            next_next_hiryoku=m.next_next_hiryoku,
            next_next_nuri=m.next_next_nuri,
            next_next_kidou=m.next_next_kidou,
            next_next_zako=m.next_next_zako,
            next_next_tower=m.next_next_tower,
            next_next_bakudan=m.next_next_bakudan,
            next_next_hashira=m.next_next_hashira,
            next_next_weapons_name=m.next_next_weapons_name,
        )
