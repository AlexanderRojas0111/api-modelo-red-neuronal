from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from app.models.project1_predict_models import predictModels
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd

router = APIRouter()

# Cargar los datos
ruta_archivo = r'PreguntasChat_1.xlsx'
datos_excel = pd.ExcelFile(ruta_archivo)
hoja_software = datos_excel.parse('PLANEACION')
le = LabelEncoder()
respuestas = hoja_software.iloc[:, 2:31].values
le.fit(respuestas.flatten())

class  DataInput (BaseModel): 
    message: str
    type: str

@router.post("/")
async def predicts(datainput: DataInput):
    try:
        
        data = [datainput.message]
        print("Data input")
        print(data)
        predictions = predictModels.predicts(data)

        prediction = []
        if (datainput.type == "software"):
            prediction = predictions["Respuesta5"]
        elif (datainput.type == "planeacion"):
            prediction = predictions["Respuesta4"]
        elif (datainput.type == "implementacion"):
            prediction = predictions["Respuesta3"]
        elif (datainput.type == "hardware"):
            prediction = predictions["Respuesta2"]
        elif (datainput.type == "capacitacion"):
            prediction = predictions["Respuesta1"]
        else:
            return JSONResponse(status_code=500, content={"message": "Falta parametro type, opciones: software, planeacion, implementacion, hardware o capacitacion ...."})    


        probabilidades = np.max(prediction, axis=-1)
        indices_predichos = np.argmax(prediction, axis=-1).flatten()
        #respuestas_posibles = le.classes_[indices_predichos4]
        respuesta_mayor_probabilidad = le.inverse_transform(indices_predichos)[np.argmax(probabilidades)]

        
        return JSONResponse(status_code=200, content={"predictions": respuesta_mayor_probabilidad})
        #return datainput
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})
    