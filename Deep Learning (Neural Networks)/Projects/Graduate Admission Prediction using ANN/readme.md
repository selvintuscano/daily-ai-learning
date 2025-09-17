# Graduate Admission Prediction using ANN

A neural network regression model to predict graduate school admission chances using student academic and profile data.

## About Dataset

This dataset includes various information like GRE score, TOEFL score, university rating, SOP (Statement of Purpose), LOR (Letter of Recommendation), CGPA, research and chance of admit. The dataset contains 400 entries with the following features:

- **GRE Scores** (out of 340)
- **TOEFL Scores** (out of 120) 
- **University Rating** (out of 5)
- **Statement of Purpose (SOP)** strength (out of 5)
- **Letter of Recommendation (LOR)** strength (out of 5)
- **Undergraduate GPA/CGPA** (out of 10)
- **Research Experience** (binary: 0 or 1)
- **Chance of Admit** (target variable, ranging from 0 to 1)

## Model Architecture
Input (7 features) → Hidden (7 neurons, ReLU) → Hidden (7 neurons, ReLU) → Output (1 neuron, Linear)

## Results
- **R² Score**: 0.42
- **Final Training Loss**: 0.0174
- **Final Validation Loss**: 0.0165
- **Epochs**: 25

## Features
- Regression model for continuous target prediction
- MinMaxScaler normalization for feature scaling
- Correlation analysis and data visualization
- Mean Squared Error loss function

## Usage
```bash
pip install numpy pandas tensorflow scikit-learn matplotlib seaborn
python admission_prediction.py
```

The model effectively captures relationships between academic metrics and admission probability, with CGPA and test scores being strong predictors.
