from app.core.config import settings
from app.utils.get_model import get_model

class PredictModel:
    def __init__(self):
        self.model = get_model(settings.MODEL_PATH)

    def predict(self, input_data):
        return self.model.predict(input_data).flatten().tolist()
    
predictModel = PredictModel()