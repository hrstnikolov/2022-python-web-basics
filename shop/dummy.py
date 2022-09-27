class Person:
    other_name = "Default"

    def __init__(self, name):
        self.name = name


def get_attributes(obj):
    return {k: v for k, v in obj.__dict__.items() if not k.startswith("_")}


ivo = Person("Ivo")
Person.other_name = "Evlogii"
Person.name = "Atanas"
emo = Person("Emo")

for obj in [ivo, Person, emo]:
    print(get_attributes(obj))

print(ivo.__class__.other_name)



