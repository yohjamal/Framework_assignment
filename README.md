COVID-19 Metadata Analysis

This project explores the CORD-19 metadata dataset using Python, Jupyter, and Streamlit.
It includes:

Data cleaning and analysis with pandas

Visualizations with matplotlib, seaborn, and wordcloud

An interactive Streamlit app to explore results

📂 Project Structure
Framework_assignment/
│── analysis.py / analysis.ipynb   # Data analysis code / notebook
│── app.py                         # Streamlit app
│── requirements.txt               # Dependencies
│── README.md                      # Documentation
│── metadata.csv                   # dataset (10k rows)

⚙️ Setup Instructions
1. Clone the repository / move into project folder
cd C:\Users\Emily\OneDrive\Documents\Framework_assignment

2. Create a virtual environment
python -m venv venv

3. Activate the environment

On Windows (PowerShell):

.\venv\Scripts\Activate


On Git Bash or Linux/Mac:

source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

▶️ Running the Project
Run Jupyter Notebook for analysis
jupyter lab


(Open analysis.ipynb to explore the data.)

Run the Streamlit app
streamlit run app.py


Then open 👉 http://localhost:8502
 in your browser.

✅ Features

Explore metadata with pandas

Visualize trends (publications per year, top journals, word clouds)

Interactive UI with Streamlit (filters, dropdowns, sliders)
