# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

# -----------------------
# Load the sample dataset
# -----------------------
@st.cache_data
def load_data(nrows=5000):
    df = pd.read_csv("metadata.csv", low_memory=False, nrows=nrows)
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year
    df["title_word_count"] = df["title"].fillna("").apply(lambda x: len(x.split()))
    return df

df = load_data()

# -----------------------
# Layout
# -----------------------
st.title("📊 CORD-19 Research Metadata Explorer")
st.markdown("""
This app lets you explore the **CORD-19 dataset** (COVID-19 research papers).  
Use the sidebar filters to interact with the data.
""")

# -----------------------
# Sidebar filters
# -----------------------
st.sidebar.header("Filters")

year_filter = st.sidebar.slider(
    "Select publication year",
    int(df["year"].min()) if df["year"].notna().any() else 2019,
    int(df["year"].max()) if df["year"].notna().any() else 2021,
    (2019, 2021)
)

journal_filter = st.sidebar.selectbox(
    "Select journal (or view all)",
    ["All"] + sorted(df["journal"].dropna().unique().tolist())
)

# Filtered dataset
filtered = df[
    (df["year"].between(year_filter[0], year_filter[1]))
]

if journal_filter != "All":
    filtered = filtered[filtered["journal"] == journal_filter]

# -----------------------
# Show sample data
# -----------------------
st.subheader("🔍 Sample of the data")
st.dataframe(filtered.head(10))

# -----------------------
# Visualization 1: Publications by year
# -----------------------
st.subheader("📈 Publications by Year")
pubs_per_year = filtered["year"].value_counts().sort_index()

fig, ax = plt.subplots()
sns.lineplot(x=pubs_per_year.index, y=pubs_per_year.values, marker="o", ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Publications")
st.pyplot(fig)

# -----------------------
# Visualization 2: Top journals
# -----------------------
st.subheader("📊 Top Journals (Filtered Data)")
top_journals = filtered["journal"].value_counts().head(10)

fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax, palette="Blues_r")
ax.set_xlabel("Number of Publications")
ax.set_ylabel("Journal")
st.pyplot(fig)

# -----------------------
# Visualization 3: Word Cloud of Titles
# -----------------------
st.subheader("☁️ Word Cloud of Titles")
text = " ".join(filtered["title"].dropna().tolist())
stopwords = set(STOPWORDS)
wordcloud = WordCloud(width=800, height=400, background_color="white",
                      stopwords=stopwords).generate(text)

fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit | Data source: [CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)")
# To run the app, use the command:
# streamlit run app.py
