from smartphone import Smartphone

catalog = [
    Smartphone('Samsung', 'Galaxy A34', '+79978999949'),
    Smartphone('Apple', 'Iphone 14', '+79278292929'),
    Smartphone('Xiaomi', 'Mi 11', '+79276555555'),
    Smartphone('Redmi', 'note 15', '+79378123456'),
    Smartphone('Huawei', 'P40', '+79992567890')
]

for smartphone_item in catalog:
    print(f'{smartphone_item.brand} - {smartphone_item.model} .'
          f' {smartphone_item.number}')
