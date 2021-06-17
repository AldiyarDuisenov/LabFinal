
from sklearn import tree
import pandas as pd
def predict(inputbrand,inputmodel,inputyear, inputengine, inputmilage, inputtransmission, inputsteeringWheel, inputdriveUnit, inputlicense):
    df = pd.read_excel('database'+inputbrand+inputmodel+'.xlsx')

    inputs = df.drop('price', axis='columns')
    target = df['price']

    inputs['transmission'].replace({"механика": 1, "автомат": 2, "типтроник": 3, "вариатор": 4, "робот": 5}, inplace=True)
    inputs['steeringWheel'].replace({"слева": 1, "справа": 2}, inplace=True)
    inputs['driveUnit'].replace({"передний привод": 1, "задний привод": 2, "полный привод": 3}, inplace=True)
    inputs['mileage'].replace({"0 - 100000": 1, "100000 - 300000": 2, "+300000": 3}, inplace=True)
    inputs['license'].replace({"Да": 1, "Нет": 2}, inplace=True)

    print(inputs)
    model = tree.DecisionTreeClassifier()
    model.fit(inputs, target)
    print('Приблезительная стоймость вашего авто:')
    print(model.predict([[inputyear, inputengine, inputmilage, inputtransmission, inputsteeringWheel, inputdriveUnit, inputlicense]]))






