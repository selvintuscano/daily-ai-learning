# California Housing Price Prediction with Neural Networks

A deep learning project that predicts median housing prices in California using an Artificial Neural Network (ANN) built with TensorFlow/Keras.

## 📊 Project Overview

This project implements a regression model to predict housing prices based on various features like location, housing characteristics, and demographic data. The model achieves an **R² score of 0.693**, indicating it can explain approximately 69% of the variance in housing prices.

## 🎯 Key Results

- **R² Score**: 0.693
- **Model Architecture**: Deep Neural Network with 636,001 parameters
- **Training Time**: 10 epochs with early stopping

## 📈 Dataset

The California Housing dataset contains **20,433 samples** with the following features:

| Feature | Description |
|---------|-------------|
| `longitude` | Longitude coordinate |
| `latitude` | Latitude coordinate |
| `housing_median_age` | Median age of houses in the block |
| `total_rooms` | Total number of rooms in the block |
| `total_bedrooms` | Total number of bedrooms in the block |
| `population` | Population in the block |
| `households` | Number of households in the block |
| `median_income` | Median income of residents (in tens of thousands) |
| `ocean_proximity` | Proximity to ocean (categorical, label-encoded) |

**Target Variable**: `median_house_value` - Median house value in USD

## 🏗️ Model Architecture

Input Layer:    Dense(1000) + ReLU + Dropout(0.2)
Hidden Layer 1: Dense(500) + ReLU + Dropout(0.2)  
Hidden Layer 2: Dense(250) + ReLU
Output Layer:   Dense(1) + Linear activation

**Total Parameters**: 636,001 (all trainable)

## 🔍 Key Insights from EDA

1. **Strongest Predictor**: `median_income` has the highest correlation (0.69) with house prices
2. **Geographic Patterns**: Clear price clustering around San Francisco Bay Area and coastal regions
3. **Multicollinearity**: High correlation between room-related features (>0.9)
4. **Price Capping**: Dataset shows evidence of price capping at $500,000

## 🚀 Getting Started

### Prerequisites
```bash
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow keras
```


## License
This project is licensed under the MIT License - see the LICENSE file for details.
🏷️ Tags
machine-learning deep-learning neural-networks tensorflow keras regression housing-prices california data-science python
