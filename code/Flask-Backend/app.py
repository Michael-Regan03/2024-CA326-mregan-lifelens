from flask import Flask, request
from flask_restful import Resource, Api 
from flask_cors import CORS
import pickle
import numpy as np
import json
import ast

app = Flask(__name__)

CORS(app)

api = Api(app)

def risk_calc(risks):
    if risks < 0.3:
        return "low-risk"
    elif risks > 0.7:
        return "mid risk"
    else:
        return "high risk"

class riskAssesment(Resource):
    def post(self):
        
        #Recieve JSON data
        json_data = request.get_json(force=True)
        
        #Extract behaviours
        behaviours = json_data.get('behaviours')

        #Transfer string to list
        behaviours = ast.literal_eval(behaviours)

        #Format list
        data = np.array([behaviours])
        #load model
        model = pickle.load(open('RFCmodel.pkl', 'rb'))

        #get prediction probabilities
        predictions = model.predict_proba(data)

        #extreact likeylhod of fittig in the class 
        risks = [p[0][1] for p in predictions]


        #Turn percentage it low/mid/hgh risk strigs
        for i in range(len(risks)):
            risks[i] = risk_calc(risks[i])

        payload ={
            'Diabetes': risks[0],
            'Pre_Diabetes': risks[1] ,
            'Depression': risks[2],    
            'COPD': risks[3], 
            'Kidney_disease' : risks[4],
            'Angina_Coronary_heart_disease' : risks[5],
            'Myocardial_infarction' : risks[6],
            'Stroke' : risks[7],
            'Arthritis,Gout,Lupus,Fibromyalgia' : risks[8],
            'Skin_cancer' : risks[9] }


        payload = json.dumps(payload)
        return payload, 200



api.add_resource(riskAssesment, '/riskassessment')



if __name__ == '__main__':
    app.run(debug=True)

