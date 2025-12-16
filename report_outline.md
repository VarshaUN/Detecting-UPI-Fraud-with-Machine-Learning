# CS229 Project Report: UPI Fraud Detection
## Results
- Logistic regression with SMOTE (10,000 transactions, 20.66% fraud):
  - F1-score: 0.877
  - Precision: 0.797
  - Recall: 0.974
  - AUC: 0.990
- Features: amount, merchant_type, festival_flag
- Dataset stats: 10,000 transactions, fraud ratio 20.66%, festival_flag in 20.45%
- ROC curve: figures/roc_curve.png
- Note: High fraud ratio inflates metrics; testing 2-5% fraud next.

# CS229 Project Report: UPI Fraud Detection
## Results
- Logistic regression with SMOTE (10,000 transactions, 20.66% fraud):
  - F1-score: 0.877
  - Precision: 0.797
  - Recall: 0.974
  - AUC: 0.990
- Features: amount, merchant_type, festival_flag
- Dataset stats: 10,000 transactions, fraud ratio 20.66%, festival_flag in 20.45%
- Festival_flag analysis: Fraud rate 19.96% (non-festival) vs. 23.37% (festival), ~17% higher during festivals
- ROC curve: figures/roc_curve.png
- Note: High fraud ratio inflates metrics; testing 2-5% fraud next.

# CS229 Project Report: UPI Fraud Detection
## Dataset
- Size: 10,000 transactions
- Fraud ratio: 20.66%
- Festival_flag ratio: 20.45% (2045 festival transactions)
- Merchant types: grocery, travel, e-commerce, temple
- Missing values: None
## Results
- Logistic regression with SMOTE (10,000 transactions):
  - F1-score: 0.877
  - Precision: 0.797
  - Recall: 0.974
  - AUC: 0.990
- Features: amount, merchant_type, festival_flag
- Festival_flag analysis: Fraud rate 19.96% (non-festival) vs. 23.37% (festival), ~17% higher during festivals
- ROC curve: figures/roc_curve.png
- Note: High fraud ratio inflates metrics; testing 2-5% fraud next.

# CS229 Project Report: UPI Fraud Detection
## Dataset
- 10,000 transactions: 20.66% fraud, 20.45% festival_flag
- 100,000 transactions: ~2-5% fraud ([Your Fraud Ratio]), ~20.45% festival_flag ([Your Festival_flag Ratio])
- Merchant types: grocery, temple, e-commerce, travel
- Missing values: None
## Results
- Logistic regression with SMOTE (10,000 transactions, 20.66% fraud):
  - F1-score: 0.877
  - Precision: 0.797
  - Recall: 0.974
  - AUC: 0.990
- Logistic regression with SMOTE (100,000 transactions, ~2-5% fraud):
  - F1-score: [Your F1]
  - Precision: [Your Precision]
  - Recall: [Your Recall]
  - AUC: [Your AUC]
- Features: amount, merchant_type, festival_flag, time_delta
- Festival_flag analysis: Fraud rate ~2% (non-festival) vs. ~4% (festival)
- ROC curve: figures/roc_curve_logistic_100k.png
- Note: 2-5% fraud aligns with real-world UPI fraud; 100,000 transactions test scalability.