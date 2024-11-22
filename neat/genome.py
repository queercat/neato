from typing import List
from gene import Gene
from connection import Connection

class Genome:
  def __init__(self, genes: List[Gene] = [], connections: List[Connection] = []):
    self.genes = genes
    self.connections = connections