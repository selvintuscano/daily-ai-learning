# Potato Disease Classification using CNN

A deep learning project that classifies potato leaf diseases using Convolutional Neural Networks (CNN). This model can identify three different classes: **Early Blight**, **Late Blight**, and **Healthy** potato leaves.

## 🌱 Project Overview

Plant diseases are a major threat to food security, and early detection is crucial for effective treatment. This project uses computer vision and deep learning to automatically classify potato leaf diseases, helping farmers identify problems early and take appropriate action.

## 📊 Dataset

The model is trained on the **Plant Village Dataset** containing potato leaf images:
- **Source**: [Plant Village Dataset on Kaggle](https://www.kaggle.com/datasets/arjuntejaswi/plant-village)
- **Total Images**: 2,152 images
- **Classes**: 3 classes
  - `Potato___Early_blight`
  - `Potato___Late_blight` 
  - `Potato___healthy`
- **Image Size**: 256×256 pixels
- **Format**: RGB images

### Dataset Split
- **Training**: 80% (1,722 images)
- **Validation**: 10% (215 images)
- **Testing**: 10% (215 images)

## 🏗️ Model Architecture

The CNN model consists of:
- **Input Layer**: 256×256×3 (RGB images)
- **Preprocessing**: Resizing and normalization (pixel values scaled to 0-1)
- **Data Augmentation**: Random flips and rotations for better generalization
- **Convolutional Layers**: 6 Conv2D layers with ReLU activation
- **Pooling Layers**: MaxPooling2D for downsampling
- **Dense Layers**: 
  - 64 neurons with ReLU activation
  - 3 neurons with Softmax activation (output layer)
- **Total Parameters**: 183,747

### Model Summary
Total params: 183,747 (717.76 KB)
Trainable params: 183,747 (717.76 KB)
Non-trainable params: 0 (0.00 B)

## 📈 Performance

- **Training Accuracy**: 98.57%
- **Validation Accuracy**: 89.06%
- **Test Accuracy**: 90.63%
- **Training Loss**: 0.0316
- **Validation Loss**: 0.3601

## 🚀 Features

- **Real-time Prediction**: Fast inference on new potato leaf images
- **High Accuracy**: Achieves over 90% accuracy on test data
- **Data Augmentation**: Robust to variations in image orientation and lighting
- **Model Persistence**: Saved in both Keras (.keras) and HDF5 (.h5) formats

## 🛠️ Technologies Used

- **Deep Learning**: TensorFlow/Keras
- **Image Processing**: PIL (Python Imaging Library)
- **Data Visualization**: Matplotlib
- **Data Handling**: NumPy
- **Development**: Python 3.x

## 🎯 Model Training Details

### Hyperparameters
- **Batch Size**: 32
- **Image Size**: 256×256
- **Epochs**: 20
- **Optimizer**: Adam
- **Loss Function**: Sparse Categorical Crossentropy
- **Learning Rate**: Default (0.001)

### Data Preprocessing
1. **Resizing**: All images resized to 256×256 pixels
2. **Normalization**: Pixel values scaled from [0, 255] to [0, 1]
3. **Data Augmentation**: 
   - Random horizontal and vertical flips
   - Random rotation (±20%)

### Training Process
- **Dataset Caching**: Improves training speed
- **Shuffling**: Randomizes data order each epoch
- **Prefetching**: Optimizes data pipeline performance

## 📊 Results & Evaluation

The model shows excellent performance with:
- High training accuracy (98.57%)
- Good generalization (90.63% test accuracy)
- Effective disease classification across all three classes

## 📚 References

1. Hughes, D., & Salathé, M. (2015). An open access repository of images on plant health to enable the development of mobile disease diagnostics.
2. Plant Village Dataset: https://www.kaggle.com/datasets/arjuntejaswi/plant-village
3. TensorFlow Documentation: https://www.tensorflow.org/
