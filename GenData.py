import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime

# Initialize Faker
fake = Faker()

# Set the seed for reproducibility
np.random.seed(42)
Faker.seed(42)

# Generate 200 rows of data
num_rows = 200

# Generate the 'Sinistre' column
sinistre = np.random.randint(2034800, 2034901, num_rows)

# Generate the 'N facture' column
n_facture = [f"{random.randint(1000, 9999)}/C/{random.randint(1000, 9999)}" for _ in range(num_rows)]

# Generate the 'Date de reception' column
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 12, 31)
date_de_reception = [fake.date_between(start_date=start_date, end_date=end_date) for _ in range(num_rows)]

# Generate the 'Montant' column
montant = np.random.randint(4500, 15001, num_rows)

# Create the DataFrame
data = {
    "Sinistre": sinistre,
    "N facture": n_facture,
    "Date de reception": date_de_reception,
    "Montant": montant
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_file_path = 'synthetic_data.csv'
df.to_csv(csv_file_path, index=False)

print(f"Data table generated and saved to {csv_file_path}")
