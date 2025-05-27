import joblib
import numpy as np
from flask import Flask, render_template, request
from db import insert_reservation  # Import the function from db.py
from config.path_config import MODEL_OUTPUT_PATH

app = Flask(__name__)

loaded_model = joblib.load(MODEL_OUTPUT_PATH)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        data = {
            'lead_time': int(request.form['lead_time']),
            'no_of_special_request': int(request.form['no_of_special_request']),
            'avg_price_per_room': float(request.form['avg_price_per_room']),
            'arrival_month': int(request.form['arrival_month']),
            'arrival_date': int(request.form['arrival_date']),
            'market_segment_type': int(request.form['market_segment_type']),
            'no_of_week_nights': int(request.form['no_of_week_nights']),
            'no_of_weekend_nights': int(request.form['no_of_weekend_nights']),
            'type_of_meal_plan': int(request.form['type_of_meal_plan']),
            'room_type_reserved': int(request.form['room_type_reserved']),
        }

        features = np.array([[data['lead_time'], data['no_of_special_request'], data['avg_price_per_room'],
                              data['arrival_month'], data['arrival_date'], data['market_segment_type'],
                              data['no_of_week_nights'], data['no_of_weekend_nights'],
                              data['type_of_meal_plan'], data['room_type_reserved']]])

        prediction = loaded_model.predict(features)
        predicted_value = int(prediction[0])

        insert_reservation(data, predicted_value)

        return render_template('index.html', prediction=predicted_value)

    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9050, debug=True)
