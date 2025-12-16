import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import f1_score, precision_score, recall_score, roc_curve, auc, accuracy_score, confusion_matrix, roc_auc_score
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
import seaborn as sns

SAVE_DIR = r"C:\Users\Varsha\UPI-detection"
os.makedirs(SAVE_DIR, exist_ok=True)
PLOT_PATH = os.path.join(SAVE_DIR, 'figures', 'roc_curve_svm_100k.png')
CM_PATH = os.path.join(SAVE_DIR, 'figures', 'cm_svm_100k.png')
os.makedirs(os.path.join(SAVE_DIR, 'figures'), exist_ok=True)

df = pd.read_csv(os.path.join(SAVE_DIR, 'upi_transactions.csv'))
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['time_delta'] = df['timestamp'].diff().dt.total_seconds().fillna(0)
X = df[['amount', 'merchant_type', 'festival_flag', 'time_delta']]
y = df['is_fraud']

print("Merchant types:", df['merchant_type'].unique())
print("Fraud ratio:", df['is_fraud'].mean())

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), ['amount', 'festival_flag', 'time_delta']),
    ('cat', OneHotEncoder(sparse_output=False), ['merchant_type'])
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_preprocessed = preprocessor.fit_transform(X_train)
X_test_preprocessed = preprocessor.transform(X_test)

smote = SMOTE(random_state=42, sampling_strategy=0.5)
X_train_smote, y_train_smote = smote.fit_resample(X_train_preprocessed, y_train)
print("Post-SMOTE class balance:", pd.Series(y_train_smote).value_counts())

model = SVC(class_weight='balanced', probability=True, random_state=42, max_iter=1000)
model.fit(X_train_smote, y_train_smote)

y_pred = model.predict(X_test_preprocessed)
y_pred_proba = model.predict_proba(X_test_preprocessed)[:, 1]

# Evaluation Metrics
print(f"SVM Accuracy: {accuracy_score(y_test, y_pred):.3f}")
print(f"SVM Precision: {precision_score(y_test, y_pred):.3f}")
print(f"SVM Recall: {recall_score(y_test, y_pred):.3f}")
print(f"SVM F1-score: {f1_score(y_test, y_pred):.3f}")
print(f"SVM AUC-ROC: {roc_auc_score(y_test, y_pred_proba):.3f}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix - SVM (100k)')
plt.xlabel('Predicted')
plt.ylabel('Actual')
try:
    plt.savefig(CM_PATH, dpi=300, bbox_inches='tight')
    print(f"Confusion matrix saved to: {CM_PATH}")
except Exception as e:
    print(f"Error saving confusion matrix: {e}")
plt.show()
plt.close()

# ROC Curve
plt.figure(figsize=(8, 6))
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
auc_score = auc(fpr, tpr)
print(f"SVM AUC: {auc_score:.3f}")
plt.plot(fpr, tpr, label=f'SVM ROC curve (AUC = {auc_score:.3f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('SVM ROC Curve (100k)')
plt.legend()
try:
    plt.savefig(PLOT_PATH, dpi=300, bbox_inches='tight')
    print(f"ROC curve saved to: {PLOT_PATH}")
except Exception as e:
    print(f"Error saving ROC curve: {e}")
plt.show()
plt.close()