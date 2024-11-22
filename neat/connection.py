class Connection:
  def __init__(self, input_node: int, output_node: int, weight: float = 0, enabled: bool = True, innovation_number: int = 0):
    self.input_node = input_node
    self.output_node = output_node
    self.weight = weight
    self.enabled = enabled
    self.innovation_number = innovation_number
    