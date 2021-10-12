#### EXERCICIO ECORE ####

from operator import itemgetter


people = [{
    "name": "Jean",
    "age": 28
}, {
    "name": "Gustavo",
    "age": 70
}, {
    "name": "Alycio",
    "age": 10
}, {
    "name": "Thiago",
    "age": 26
}]


def add(person):
    people.append(person)


def sort_by_name():
    return sorted(people, key=itemgetter("name"))


def sort_by_age():
    return sorted(people, key=itemgetter("age"))


def classify_by_age(person):
    if person["age"] <= 12:
        return "Criança"
    if person["age"] <= 19:
        return "Adolescente"
    if person["age"] <= 65:
        return "Adulto"
    if person["age"] > 65:
        return "Idoso"


# Execuções para validação

print("People:", people)
print("People sorted by name:", sort_by_name())
print("People sorted by age:", sort_by_age())

print("Adding")

ivone = {"name": "Ivone", "age": 55}
add(ivone)

print("Classification")

for person in people:
    print(person["name"], classify_by_age(person))