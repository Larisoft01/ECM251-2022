from dao.product import ProductDAO
from models.product import Product


class ProductController:
    def __init__(self) -> None:
        pass

    def pickup_item(self, id) -> Product:
        product = ProductDAO.get_instance().pickup_item(id)
        return product

    def insert_item(self, item) -> bool:
        try:
            ProductDAO.get_instance().insert_item(item)
        except:
            return False
        return True

    def pickup_all_items(self) -> list[Product]:
        items = ProductDAO.get_instance().get_all()
        return items
            