import pandas as pd

df = pd.read_csv("../../material/mais_ouvidas_2024.csv")

print(df.head())
print(df.info())

for column in df.columns:
    if df[column].dtype == "object":
        df[column] = df[column].str.replace(",", "").astype(float, errors='ignore')

df["Release Date"] = pd.to_datetime(df["Release Date"])
print(df.dtypes)

df["Streaming Popularity"] = df[["Spotify Popularity", "YouTube Views", "TikTok Likes", "Shazam Counts"]].mean(axis=1)

print(df["Streaming Popularity"])

df["Total Streams"] = df[["Spotify Streams", "YouTube Views", "TikTok Views", "Pandora Streams", "Soundcloud Streams"]].sum(axis=1)

print(df["Total Streams"])

filtered_df = df[(df["Spotify Popularity"] > 80) & (df["Total Streams"] > 1_000_000)]

print(filtered_df.head())

filtered_df.to_json("./filtered_list.json", index=False)