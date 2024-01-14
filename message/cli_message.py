from jinja2 import Template
from message.message import MessageData
from typing import List
TEMPLATE = (
    "{% for m in messages %}"
    "-----\n"
    "{% if loop.first %}"
    " /)／)\n"
    "(・　) < Current Schedule {{m.start_date}} - {{m.end_date}}\n"
    " ￣￣\n"
    "ステージ・・・{{m.stage}}\n"
    "偏差値・・・{{m.hyouka}}\n"
    "支給ブキ・・・{{m.weapons_name}}\n"
    "（火力: {{m.hiryoku}}, 塗り: {{m.nuri}}, 機動力: {{m.kidou}},"
    "対雑魚: {{m.zako}}, 対タワー: {{m.tower}}, 対爆弾: {{m.bakudan}}, 耐柱: {{m.hashira}}）\n"
    "{% else %}"
    "{{m.start_date}} - {{m.end_date}}　ステージ: {{m.stage}}　偏差値: {{m.hyouka}}\n"
    "   支給ブキ: {{m.weapons_name}}\n"
    "   （火力: {{m.hiryoku}}, 塗り: {{m.nuri}}, 機動力: {{m.kidou}}, 対雑魚: {{m.zako}}, 対タワー: {{m.tower}}, 対爆弾: {{m.bakudan}}, 耐柱: {{m.hashira}}）\n"
    "{% endif %}"
    "{% endfor %}"
)


class CliMessage:
    @staticmethod
    def create(message_data_list: List[MessageData]) -> str:
        template: Template = Template(source=TEMPLATE)
        return template.render(
            messages=[vars(m_data) for m_data in message_data_list]
        )
