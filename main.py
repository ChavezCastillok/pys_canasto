from pyscript import when, document


class Product:
    def __init__(self, code, description, creation_date="Dec 2") -> None:
        self.code = code
        self.description = description
        self.creation_date = creation_date

    def __str__(self) -> str:
        return f"{str(self.code).zfill(6)}: {self.description}"


with open("lista.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)


myList = [
    Product(1, "Harina Pan 1kg"),
    Product(433, "Papa p/k"),
    Product(467, "Huevos x15"),
    Product(3783, "Jabon de baño Natural Feeling x1"),
]
my_element = document.querySelector("#my-list")

inputSearch = document.querySelector("#search")


def update_list(items):
    my_element.innerHTML = ""
    for item in items:
        my_element.innerHTML += f"<li>{item}</li>"


@when("click", "#search")
def reset(event):
    inputSearch.value = ""
    update_list(myList)


@when("input", "#search")
def result_search(event):
    list = []
    term = inputSearch.value
    for item in myList:
        if term.lower() in item.description.lower():
            list.append(item)
        update_list(list)


print("abrimos para grabar nuevos datos")
with open("lista.txt", "a") as archivo:
    archivo.write("421, tomate\n")

print("volvemos a abrir el archivo para ver el content")
with open("lista.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
