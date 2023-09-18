from prediction_Validation_Insertion import pred_validation
from predictFromModel import prediction


def predict_Batch_Files(path_name):
    path = path_name
    pred_val = pred_validation(path)  
    pred_val.prediction_validation()
    pred = prediction(path)
    path = pred.predictionFromModel()
    return path