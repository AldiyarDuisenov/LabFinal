# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from HTMLparser import parse
from predictor import predict

def inputdata():
    mycar = []
    mycar.append(input('Введите марку авто прописными буквами на латинице. Пример ( Тойота => toyota )\n'))
    mycar.append(input('Введите модель авто, заменяя пробел на "-". Пример ( Land Cruiser => land-cruiser)\n'))
    mycar.append(input('Введите год выпускаю Пример ( 2017 )\n'))
    mycar.append(input('Введите объем двигателя. Пример ( пяти литровый двигатель => 5.0)\n'))
    mycar.append(input('Введите пробег в км. Пример ( 180000км => 180000 )\n'))
    mycar.append(input('Коробка передачь: механика / автомат / типтроник / вариатор / робот\n'))
    mycar.append(input('Руль: слева / справа\n'))
    mycar.append(input('Привод: передний привод / задний привод / полный привод\n'))
    mycar.append(input('Растоможен в Казахстане: Да / Нет\n'))
    parse(mycar[0], mycar[1])
    if (int(mycar[4]) >= 0 and int(mycar[4]) <= 100000):
        mycar[4] = 1
    if (int(mycar[4]) > 100000 and int(mycar[4]) <= 300000):
        mycar[4] = 2
    if (int(mycar[4]) > 300000):
        mycar[4] = 3
    if (mycar[5] == 'механика'):
        mycar[5] = 1
    if (mycar[5] == 'автомат'):
        mycar[5] = 2
    if (mycar[5] == 'типтроник'):
        mycar[5] = 3
    if (mycar[5] == 'вариатор'):
        mycar[5] = 4
    if (mycar[5] == 'робот'):
        mycar[5] = 5
    if (mycar[6] == 'слева'):
        mycar[6] = 1
    if (mycar[6] == 'справа'):
        mycar[6] = 2
    if (mycar[7] == 'передний привод'):
        mycar[7] = 1
    if (mycar[7] == 'задний привод'):
        mycar[7] = 2
    if (mycar[7] == 'полный привод'):
        mycar[7] = 3
    if (mycar[8] == 'Нет'):
        mycar[8] = 1
    if (mycar[8] == 'Да'):
        mycar[8] = 2

    predict(mycar[0], mycar[1], mycar[2], mycar[3], mycar[4], mycar[5], mycar[6], mycar[7], mycar[8])
inputdata()
