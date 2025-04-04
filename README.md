"# AI Production Dashboard" 
code README.md
# AI Production Dashboard

A real-time machine performance monitoring dashboard built with **FastAPI**, **MongoDB**, and **Streamlit**.

## 🚀 Features

- Real-time data ingestion via FastAPI
- MongoDB for backend storage
- Streamlit dashboard for live performance monitoring
- Simulated machine data generation

## 📁 Project Structure

.
├── data/                  # Sample or live data files
├── scripts/               # Python scripts (data simulator, FastAPI app)
├── dashboard_app.py       # Streamlit dashboard entry point
├── requirements.txt       # Python dependencies
└── README.md              # You're here!

# 1. Clone the repository
git clone https://github.com/Priyansh025/ai-production-dashboard.git
cd ai-production-dashboard

# 2. (Optional but recommended) Create and activate a virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
# Navigate to the scripts folder
cd scripts

# Run FastAPI server
uvicorn ingest_api:app --reload
# Go back to project root if needed
cd ..

# Run Streamlit dashboard
streamlit run dashboard_app.py
