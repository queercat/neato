from typing import List
from gene import Gene
from connection import Connection

import random

class Genome:
  """Represents a neural network."""

  innovation_number = 0
  """Static innovation number used for speciation."""

  def next_innovation_number():
    """Return and increment the static innovation number."""
    Genome.innovation_number += 1
    return Genome.innovation_number - 1

  def __init__(self, genes: List[Gene] = [], connections: List[Connection] = []):
    self.genes = genes
    self.connections = connections

  def __sub__(self, other: 'Genome', c1: float = 1, c2: float = 1, c3: float = 1, N: int = 1) -> float:
    """Caclulate their compatibility distance."""
    left = {}
    right = {}

    for connection in self.connections:
      left[connection.innovation_number] = connection
    
    for connection in other.connections:
      right[connection.innovation_number] = connection

    left_set = set(left.keys())
    right_set = set(right.keys())

    disjoint = left_set.difference(right_set)
    excess = right_set.difference(left_set)

    average_weight_difference = 0

    for connection_id in left_set.intersection(right_set):
      average_weight_difference += abs(left[connection_id].weight - right[connection_id].weight)
    
    average_weight_difference /= len(left_set.intersection(right_set))

    return c1 * len(disjoint) / N + c2 * len(excess) / N + c3 * average_weight_difference


  def __mul__(self, other: 'Genome') -> 'Genome':
    """Cross two genomes."""
    if not isinstance(other, Genome):
      raise ValueError("Multiplicand must be of type Genome.")

    new_genome = Genome()

    left = {}
    right = {}

    for connection in self.connections:
      left[connection.innovation_number] = connection
    
    for connection in other.connections:
      right[connection.innovation_number] = connection

    left_set = set(left.keys())
    right_set = set(right.keys())

    intersected = left_set.intersection(right_set)

    genomes = []
    connections = []

    # For non-disjoint / non-excess choose randomly.
    for connection_id in intersected:
      choices = [left[connection_id], right[connection_id]]

      connections.append(random.choice(choices))

    # For disjoint / excess choose highest fitness.
    for connection_id in left_set.symmetric_difference(right_set):
      # TODO: Calculate fitness
      pass 

    