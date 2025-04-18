# 🦈 Global Shark Attacks Visualization

This is an interactive data visualization app built using **Streamlit** to explore global shark attack statistics. Users can view the distribution of total and fatal shark attacks for different countries using an interactive pie chart.

## 📊 Features

- Reads shark attack data from an Excel file (`.xlsx`)
- Interactive pie chart comparing **total attacks** vs **fatal attacks** per country
- Slider to select country by index
- Built using:
  - `Streamlit` for UI
  - `pandas` for data processing
  - `matplotlib` for visualization
  - `openpyxl` for reading Excel files

---

## 🗂️ Project Structure

global-shark-attacks-visualization/ ├── app.py # Streamlit app code ├── global_shark_attacks.xlsx # Excel file containing the dataset ├── requirements.txt # Python dependencies ├── README.md # Project documentation (this file) └── .gitignore # Optional Git ignore file


---

## 📌 Prerequisites

Make sure Python is installed (recommended version: Python 3.8+).

Install dependencies using:

```bash
pip install -r requirements.txt

🚀 How to Run the App

# 1. Clone the repository
git clone https://github.com/your-username/global-shark-attacks-visualization.git
cd global-shark-attacks-visualization

# 2. (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate     # On Windows
# OR
source venv/bin/activate  # On macOS/Linux

# 3. Install the required libraries
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py

Once it's running, open your browser and go to http://localhost:8501