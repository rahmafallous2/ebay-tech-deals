import pandas as pd


columns = ["timestamp", "title", "price", "original_price", "shipping", "item_url"]
df = pd.read_csv("ebay_tech_deals.csv", names=columns, header=0, dtype=str)

for col in ["price", "original_price"]:
    df[col] = df[col].str.replace("US", "", regex=False)
    df[col] = df[col].str.replace("$", "", regex=False)
    df[col] = df[col].str.replace(",", "", regex=False)
    df[col] = df[col].str.strip()

df["original_price"] = df["original_price"].replace(["", "N/A"], pd.NA)
df["original_price"] = df["original_price"].fillna(df["price"])


df["shipping"] = df["shipping"].replace(["", "N/A"], pd.NA)
df["shipping"] = df["shipping"].fillna("Shipping info unavailable")


df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["original_price"] = pd.to_numeric(df["original_price"], errors="coerce")

df["discount_percentage"] = ((df["original_price"] - df["price"]) /
                             df["original_price"] * 100).round(2)


df.drop_duplicates(subset=['item_url'], inplace=True)

df.to_csv("cleaned_ebay_deals.csv", index=False)
print(f"Cleaned data saved successfully with {len(df)} rows!")

print("Total rows:", len(df))
print("Unique URLs:", df["item_url"].nunique())
print("Unique Titles:", df["title"].nunique())
