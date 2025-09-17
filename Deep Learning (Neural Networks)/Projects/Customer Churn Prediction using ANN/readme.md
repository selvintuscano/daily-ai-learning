# Customer Churn Prediction using ANN

A neural network model to predict bank customer churn using TensorFlow/Keras with comparison of sigmoid vs ReLU activation functions.

## Dataset
- 10,000 bank customer records
- 20% churn rate (2,037 customers)
- Features: Credit Score, Geography, Gender, Age, Tenure, Balance, etc.

## Model Architecture
Input (11 features) → Hidden (11 neurons) → Hidden (11 neurons) → Output (1 neuron)

## Results

| Model | Test Accuracy |
|-------|---------------|
| Sigmoid | 86.3% |
| ReLU | 85.95% |

Both activation functions performed similarly, with sigmoid showing marginally better results.
Retry

## Usage
```bash
pip install numpy pandas tensorflow scikit-learn matplotlib
python churn_prediction.py
```
