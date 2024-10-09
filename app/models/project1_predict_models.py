from app.core.config import settings
from app.utils.get_model import get_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


class Project1PredictModels:
    def __init__(self):
        self.model1 = get_model(settings.PROJECT1_MODEL1_PATH)
        self.model2 = get_model(settings.PROJECT1_MODEL2_PATH)
        self.model3 = get_model(settings.PROJECT1_MODEL3_PATH)
        self.model4 = get_model(settings.PROJECT1_MODEL4_PATH)
        self.model5 = get_model(settings.PROJECT1_MODEL5_PATH)
    

    def predicts(self, input_data):
        tokenizador = Tokenizer()
        tokenizador.fit_on_texts(input_data)
        longitud_maxima = 50
        secuencias_preguntas = tokenizador.texts_to_sequences(input_data)
        preguntas_rellenadas = pad_sequences(secuencias_preguntas, maxlen=longitud_maxima)
        print("preguntas rellenadas")
        print(preguntas_rellenadas)

        prediction1 = self.model1.predict(preguntas_rellenadas)
        prediction2 = self.model2.predict(preguntas_rellenadas)
        prediction3 = self.model3.predict(preguntas_rellenadas)
        prediction4 = self.model4.predict(preguntas_rellenadas)
        prediction5 = self.model5.predict(preguntas_rellenadas)
        
        return {
            "Respuesta1": prediction1, 
            "Respuesta2": prediction2, 
            "Respuesta3": prediction3, 
            "Respuesta4": prediction4, 
            "Respuesta5": prediction5
        }
        

predictModels = Project1PredictModels()