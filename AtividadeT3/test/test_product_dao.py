
from src.dao.product import ProductDAO

items = ProductDAO.get_instance().get_all()

print(items)
for Product in items:
    print(Product)