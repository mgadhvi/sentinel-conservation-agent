import folium

def create_location_map(lat, lon, date, output_path="map.html"):
    """
    Generates an interactive HTML map centered on the satellite image coordinates.
    """
    # Initialize the map using a clean, professional base layer
    m = folium.Map(location=[lat, lon], zoom_start=10, tiles="CartoDB positron")

    # Add a specialized marker for the conservation site
    folium.Marker(
        [lat, lon],
        popup=f"<b>Sentinel-2 Capture</b><br>Date: {date}",
        tooltip="View Analysis Site",
        icon=folium.Icon(color="green", icon="leaf", prefix="fa")
    ).add_to(m)

    m.save(output_path)
    return output_path