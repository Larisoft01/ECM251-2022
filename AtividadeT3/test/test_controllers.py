from src.controllers.productcontroller import ItemController
from AtividadeT3.src.models.product import Product

controller = ItemController()
items = controller.pegar_todos_itens()
for item in items:
    print(item)

novo_item = Product("OLA1", "Cooler REDRAGON Vermelho", 19.90)
print(controller.inserir_item(novo_item))

print("**************************************")
items = controller.pegar_todos_itens()
for item in items:
    print(item)

print("**************************************")
item = controller.pegar_item("CAF6")
print(item)