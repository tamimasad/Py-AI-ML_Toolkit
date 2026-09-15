import pandas as pd
from data_preprocessing.cleaning.clean_data import clean_data

# Load the dataset
df = pd.read_csv("test/test_dataset.csv")

# 2. Display the original dataset


print("Original Dataset:")
print(df)

print("\nOriginal Shape:")
print(df.shape)


# 3. Clean the dataset


cleaned_df = clean_data(df)


# 4. Display the cleaned dataset


print("\nCleaned Dataset:")
print(cleaned_df)

print("\nCleaned Shape:")
print(cleaned_df.shape)


# 5. Save the cleaned dataset

cleaned_df.to_csv("test/cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully.")
