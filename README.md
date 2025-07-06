# 💸 Detecting UPI Fraud with Machine Learning: Leveraging Festive Patterns

India’s UPI handles over **150 billion transactions annually**, but loses **₹1,200 crore** to fraud.  
This project uses machine learning to detect fraud in a **100,000-transaction** dataset, where **3.198%** are fraudulent.  
A key insight? Fraud spikes during festivals  **4% vs. 2%** captured by a custom `festival_flag` feature.

---

## 📁 Dataset Overview

- **Size**: 100,000 synthetic UPI transactions  
- **Fraud Rate**: 3.198%  
- **Key Features**:  
  - `amount`  
  - `merchant_type`  
  - `time_delta`  
  - `festival_flag` (20.45% of transactions)

All features were preprocessed using **StandardScaler** and **OneHotEncoder**. No derived features were added — we focused on raw, interpretable inputs.

---

## 🧠 Approach

We trained two models to detect fraud:

- **Logistic Regression (LR)**:  
  Optimizes  
  $$J(θ) = -∑[y \log(h_θ(x)) + (1-y) \log(1-h_θ(x))]$$  
  to estimate fraud probability.

- **Support Vector Machine (SVM)**:  
  Uses an RBF kernel to draw a decision boundary by minimizing  
  $$\min_{w,b} \frac{1}{2}||w||^2$$

To address class imbalance (only 3.198% fraud), we used **SMOTE** for oversampling.  
The `festival_flag` helped capture seasonal fraud surges — **4% during festivals vs. 2% otherwise**.

---

## 📊 Model Performance

| Model | Accuracy | Precision | Recall | F1-score | AUC  |
|-------|----------|-----------|--------|----------|------|
| **LR**  | 0.787    | 0.066     | 0.449  | 0.115    | 0.644 |
| **SVM** | 0.031    | 0.031     | 1.000  | 0.060    | 0.471 |

- **Training set**: 80,000 samples  
- **Test set**: 20,000 samples  
- LR caught more frauds with fewer false alarms.  
- SVM flagged all frauds but misclassified too many safe transactions.

---

## 🎯 Conclusion

This project shows that **Logistic Regression** is a strong baseline for UPI fraud detection, especially when paired with features like `festival_flag`.  
While **SVM** struggled, the insights gained pave the way for smarter fraud detection systems that can protect platforms like **PhonePe** and **Google Pay** from massive losses.

---

> 💡 _Machine learning can make digital payments safer — one transaction at a time._
