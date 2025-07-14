# 🌲 Vancouver Parks and Elevation Analysis

This project analyzes the spatial relationship between **parks** and **elevation zones** in Vancouver, BC using Python, GeoPandas, and open data.

## 📍 Goal

- Categorize elevation using 2-meter contour data
- Join park polygons to elevation bands
- Visualize elevation zones, parks, and neighborhoods
- Generate a bar chart showing how many parks fall into each elevation range

## 📂 Data Sources

- [City of Vancouver Open Data Portal](https://opendata.vancouver.ca)
  - `elevation.geojson` (2m contour lines)
  - `parks-polygon.geojson` (park boundaries)
  - `local-area-boundary.geojson` (neighborhoods)

## 🛠 Tools Used

- Python
- GeoPandas
- Pandas
- Contextily (for basemaps)
- Matplotlib

## 🗺 Outputs

- **Map**: Color-coded elevation bands + parks + neighborhoods  
  `vancouver_parks_elevation_map.png`

- **Bar Chart**: Parks per elevation band  
  `parks_per_elevation_band.png`

```bash
python vancouver_parks_elevation.py

