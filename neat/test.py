from genome import Genome
from gene import Gene, GeneType
from connection import Connection

genes = {
  1: Gene(1, GeneType.INPUT),
  2: Gene(2, GeneType.INPUT),
  3: Gene(3, GeneType.INPUT),
  4: Gene(4, GeneType.OUTPUT),
  5: Gene(5, GeneType.HIDDEN)
}

connections = [
  Connection(1, 4, .7, True, 1),
  Connection(2, 4, -.5, False, 2),
  Connection(3, 4, .5, True, 3),
  Connection(2, 5, .2, True, 4),
  Connection(1, 5, .6, True, 6),
  Connection(4, 5, .6, True, 11)
]

genome = Genome(genes, connections)

print(genome)