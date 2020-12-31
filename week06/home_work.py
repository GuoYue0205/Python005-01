# 背景：在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求定义动物园、动物、猫、狗四个类。
# 这个类可以使用如下形式为动物园增加一只猫：

# 具体要求：
# 定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
# 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
# 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
# 动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。


from abc import ABCMeta,abstractmethod
import threading
def animal_size(x):
    return{
        '小':1,
        '中等':2,
        '大':3,
    }.get(x,0)

class Zoo(object):
    def __init__(self,name):
        self.name = name
    
    # “添加动物”方法
    def add_animal(self, object):
        # “添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能
        if isinstance(object,Cat):
            if not hasattr(self, 'Cat'):
                self.Cat = object
    
        elif isinstance(object,Dog):
            if not hasattr(self, 'Dog'):
                self.dog = object

        else:
            pass
            

# 动物类不允许被实例化 加入mataclass
class Animal(metaclass=ABCMeta):
    # 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性
    def __init__(self,animal_type,shape,character):
        self.animal_type = animal_type   # 类型
        self.shape = shape  # 体型
        self.character = character  # 性格

    # 是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”
    @property
    def is_ferocious(self):
        if self.animal_type == '食肉类型' and self.character == '凶猛' and animal_size(self.shape)>=1:
            return True
        else:
            return False
    
    @abstractmethod
    def eat(self):
        pass

class Cat(Animal):
    # 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性
    def __init__(self,name,animal_type,character,shape):
        super(Cat,self).__init__(animal_type,shape,character)
        self.name = name #名字
    # 是否适合作为宠物
    @property
    def is_suitable_for_pets(self):
        if self.character != '凶猛':
            return True
        else:
            return False
    # “叫声”作为类属性
    calls = '喵'

    def eat(self):
        print('eat')

class Dog(Animal):
    def __init__(self,name,animal_type,character,shape):
        super(Dog,self).__init__(animal_type,shape,character)
        self.name = name
    
    # 是否适合作为宠物
    @property
    def is_suitable_for_pets(self):
        if self.character != '凶猛':
            return True
        else:
            return False
    # “叫声”作为类属性
    calls = '旺'

    def eat(self):
        print('eat')


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # print(z.name)
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # print(cat1.name)
    # print(cat1.is_ferocious)
    # print(cat1.animal_type)
    # print(cat1.shape)
    # print(cat1.character)
    # print(cat1.is_suitable_for_pets)
    # print(Cat.calls)
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # print(z.Cat)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(have_cat)