# scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

import typeparser
import prodPageData
import ofArray
import predictor
import numpy as np

def parse(carmake, carmodel):
    database = []
    pagecounter = []
    years = []
    prices = []
    engines = []
    mileages = []
    transmissions = []
    steeringWheels = []
    driveUnits = []
    licenses = []
    url = 'https://kolesa.kz/cars/' + carmake + '/' + carmodel + '/?page='
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find("div", {"class": "pager"}).find('ul').find_all('li')
    for page in pages:
        pagecounter.append((typeparser.parseToInt(page.text)))

    for x in range(0, ofArray.return_largest_element(pagecounter)):
            url = 'https://kolesa.kz/cars/'+ carmake +'/'+ carmodel + '/?page=' + str(x)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            dataIDs = soup.find_all("div", {"class": "row vw-item list-item a-elem"})


            for dataID in dataIDs:
                years.append(prodPageData.prodPageDataParser(dataID).year)
                engines.append(prodPageData.prodPageDataParser(dataID).engine)
                mileages.append(prodPageData.prodPageDataParser(dataID).mileage)
                transmissions.append(prodPageData.prodPageDataParser(dataID).transmission)
                steeringWheels.append(prodPageData.prodPageDataParser(dataID).steeringWheel)
                driveUnits.append(prodPageData.prodPageDataParser(dataID).driveUnit)
                licenses.append(prodPageData.prodPageDataParser(dataID).license)
                prices.append(prodPageData.prodPageDataParser(dataID).price)


            data = {
                "year": years,
                "engine": engines,
                "mileage": mileages,
                "transmission": transmissions,
                "steeringWheel": steeringWheels,
                "driveUnit": driveUnits,
                "license": licenses,
                "price": prices,
            }

            df = pd.DataFrame(data)
            df.to_excel('./database'+carmake+carmodel+'.xlsx', index=False)





