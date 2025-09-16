# Breast Cancer Classification with Neural Networks

A machine learning project that classifies breast cancer tumors as malignant or benign using an Artificial Neural Network built with TensorFlow/Keras on the Wisconsin Breast Cancer dataset.

## 📊 Project Overview

This project implements a binary classification model to predict whether breast cancer tumors are malignant (cancerous) or benign (non-cancerous) based on cell nucleus features extracted from digitized images of fine needle aspirate (FNA) samples. The model achieves **95.6% accuracy** on the test dataset.

## 🎯 Key Results

- **Test Accuracy**: 95.6%
- **Dataset**: Wisconsin Breast Cancer dataset (569 samples)
- **Model Architecture**: Simple Neural Network with 30 input features
- **Training Epochs**: 10 epochs with validation split

## 📈 Dataset Information

The Wisconsin Breast Cancer dataset contains **569 samples** with **30 features** computed from digitized images of cell nuclei:

### Feature Categories
1. **Mean values** (10 features): radius, texture, perimeter, area, smoothness, compactness, concavity, concave points, symmetry, fractal dimension
2. **Standard error** (10 features): SE of the above measurements
3. **Worst values** (10 features): Mean of the three worst/largest values for each feature

### Target Classes
- **0**: Malignant (212 samples)
- **1**: Benign (357 samples)

### Dataset Statistics
| Class | Count | Percentage |
|-------|-------|------------|
| Benign (1) | 357 | 62.7% |
| Malignant (0) | 212 | 37.3% |

## 🏗️ Model Architecture

- Input Layer:  Flatten(30 features) 
- Hidden Layer:  Dense(20) + ReLU activation
- Output Layer:  Dense(2) + Sigmoid activation

**Model Configuration:**
- **Optimizer**: Adam
- **Loss Function**: Sparse Categorical Crossentropy
- **Metrics**: Accuracy
- **Total Parameters**: Approximately 642 trainable parameters

## 🔍 Key Insights

1. **Class Imbalance**: Dataset has more benign cases (62.7%) than malignant (37.3%)
2. **Feature Scaling**: StandardScaler normalization significantly improves model performance
3. **Quick Convergence**: Model reaches high accuracy within just 10 epochs
4. **No Missing Values**: Clean dataset with no preprocessing required for missing data

## 🚀 Getting Started

### Prerequisites
```bash
pip install numpy pandas matplotlib scikit-learn tensorflow
```

## 🔧 Model Performance

#### Training History

Final Training Accuracy: 95.8%
Final Validation Accuracy: 97.8%
Training Loss: 0.130
Validation Loss: 0.116

#### Test Results

Test Accuracy: 95.6%
Model generalizes well with minimal overfitting

### 📊 Training Visualization
The model shows excellent convergence:

Accuracy increases rapidly from 63% to 95% in the first few epochs
Validation accuracy reaches 97.8%, indicating good generalization
Loss decreases steadily without signs of overfitting

