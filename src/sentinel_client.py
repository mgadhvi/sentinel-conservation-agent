import planetary_computer
from pystac_client import Client

class SentinelClient:
    """
    Interfaces with the Microsoft Planetary Computer STAC API to retrieve
    Sentinel-2 satellite metadata.
    """

    def __init__(self):
        """Initializes the STAC client with signed access."""
        self.catalog = Client.open(
            "https://planetarycomputer.microsoft.com/api/stac/v1",
            modifier=planetary_computer.sign_inplace,
        )

    def find_latest_image(self, lat, lon):
        """
        Queries the catalog for the most recent image at given coordinates.

        Args:
            lat (float): Latitude.
            lon (float): Longitude.

        Returns:
            dict: Image metadata or None if no results are found.
        """
        bbox = [lon - 0.05, lat - 0.05, lon + 0.05, lat + 0.05]

        search = self.catalog.search(
            collections=["sentinel-2-l2a"],
            bbox=bbox,
            datetime="2024-01-01/2026-01-01",
            query={"eo:cloud_cover": {"lt": 50}},
        )
        
        items = search.item_collection()
        valid_items = [i for i in items if "visual" in i.assets]
        
        
        # Guard clause: Exit early if no valid images were found
        if not valid_items:
            return None
            
        item = valid_items[0]
        return {
            "date": item.datetime.strftime("%Y-%m-%d"),
            "cloud_cover": item.properties['eo:cloud_cover'],
            "url": item.assets['visual'].href
        }