from dataclasses import dataclass


@dataclass
class MessageData:
    start_date: str
    end_date: str
    stage: str
    weapons_name: str
    hyouka: int
    boss: str
    hiryoku: float
    nuri: float
    kidou: float
    zako: float
    tower: float
    bakudan: float
    hashira: float
