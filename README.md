
# 🌍 Real-Time Earthquake Monitoring Webapp

An interactive web application built using **Python, Streamlit, Pandas, and Plotly** to monitor recent earthquakes and explore earthquake activity over the past month using data from the **US Geological Survey (USGS)**.

The application displays earthquake locations on interactive maps and allows users to filter earthquakes based on their magnitude.

## ✨ Features

- **Real-Time Data:** Fetches earthquake data recorded in the last hour.
- **Historical Data:** Displays earthquake records from the last month.
- **Interactive Maps:** Visualizes earthquake locations using Plotly.
- **Magnitude Filter:** Filter earthquakes using a minimum magnitude slider.
- **Earthquake Details:** View location, magnitude, latitude, longitude, and timestamps.
- **Timezone Conversion:** Displays earthquake timestamps in UTC and Los Angeles local time.
- **Data Tables:** Explore filtered real-time and historical earthquake records.
- **Error Handling:** Displays an error message if the API request fails.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Plotly Express
- Requests
- USGS Earthquake API

## 📂 Project Structure

```text
earthquake-monitoring/
│
├── app.py
├── requirements.txt
└── README.md
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

Navigate to the project directory:

```bash
cd earthquake-monitoring
```

### 2. Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL, usually:

http://localhost:8501

Open the URL in your browser to use the application.

## 🌐 Data Source

This project uses publicly available earthquake feeds from the US Geological Survey (USGS).

- **Last Hour Feed:**  
  https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson

- **Last Month Feed:**  
  https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson

The application retrieves the data through HTTP requests and processes the GeoJSON response using Pandas.

## 📊 How It Works

1. Fetches earthquake records from the USGS API.
2. Extracts earthquake locations, magnitudes, and timestamps.
3. Converts UTC timestamps to Los Angeles local time.
4. Filters records according to the selected minimum magnitude.
5. Displays earthquake locations on interactive maps.
6. Presents the filtered records in data tables.

## 🎯 Project Objective

The objective of this project is to demonstrate how public APIs, data processing, and interactive visualizations can be combined to build a simple earthquake monitoring dashboard.

## 🔮 Future Improvements

- Add automatic data refresh at regular intervals.
- Include magnitude-based alerts for significant earthquakes.
- Add filters for date, location, and depth.
- Display earthquake depth and magnitude statistics.
- Add a global earthquake heatmap.
- Deploy the application online using Streamlit Community Cloud.

## 👩‍💻 Author

**Haadiya Faruqi**

AI Student & Developer

## 📄 License

This project is intended for educational and learning purposes.
