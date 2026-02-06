import planetary_computer
from pystac_client import Client
from src.config import CLOUD_THRESHOLD

class SentinelClient:
    """
    A client for searching and retrieving Sentinel-2 satellite imagery
    from the Microsoft Planetary Computer STAC API.
    """

    def __init__(self):
        """Initialises the STAC client with signed access to the planetary catalog."""
        self.catalog = Client.open(
            "https://planetarycomputer.microsoft.com/api/stac/v1",
            modifier=planetary_computer.sign_inplace,
        )

    def find_latest_image(self, lat, lon):
        """
        Searches for the most recent Sentinel-2 image at a specific coordinate.

        Args:
            lat (float): Latitude of the target location.
            lon (float): Longitude of the target location.

        Returns:
            dict: Metadata of the found image (date, cloud cover, and URL) 
                  or None if no image is found.
        """
        # Define a small bounding box (~5km) around the coordinates
        bbox = [lon - 0.05, lat - 0.05, lon + 0.05, lat + 0.05]

        # Search for Sentinel-2 Level 2A data
        search = self.catalog.search(
            collections=["sentinel-2-l2a"],
            bbox=bbox,
            datetime="2024-01-01/2026-01-01",
            query={"eo:cloud_cover": {"lt": 50}}, # Broad filter for initial search
        )
        
        items = search.item_collection()
        
        # Ensure the item has a visual (RGB) asset available
        valid_items = [i for i in items if "visual" in i.assets]
        
        if not valid_items:
            return None
            
        # Select the most recent image
        item = valid_items[0]
        return {
            "date": item.datetime.strftime("%Y-%m-%d"),
            "cloud_cover": item.properties['eo:cloud_cover'],
            "url": item.assets['visual'].href
        }