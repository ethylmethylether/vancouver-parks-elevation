# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 17:15:25 2025

@author: Uzair
"""
import pandas as pd
import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt

# -------------------------------
# Load GeoJSON datasets
# -------------------------------
elev_zones = gpd.read_file('elevation.geojson')  # 2m contour lines
neighborhood = gpd.read_file('local-area-boundary.geojson')  # Neighborhoods
parks_b = gpd.read_file('parks-polygon.geojson')  # Park boundaries

# -------------------------------
# Reproject all to same CRS (Web Mercator for basemap compatibility)
# -------------------------------
target_crs = 'EPSG:3857'
elev_zones = elev_zones.to_crs(target_crs)
neighborhood = neighborhood.to_crs(target_crs)
parks_b = parks_b.to_crs(target_crs)

# -------------------------------
# Create elevation bands
# -------------------------------
bins = [0, 10, 20, 60, 100]
labels = ['0-10m', '10-30m', '30-60m', '60+m']
elev_zones['elev_band'] = pd.cut(elev_zones['elevation'], bins=bins, labels=labels)

# Dissolve elevation contours into bands
elev_zones = elev_zones.dissolve(by='elev_band').reset_index()

# -------------------------------
# Spatial Join: Parks with elevation bands
# -------------------------------
parks_with_elev = gpd.sjoin(parks_b, elev_zones, how='left', predicate='intersects')

# -------------------------------
# Count parks per elevation band
# -------------------------------
parks_by_band = parks_with_elev.groupby('elev_band', observed=True).size().reset_index(name='park_count')

# -------------------------------
# Map Visualization
# -------------------------------
fig, ax = plt.subplots(figsize=(12, 12))

# Plot elevation bands
elev_zones.plot(column='elev_band', legend=True, ax=ax, alpha=0.6)

# Plot neighborhood boundaries
neighborhood.plot(ax=ax, facecolor='none', edgecolor='black', alpha=0.6, linewidth=1)

# Plot park polygons
parks_b.plot(ax=ax, facecolor='green', edgecolor='darkgreen', alpha=1.0)

# Add OpenStreetMap basemap
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik, zoom=13)

plt.title('Elevation Bands and Parks of Vancouver')
plt.axis('off')
plt.tight_layout()
plt.savefig('vancouver_parks_elevation_map.png', dpi=300)
plt.show()

# -------------------------------
# Bar Chart: Parks per elevation band
# -------------------------------
plt.figure(figsize=(10, 6))
plt.bar(parks_by_band['elev_band'].astype(str), parks_by_band['park_count'], color='seagreen')

plt.title('Number of Parks per Elevation Band')
plt.xlabel('Elevation Band')
plt.ylabel('Park Count')
plt.grid(True, axis='y', linestyle='--', alpha=0.8)
plt.tight_layout()
plt.savefig('parks_per_elevation_band.png', dpi=300)
plt.show()

