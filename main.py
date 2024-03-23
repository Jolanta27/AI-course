x = 42
print(x)

x = 3.14
print(x)

text = "hello world"
print(text)

a = complex(1, 3)
print(a) 
# creating a complex number

secondText = """Hello World
And Mars!"""
print(secondText)
print(5 * text)
print(text[0])
size = len(text)
print(size)
print(text[size - 1])
print(text[1:5]) # without 5
print(text[1:4:2])
print(text[:8])
print(text[2:])
print(text[::2])
print(text[: size//2]) #return half part of str
print(text[size//2:]) #return second part of str
stundets = [
    "Justyna Janczur",
    "Mariusz Hanclik",
    "Tomasz Skawiński",
    "Błażej Grela",
    "Dawid Maciej Prażmo",
    "Piotr  Gaszczyk",
    "Monika Fajfer-Jakubek",
    "Jolanta Galczynska",
    "Mateusz  Lipiński",
    "Ernest Antczak",
    "Dawid Koźmiński",
    "Marcin  Wiktorowicz",
    "Marcin Bednarski",
    "Krzysztof Wysocki",
    "Lilianna Gołaszewska",
    "Agnieszka Chojka",
    "Magdalena Biszczuk",
    "Katarzyna Dudziak-Wożnicka",
    "Ilona Semkowicz",
    "Urszuła Głuch",
    "Mateusz  Plewa",
    "Jakub Gołębiewski",
    "Robert Relidzynski",
    "Rafał Pańkowski",
]

print(stundets)
scores = [90, 80, 70, 60, 50]
print(70 in scores)
scores.append(40)
print(scores)
scores.copy()
print(scores)
scores.insert(1, 100)
print(scores)
print(scores.count(90))
scores.extend([40, 30, 20, 10])
print(scores)

phones = {
    "John Doe": "123-456-789",
    "John Domber": "098-765-4321",
    "John Smith": "321-656-324",
}
phones["Justin Time"] = "123-456-789"
print(phones["John Doe"])
print(phones)
