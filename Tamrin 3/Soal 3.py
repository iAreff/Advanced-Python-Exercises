class ProductPrice:
    def __init__(self, name, *args):
        self.name = name
        self.__product_price_list = []
        self.__product_price_list.extend(args)

    def __str__(self):
        return f'{self.__product_price_list}'

    # def __add__(self, obj):
    #     temp = []
    #     for i in range(len(self.__product_price_list)):
    #         temp.append(self.__product_price_list[i] +
    #                    obj.__product_price_list[i])
    #     return temp

    # def __sub__(self, obj):
    #     temp = []
    #     for i in range(len(self.__product_price_list)):
    #         temp.append(self.__product_price_list[i] -
    #                    obj.__product_price_list[i])
    #     return temp

    # def __mul__(self, obj):
    #     temp = []
    #     for i in range(len(self.__product_price_list)):
    #         temp.append(self.__product_price_list[i]
    #                    * obj.__product_price_list[i])
    #     return temp

    # def __truediv__(self, obj):
    #     temp = []
    #     for i in range(len(self.__product_price_list)):
    #         temp.append(self.__product_price_list[i] /
    #                    obj.__product_price_list[i])
    #     return temp

    # def __lt__(self, obj):
    #     a, b = 0, 0
    #     for i in range(len(self.__product_price_list)):
    #         if self.__product_price_list[i] < obj.__product_price_list[i]:
    #             a += 1
    #         elif self.__product_price_list[i] > obj.__product_price_list[i]:
    #             b += 1
    #     if a > b:
    #         return f'{self.name} is a more efficient shop'
    #     elif b > a:
    #         return f'{obj.name} is a more efficient shop'

    # def __len__(self):
    #     return len(self.__product_price_list)

    def off(self, percent):
        self.__previous_prices = self.__product_price_list.copy()
        off_amount = (100 - percent) / 100
        for i in range(len(self.__product_price_list)):
            self.__product_price_list[i] *= off_amount
            self.__product_price_list[i] = int(self.__product_price_list[i])

    def remove_off(self):
        if self.__previous_prices:
            self.__product_price_list = self.__previous_prices

    def average_price(self):
        return sum(self.__product_price_list) // len(self.__product_price_list)

    @staticmethod
    def compare(shop1, shop2):
        a, b = 0, 0
        for i in range(len(shop1.__product_price_list)):
            if shop1.__product_price_list[i] < shop2.__product_price_list[i]:
                a += 1
            elif shop1.__product_price_list[i] > shop2.__product_price_list[i]:
                b += 1
        if a > b:
            return f'{shop1.name} is a more efficient shop'
        elif b > a:
            return f'{shop2.name} is a more efficient shop'
        return f'Both Shops are the same'

#-------------------------------------------------------

shop1 = ProductPrice('Refah', 5000, 10000, 15000, 6000, 25000, 12000, 14000, 10000, 7000, 20000)
shop2 = ProductPrice('Ofogh Koorosh', 4000, 12000, 16000, 5000, 22000, 10000, 16000, 11000, 5000, 18000)

# print(shop1 + shop2)
# print(shop1 - shop2)
# print(shop1 * shop2)
# print(shop1 / shop2)
# print(shop1 < shop2)

print(ProductPrice.compare(shop1, shop2))

print(shop1)
print(f'Refah Shop Average Products Price without off: {shop1.average_price()}')
print(shop2)
print(f'Ofogh Koorosh Shop Average Products Price without off: {shop2.average_price()}')

shop1.off(20)
shop2.off(20)
print(shop1)
print(f'Refah Shop Average Products Price with off: {shop1.average_price()}')
print(shop2)
print(f'Ofogh Koorosh Shop Average Products Price with off: {shop2.average_price()}')

shop1.remove_off()
shop2.remove_off()
print(shop1)
print(shop2)