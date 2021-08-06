import json
import pickle


import numpy as np

area_type = None
data_columns= None
model = None





def load_saved_artifacts():

    print("Loading Artifacts")
    global data_columns
    global area_type

    with open("./artifacts/columns.json", "r") as data:
        data_columns = json.load(data)['data_columns']
        area_type = data_columns[3:]
        print(area_type)

    global model
    if model is None:
        with open("./artifacts/banglore_house_price.pickle", 'rb') as data:
            model = pickle.load(data)

def get_estimated_price(area_type, sqft, bhk, bath):
    try:
        loc_index = data_columns.index(area_type.lower())

    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = bath
    x[1] = bhk
    x[2] = sqft
    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0], 2)

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_estimated_price('carpet  area', 1000, 3, 3))
    print(get_estimated_price('plot  area', 2000, 2, 2))
    print(get_estimated_price('plot  area', 1000, 2, 2))
    print(get_estimated_price('plot  area', 1000, 2, 2))
