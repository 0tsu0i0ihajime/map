import requests
import geopandas as gpd
from shapely.geometry import box

bbox = box(122.934570, 20.425615, 153.986672, 45.551483)

overpass_url = "https://overpass-api.de/api/interpreter"
overpass_query = f"""
    [out:json];
    (
        node["place"="city"](bbox);
        way["place"="city"](bbox);
        relation["place"="city"](bbox);
    );
    out center;
    """
response = requests.get(overpass_url, params={'data':overpass_query})
data = response.json()

gdf = gpd.GeoDataFrame.from_features(data['features'])