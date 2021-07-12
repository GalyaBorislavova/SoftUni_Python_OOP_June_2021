class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name: str):
        product_with_this_name = [p for p in self.products if p.name == product_name]
        if product_with_this_name:
            return product_with_this_name[0]

    def remove(self, product_name: str):
        searched_product = [p for p in self.products if p.name == product_name]
        if searched_product:
            self.products.remove(searched_product[0])

    def __repr__(self):
        return '\n'.join([f"{p.name}: {p.quantity}" for p in self.products])


# product_repo = ProductRepository()
#
# apple = Food("apple")
# banana = Food("banana")
# water = Drink("water")
#
# product_repo.add(apple)
# product_repo.add(banana)
# product_repo.add(water)
#
# print(product_repo)
#
# print(product_repo.find("water"))
# product_repo.remove("apple")
#
# print(product_repo)