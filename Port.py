class Port:
    def __init__(self, model, name:str):
        self.model = model
        self.name : str = name

    def __eq__(self, other):
        if isinstance(other, Port):  return (self.name == other.name and self.model.name == other.model.name)
        else: raise NotImplementedError()

    def __hash__(self):
        return hash((self.model.name, self.name))
