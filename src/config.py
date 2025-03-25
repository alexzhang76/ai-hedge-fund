from enum import Enum
from dataclasses import dataclass

class Language(Enum):
    ENGLISH = "en"
    CHINESE = "zh"

@dataclass
class Config:
    language: Language = Language.ENGLISH

config = Config() 