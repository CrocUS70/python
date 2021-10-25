# используется для сортировки
from operator import itemgetter

"""Деталь"""
class Detail:
    def __init__(self, id, name1, price, provider_id):
        self.id=id
        self.name1=name1
        self.price=price
        self.provider_id=provider_id

"""Поставщик"""
class Provider:
    def __init__(self, id, name):
        self.id=id
        self.name=name
        
"""Детали поставщика"""
class DetailProvider:
    def __init__(self, provider_id, detail_id):
        self.provider_id=provider_id
        self.detail_id=detail_id

#поставщики (id поставщика, название поставщика)
providers=[Provider(1,'АвтоСпейс'),
Provider(2,'Favorit-auto'),
Provider(3,'Автотрейд'),

Provider(11,'Next-auto'),
Provider(22,'Гарант-Авто'),
Provider(33,'Forum-Auto'),
]

#детали (id детали, название детали, цена, id поставщика)
details=[Detail(1,'сцепление',4000,1),
Detail(2,'маховик',2000,3),
Detail(3,'поршень',15000,3),
Detail(4,'колодка',1500,2),
Detail(5,'подвеска',14000,1),
]

#детали поставщика (id поставщика,id детали)
details_providers=[DetailProvider(1,1),
DetailProvider(2,2),
DetailProvider(3,3),
DetailProvider(4,4),
DetailProvider(5,5),

DetailProvider(22,1),
DetailProvider(11,2),
DetailProvider(33,3),
DetailProvider(33,4),
DetailProvider(11,5),
]

def main():
    one_to_many=[(d.name1,d.price,p.name)
        for p in providers
        for d in details
        if d.provider_id == p.id
    ]

    many_to_many_temp=[(p.name, dp.provider_id,dp.detail_id)
        for p in providers
        for dp in details_providers
        if p.id==dp.provider_id
    ]

    many_to_many=[(d.name1,d.price,provider_name)
        for provider_name, provider_id, detail_id in many_to_many_temp
        for d in details if d.id == detail_id
    ]

    print('Задание Г1')
    res_11 = [(p.name,list(name1 for name1,_,name in one_to_many if name == p.name)) for p in providers if p.name[0] == 'А']
    print(res_11)  

    print('\nЗадание Г2')
    res_12_unsorted = []
    # Перебираем все дисплейные классы
    for p in providers:
        # Список компьютеров дисплейного класса
        p_details = list(filter(lambda x: x[2] == p.name, one_to_many))
        # Если дисплейный класс не пустой
        if len(p_details) > 0:
            res_12_unsorted.append((p.name, max(p_details, key=lambda x: x[1])[1]))
 
    # Сортировка по максимальной стоимости
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('Задание Г3')
    res_13 = []
    # Перебираем все дисплейные классы
    for detail,_,provider in many_to_many:
        res_13.append((detail, provider))
    res_13 = sorted(res_13, key=itemgetter(1))
    print(res_13)

if __name__ == '__main__':
    main()