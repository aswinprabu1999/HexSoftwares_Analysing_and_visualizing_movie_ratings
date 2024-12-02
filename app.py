import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the preprocessed data
df = pd.read_csv(r'C:\Users\Aswin prabu\.cache\kagglehub\datasets\thedevastator\imdb-movie-ratings-dataset\versions\2\movie_data.csv')

# Calculate summary statistics
mean_rating = df['imdb_score'].mean()
median_rating = df['imdb_score'].median()
mode_rating = df['imdb_score'].mode()[0]

# Streamlit UI components
st.title("Movie Ratings Dashboard")

st.write("### Summary Statistics")
st.write(f"Mean IMDb Rating: {mean_rating}")
st.write(f"Median IMDb Rating: {median_rating}")
st.write(f"Mode IMDb Rating: {mode_rating}")

# Add your visualizations, for example, a histogram
st.write("### Rating Distribution")

# Create the histogram using matplotlib
plt.figure(figsize=(10,6))
plt.hist(df['imdb_score'], bins=20, edgecolor='black')
plt.title('IMDb Rating Distribution')
plt.xlabel('IMDb Rating')
plt.ylabel('Frequency')

# Show top-rated movies
top_rated = df[['movie_title', 'imdb_score']].sort_values(by='imdb_score', ascending=False).head(10)
st.write("### Top 10 Movies")
st.write(top_rated)

# Display the plot with Streamlit
st.pyplot(plt)
