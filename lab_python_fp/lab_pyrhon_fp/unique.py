
# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        self.index = 0
        self.used = set()
        self.ignore_case = kwargs.get("ignore_case", False)
        self.lower_set = set()
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False

    def __next__(self):
        # Нужно реализовать __next__
        current = None
        while True:
            if isinstance(self.items, list):
                if self.index >= len(self.items):
                    raise StopIteration
                else:
                    current = self.items[self.index]
                    self.index += 1
            else:
                current = next(self.items)

            if not self.ignore_case and current not in self.used:
                self.used.add(current)
                return current
            elif self.ignore_case and isinstance(current, str):
                if current.lower() not in self.lower_set:
                    self.used.add(current)
                    self.lower_set.add(current.lower())
                    return current

    def __iter__(self):
        return self


if __name__ == "__main__":
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(data1)
    '''for i in Unique(data, ignore_case=True):
        print(i)'''
    un1 = Unique(data1)
    for i1 in un1:
        print(i1, end=' ')
    print('\n')

    data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(data2)
    un2 = Unique(data2)
    for i2 in un2:
        print(i2, end=' ')
    print('\n', end='')
    
    un3 = Unique(data2, ignore_case=True)
    for i2 in un3:
        print(i2, end=' ')
    print('\n')
