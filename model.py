from keras.models import load_model
import numpy as np
import cv2

model = load_model('./plant.h5')

def run_model(file):
    input = cv2.imread(file)
    input = cv2.resize(input, (150, 150))
    input = cv2.cvtColor(input, cv2.COLOR_BGR2RGB)
    
    result = model.predict(np.array([input]))
    prediction = np.argmax(result, axis=1)
    
    print(result, prediction)
    return {
        "result": result.tolist(),
        "prediction": prediction.tolist()
    }

