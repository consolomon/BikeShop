iris = {}


def add_iris(id_n: int, species: str, petal_length, petal_width, **kwargs):
    item = {"species": species, "petal_length": petal_length, "petal_width": petal_width}
    for k, v in kwargs.items():
        item[k] = v
    iris[id_n] = item
