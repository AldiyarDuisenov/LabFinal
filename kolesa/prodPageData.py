import requests
from bs4 import BeautifulSoup

import typeparser

def prodPageDataParser(dataID):
    engine = None
    mileage = 0
    transmission = None
    steeringWheel = None
    driveUnit = None
    license = None
    Url = 'https://kolesa.kz/a/show/' + str(dataID.attrs['data-id'])
    response = requests.get(Url)
    soup = BeautifulSoup(response.text, 'lxml')
    year = typeparser.parseToInt(soup.find("h1", {"class": "offer__title"}).find("span", {"class": "year"}).text)
    stats = soup.find("div", {"class": "offer__parameters"}).find_all("dl", {"class": ""})
    for engines in stats:
        if(engines.find("dt", {"title": "Объем двигателя, л"})):
            engine = typeparser.parseToFloat(str(engines.find("dd", {"class": "value"}).text))
    for mileages in stats:
        if(mileages.find("dt", {"title": "Пробег"})):
            tempmil = typeparser.parseToInt(str(mileages.find("dd", {"class": "value"}).text))
            if(tempmil >= 0 and tempmil <= 100000):
                mileage = '0 - 100000'
            if (tempmil > 100000 and tempmil <= 300000):
                mileage = '100000 - 300000'
            if (tempmil > 300000):
                mileage = '+300000'
    for transmissions in stats:
        if(transmissions.find("dt", {"title": "Коробка передач"})):
            transmission = transmissions.find("dd", {"class": "value"}).text
    for steeringWheels in stats:
        if(steeringWheels.find("dt", {"title": "Руль"})):
            steeringWheel = steeringWheels.find("dd", {"class": "value"}).text
    for driveUnits in stats:
        if(driveUnits.find("dt", {"title": "Привод"})):
            driveUnit = driveUnits.find("dd", {"class": "value"}).text
    for licenses in stats:
        if(licenses.find("dt", {"title": "Растаможен в Казахстане"})):
            license = licenses.find("dd", {"class": "value"}).text
    price = typeparser.parseToInt(soup.find("div", {"class": "offer__price"}).text)

    class data:
        def __init__(self, year, engine, mileage, transmission, steeringWheel, driveUnit, license, price):
            self.year = year
            self.engine = engine
            self.mileage = mileage
            self.transmission = transmission
            self.steeringWheel = steeringWheel
            self.driveUnit = driveUnit
            self.license = license
            self.price = price
    carData = data(year, engine, mileage, transmission, steeringWheel, driveUnit, license, price)
    database = {
        "year": year,
        "engine": engine,
        "mileage": mileage,
        "transmission": transmission,
        "steeringWheel": steeringWheel,
        "driveUnit": driveUnit,
        "license": license,
        "price": price
    }

    return carData

