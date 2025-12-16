import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker('en_IN')
n = 100000
data = {
        'amount': [random.uniform(10, 50000) for _ in range(n)],
        'timestamp': [fake.date_time_this_year() for _ in range(n)],
        'merchant_type': [random.choice(['grocery', 'temple', 'e-commerce', 'travel']) for _ in range(n)],
        'festival_flag': [1 if random.random() < 0.2045 else 0 for _ in range(n)],
        'is_fraud': [0] * n
    }
df = pd.DataFrame(data)
df['is_fraud'] = ((df['amount'] > 5000) & (np.random.random(n) < 0.025)) | \
                ((df['festival_flag'] == 1) & (np.random.random(n) < 0.05))
df['is_fraud'] = df['is_fraud'].astype(int)
df.to_csv(r"C:\Users\Varsha\UPI-detection\upi_transactions.csv", index=False)
print("Dataset size:", len(df))
print("Fraud ratio:", df['is_fraud'].mean())
print("Festival_flag ratio:", df['festival_flag'].mean())
print("Merchant types:", df['merchant_type'].unique())
print("Feature stats:", df[['amount', 'festival_flag', 'is_fraud']].describe())