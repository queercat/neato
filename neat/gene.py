from enum import Enum

class GeneType(Enum):
  INPUT = 0,
  OUTPUT = 1,
  HIDDEN = 2

class Gene:
  def __init__(self, id: str, type: GeneType):
    self.id = id
    self.type = type