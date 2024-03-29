import sqlite3
from datetime import datetime, timedelta
import random

conn = sqlite3.connect('Restaurant.db')
c = conn.cursor()

c.executescript(
'''
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Пельмени сибирские', 'Горячие закуски', 
    'Прозрачный бульон, хвойное масло, сметана', 1080, 1, NULL, 0);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Арахис по-лаосски', 'Холодные закуски', 
    'Арахис, обжаренный на масле с кайенским перцем и соевым соусом', 290, 1, NULL, 1);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Устрицы', 'Холодные закуски', 
    'Устрицы', 290, 1, NULL, 0);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Парфе из печени цесарки с черным трюфелем', 'Холодные закуски', 
    'Варенье из слив, мороженное со вкусом сдобы', 850, 1, NULL, 0);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Традиционный французский суп', 'Супы', 
    'Куриный бульон, тимьян, слоеное тесто', 550, 1, NULL, 0);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Фирменный сырный суп', 'Супы', 
    'Из 4 сыров', 850, 1, NULL, 1);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Запеченный сыр Бри', 'Горячие закуски', 
    'С грушей и розмарином', 1490, 1, NULL, 1);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Котлетки из судака', 'Основные блюда', 
    'Печёный в углях картофель, разносолы, соус тар-тар', 1250, 1, NULL, 0);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Пирог с дичью и фуагра', 'Основные блюда', 
    'Соус с трюфелем, картофельное пюре, мочёные райские яблочки', 1500, 1, NULL, 0);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Оливье от "Люсьена"', 'Холодные закуски', 
    'Ростбиф, утка и цыпленок', 720, 1, NULL, 0);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Деревенский салат', 'Холодные закуски', 
    'Со свежими огурцами, куриным яйцом, редисом, зеленым луком и укропом. Заправляется сметана & майонез', 420, 1, NULL, 1);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Жюльен из белых грибов', 'Горячие закуски', 
    'Запеченный в тончайших блинчиках', 460, 1, NULL, 1);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Царская уха', 'Супы', 
    'Из трех видов рыб, с рыбными варениками', 790, 1, NULL, 0);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Мидии в сливочном соусе', 'Основные блюда', 
    'Сковородка тихоокеанских мидий в створках с луком-порей и соусом из слоивок и сыра', 580, 1, NULL, 0);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Феттуччине с грибами', 'Основные блюда', 
    'Паста, шампиньоны, петрушка, лук, томаты черри, сливки и пармезан', 490, 1, NULL, 1);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Пенне с овощами и соусом аррабиата', 'Основные блюда', 
    'Кабачок, перец болгарский, баклажаны, брокколи, оливки, маслины', 420, 1, NULL, 1);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Старорусский пудинг', 'Десерты', 
    'Из яичных желтков под хрустящей карамелью', 410, 1, NULL, 1);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Песочный тарт', 'Десерты', 
    'С желе из гуавы и нежным кремом из карамельного шоколада', 320, 1, NULL, 1);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Горячий шоколадный торт', 'Десерты', 
    'С ванильным мороженым', 390, 1, NULL, 1);
INSERT INTO Блюда (Название, Тип, Ингредиенты, Цена, Наличие, Скидка, Вегетарианское) VALUES('Наполеон', 'Десерты', 
    'С клубникой "фламбе" и карамельным куполом', 670, 1, NULL, 1);
'''
)
conn.commit()

a = ['VIP', 'У окна', 'В зале']
b = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 6, 6, 8, 10]
for i in range(1, 21):
    r = random.choice(b)
    r1 = random.choice(a)
    if r1 == 'VIP':
        r2 = random.randint(500, 999)
    elif r1 == 'У окна':
        r2 = random.randint(100, 499)
    else:
        r2 = random.randint(20, 99)
    c.execute("INSERT INTO Столики (Тип, Места, Цена) VALUES ('%s','%s', '%s')" % (r1, r, r2*10))
conn.commit()

date1 = datetime.now()
for i in range(1, 31):
    c.execute("SELECT Столик FROM Столики;")
    row = c.fetchall()
    table = random.choice(row)
    t = random.randint(5, 600)
    c.execute("INSERT INTO Заказы (Столик, Дата) VALUES ('%s','%s')" % (table[0], date1 - timedelta(minutes=t)))
conn.commit()

for i in range(1, 21):
    c.execute("SELECT Заказ FROM Заказы;")
    row = c.fetchall()
    ord = random.choice(row)
    iter = random.randint(1, 5)
    for j in range (1, iter + 1):
        c.execute("SELECT Блюдо FROM Блюда;")
        row = c.fetchall()
        dish = random.choice(row)
        c.execute("INSERT INTO Заказы_Блюда (Заказ, Блюдо) VALUES ('%s','%s')" % (ord[0], dish[0]))
conn.commit()

date1 = datetime.date(datetime.now())
for i in range(1, 31):
    c.execute("SELECT Столик FROM Столики;")
    row = c.fetchall()
    table = random.choice(row)
    t = random.randint(1, 30)
    try:
        c.execute("INSERT INTO Бронирования (Столик, Дата) VALUES ('%s','%s')" % (table[0], date1 + timedelta(days=t)))
    except:
        pass
conn.commit()

date = datetime.now() - timedelta(days=50)
sum = 0
for i in range(1, 51):
    date = date + timedelta(days=1)
    r = random.randint(1000, 10000)
    r1 = random.randint(-4000, -500)
    sum = sum + r*10
    c.execute("INSERT INTO Доходы (Дата, Доход, Состояние_счета) VALUES ('%s','%s', '%s')" % (date, r*10, sum))
    sum = sum + r1*10
    c.execute("INSERT INTO Доходы (Дата, Доход, Состояние_счета) VALUES ('%s','%s', '%s')" % (date + timedelta(hours=1), r1 * 10, sum))
conn.commit()
c.close()
conn.close()