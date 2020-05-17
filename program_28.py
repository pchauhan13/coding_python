class Chef:
    def make_chicken(self):
        print("The chef is making chicken")
        return

    def make_salad(self):
        print("The chef is making salad")
        return

    def make_special_dish(self):
        print("The chef is making bbq ribs")
        return

class ChineseChef(Chef):
    def make_fried_rice(self):
        print("The Chinese chef is making fried rice")

my_chef = Chef()
my_chef.make_special_dish()

my_chinese_chef = ChineseChef()
my_chinese_chef.make_fried_rice()
