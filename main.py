class Wrapper:
    def __init__(self, object):
        self.wrapped = object # Сохранить объект
    def __getattr__(self, attrname):
        print("Trace: ", attrname) # Трассировать значение
        return getattr(self.wrapped, attrname) # Делегировать значение

X = Wrapper([1, 2, 3])  # Создать оболочку для списка
X.append(4) # Делегировать списковому методу
print(X.wrapped) # Вывести внутренний объект
Y = Wrapper({"a": 1, "b" : 2}) # Создать оболочку словария
Y.keys() # Делегировать словарному методу
print(Y.wrapped)

