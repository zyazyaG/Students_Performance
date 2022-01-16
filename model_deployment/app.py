from flask import Flask, render_template, request
import pandas as pd
import joblib


app = Flask(__name__)


@app.route("/")

def index():
    return render_template('/index.html')
    

@app.route('/predict', methods=['GET','POST'])

def predict():
    
    if request.method == "POST":
        #get form data
        to_predict_list = request.form.to_dict()
        
        #call preprocessDataAndPredict and pass inputs
        try:
            prediction = preprocessDataAndPredict(to_predict_list)
            #pass prediction to template
            return render_template('/predict.html', prediction = prediction)
   
        except ValueError:
            return "Please Enter valid values"
  
        pass
    pass


def preprocessDataAndPredict(feature_dict):
    
    test_data = {k:[v] for k,v in feature_dict.items()}  
    test_data = pd.DataFrame(test_data)

    file = open("lr_model.pkl","rb")
    
     #load trained model
    trained_model = joblib.load(file)
    
    predict = trained_model.predict(test_data)

    return predict
    
    pass
if __name__ == '__main__':
    app.run(debug=True)