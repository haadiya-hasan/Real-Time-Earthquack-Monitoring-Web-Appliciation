
import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# Function to fetch earthquake data
def fetch_earthquake_data(url):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()

        earthquakes = []

        for feature in data["features"]:
            properties = feature["properties"]
            geometry = feature["geometry"]

            utc_time = pd.to_datetime(
                properties["time"], unit="ms", utc=True
            )

            local_time = utc_time.tz_convert("America/Los_Angeles")

            earthquakes.append({
                "place": properties["place"],
                "magnitude": properties["mag"],
                "time_utc": utc_time,
                "time_local": local_time,
                "latitude": geometry["coordinates"][1],
                "longitude": geometry["coordinates"][0]
            })

        return pd.DataFrame(earthquakes)

    except (requests.RequestException, ValueError, KeyError) as e:
        st.error(f"Unable to fetch earthquake data: {e}")
        return pd.DataFrame()

# USGS earthquake data URLs
realtime_url = (
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/"
    "summary/all_hour.geojson"
)

historical_url = (
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/"
    "summary/all_month.geojson"
)

# Fetch earthquake data
realtime_data = fetch_earthquake_data(realtime_url)
historical_data = fetch_earthquake_data(historical_url)

# Streamlit app layout
st.title("Real-Time Earthquake Monitoring Webapp")

st.markdown(
    "This app visualizes real-time and historical earthquake "
    "data from the US Geological Survey (USGS)."
)

# Filter by magnitude
min_magnitude = st.slider(
    "Minimum Magnitude",
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=0.1
)

filtered_realtime = realtime_data[
    realtime_data["magnitude"] >= min_magnitude
] if not realtime_data.empty else realtime_data

filtered_historical = historical_data[
    historical_data["magnitude"] >= min_magnitude
] if not historical_data.empty else historical_data

# Function to display earthquake maps
def display_earthquake_map(data, title):
    if data.empty:
        st.info("No earthquake data available for this selection.")
        return

    fig = px.scatter_map(
        data,
        lat="latitude",
        lon="longitude",
        size="magnitude",
        color="magnitude",
        hover_name="place",
        hover_data=["time_utc", "time_local", "magnitude"],
        zoom=1,
        height=600,
        title=title
    )

    st.plotly_chart(fig, use_container_width=True)

# Display maps
st.subheader("Recent Earthquakes")
display_earthquake_map(
    filtered_realtime, "Recent Earthquakes (Last Hour)"
)

st.subheader("Historical Earthquakes")
display_earthquake_map(
    filtered_historical, "Historical Earthquakes (Last Month)"
)

# Display raw data
st.subheader("Filtered Real-Time Earthquake Data")
st.dataframe(filtered_realtime, use_container_width=True)

st.subheader("Filtered Historical Earthquake Data")
st.dataframe(filtered_historical, use_container_width=True)

# Sidebar information
st.sidebar.subheader("About This App")
st.sidebar.info(
    "This application fetches earthquake data from the USGS API "
    "and displays it on interactive maps. Use the slider to filter "
    "earthquakes by magnitude. Times are shown in UTC and "
    "Los Angeles local time."
)
