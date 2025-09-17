# Neural Networks & Deep Learning Notes
*Learning Order: Foundation → Implementation*

## 1. Introduction: What is Deep Learning?

### Relationship to AI and ML
```
AI (Artificial Intelligence)
├── ML (Machine Learning)
│   ├── Statistical tool to analyze data
│   └── Prediction, forecasting
└── DL (Deep Learning) 🧠
    └── Mimic Human Brain
```

### Why is Deep Learning Popular Now?
1. **Huge Data** availability
2. **Hardware Advancement** - NVIDIA GPU (Graphical Processing Unit)

---

## 2. Basic Building Block: Perceptron

### Single Layered Neural Network
A perceptron is the simplest form of neural network:

```
Input Features         Hidden Layer    Output
Study (x₁) ──○──┐
                ├─○─→ Output Neuron
Play (x₂) ───○──┤
                │
Sleep (x₃) ──○──┘
```

**Example Dataset:**
| Study | Play | Sleep | Pass/Fail |
|-------|------|-------|-----------|
| 7     | 3    | 7     | 1         |
| 2     | 5    | 8     | 0         |
| 4     | 3    | 7     | 1         |

**Key Point**: Each row (Study, Play, Sleep) gets processed one by one to predict Pass/Fail.

---

## 3. Forward Propagation - How Data Flows

### Step 1: Linear Combination
Calculate the weighted sum of inputs:

```
Z = x₁w₁ + x₂w₂ + x₃w₃ + b
```

Where:
- `x₁, x₂, x₃` = input features (Study, Play, Sleep hours)
- `w₁, w₂, w₃` = weights (learned parameters)
- `b` = bias term
- `Z` = weighted sum

**Note**: We add bias when weights are zero, then we apply bias

### Step 2: Apply Activation Function
```
y = Z × i w^i
```
Then pass through activation function to get final output.

### Network Flow Diagram:
```
x₁ ──○── w₁ ──┐
              ├─○─ Act(Z×w+b) ──→ O/P
x₂ ──○── w₂ ──┤                    │
              │                    ↓
x₃ ──○── w₃ ──┘                   ŷ
```

---

## 4. Activation Functions - The Decision Makers

### What is an Activation Function?
An **Activation Function** is a function that decides whether a neuron should be activated or not.

### Real-world Analogy
- If you place a hot object on your hand, you will move your hand away as the neurons there are getting activated
- **Weights help your neurons to act** (determine what level they should be activated)

### Example: Sigmoid Activation Function
Used for **Binary Classification** problems:

#### Sigmoid Formula:
```
Sigmoid = 1/(1 + e^(-z))
```

With bias included:
```
Sigmoid = 1/(1 + e^(-(Z×w + b)))
```

**Output Range**: (0 to 1) - Perfect for binary classification!

**Example**: If predicted value is 0, then ŷ = 1

---

## 5. Loss Function - Measuring Errors

### What is Loss?
The difference between actual and predicted values:

```
Loss = (y - ŷ)
```

Where:
- `y` = actual value (ground truth)
- `ŷ` = predicted value

### Goal
**Aim**: Minimize the difference (y - ŷ) to be as close to **0** as possible.

**Question**: Now you know the difference is huge. What do you do?
**Answer**: Use Backpropagation!

---

## 6. Backpropagation - Learning from Mistakes ⭐

### Purpose
**Aim of backpropagation**: To update weights so the model learns from its mistakes.

### How it Works
```
Input ──→ Forward Pass ──→ Calculate Loss ──→ Backward Pass ──→ Update Weights
   ↑                                                                    │
   └────────────────── Repeat Process ←─────────────────────────────────┘
```

### The Learning Process
1. Calculate how wrong the prediction was (Loss)
2. Figure out which weights contributed most to the error
3. Update those weights to reduce future errors
4. Repeat until the model gets better

### Optimizers
**The optimizer ensures each weight gets updated** while we are doing backpropagation.

**Example optimizer**: Gradient Descent

---

## 7. Putting It All Together: Complete Neural Network

### Multi-layer Network Architecture
```
Input Layer    Hidden Layers    Output Layer

x₁ ──○─────────○─────────○
              ╱ ╲       ╱
x₂ ──○────────○───○─────○ ──→ Final Prediction
             ╱     ╲   ╱
x₃ ──○──────○───────○─○
```

### The Complete Process
1. **Input**: Feed data (Study, Play, Sleep hours)
2. **Forward Propagation**: Calculate Z, apply activation
3. **Loss Calculation**: Compare prediction with actual result
4. **Backpropagation**: Update weights to reduce error
5. **Repeat**: Continue until model is accurate

### Weight Assignment During Training
While training, we assign weights based on what level a neuron should be activated.

---

## 8. Key Formulas Summary

### Linear Combination
```
Z = Σ(xᵢ × wᵢ) + b
```

### Sigmoid Activation
```
σ(z) = 1/(1 + e^(-z))
```

### Loss Function
```
Loss = (y - ŷ)²
```

---

## 9. Learning Path Summary

**Foundation Built**:
✅ Understanding AI → ML → DL hierarchy  
✅ Basic perceptron structure  
✅ Forward propagation mathematics  
✅ Activation functions (Sigmoid)  
✅ Loss function concept  
✅ Backpropagation for learning  

**Next Steps to Explore**:
- Different activation functions (ReLU, Tanh)
- Multiple hidden layers (Deep Networks)
- Different optimizers (Adam, SGD)
- Various loss functions for different problems
- Regularization techniques
- Different network architectures (CNN, RNN)

---

## 10. Important Insights from Your Notes

🧠 **Key Realizations**:
- Neural networks mimic how our brain processes information
- Weights determine how much each input matters
- Activation functions decide if a neuron "fires"
- Learning happens by adjusting weights based on mistakes
- The process is iterative - the network gets better over time

**Real-world Connection**: Just like touching something hot makes you pull away (neuron activation), neural networks learn to "react" appropriately to different inputs through training!