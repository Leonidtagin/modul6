class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}\n'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
    
    def get_products(self):
            file = open(self.__file_name, 'r')
            data = file.read()
            file.close()
            return data

    def add(self, *products):
            for product in products:
                if product.name not in products:
                   file = open(self.__file_name, 'a')
                   file.write(product.__str__())
                   file.close()
                elif product.name in product:
                    print(f'Продукт{product.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Spaghetti', 3.4, 'Groceries')
p2 = Product('Potato', 50.5, 'Vegetable')
p3 = Product('Potato', 5.5, 'Vegetable')

s1.add(p1)
s1.add(p2)
s1.add(p3)



print(p1)
print(p2)
print(p3)

print(s1.get_products())

