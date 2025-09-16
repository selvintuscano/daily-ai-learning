from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

# Load the trained model
# Load your trained model
model = load_model("house_price_model.keras")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get input features from form
            longitude = float(request.form['longitude'])
            latitude = float(request.form['latitude'])
            housing_median_age = float(request.form['housing_median_age'])
            total_rooms = float(request.form['total_rooms'])
            total_bedrooms = float(request.form['total_bedrooms'])
            population = float(request.form['population'])
            households = float(request.form['households'])
            median_income = float(request.form['median_income'])
            ocean_proximity = float(request.form['ocean_proximity'])
            
            # Prepare features for prediction
            features = np.array([
                longitude, latitude, housing_median_age, total_rooms, total_bedrooms,
                population, households, median_income, ocean_proximity
            ]).reshape(1, -1)
            
            # Make prediction
            price = model.predict(features)[0][0]
            
            return render_template('index.html', prediction=f"${price:,.2f}")
        except Exception as e:
            return render_template('index.html', prediction=f"Error: {str(e)}")
    
    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
