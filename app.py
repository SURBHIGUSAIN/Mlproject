from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)  # will give us entry point

# create a variable and assign this applocation bcoz later we will create route
app = application
# Route for a home page


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():  # we will do all the things here geting data and doing prediction
    if request.method == 'GET':
        # not index becuase index is a home page
        return render_template('home.html')
        # the home page will have simple data points that is needeed for provided to the model
    else:  # if it is not Get then it is post hence get the inputs
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get(
                'parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get(
                'test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)  # see how data looks like

        predict_pipeline = PredictPipeline()  # initialize predict pipeline

        results = predict_pipeline.predict(pred_df)  # hit predict function

        # results[0] bcoz result is in form of list
        return render_template('home.html', results=results[0])


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
