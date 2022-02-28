import json

def parse_geom(geom_str):
    """
Parse GeoJson geoms if needed.

geom_str: geom column

Example:
df['geom']=df['geom].apply(prase_geom)
   """

    try:
        return shape(json.loads(geom_str))
    except (TypeError, AttributeError):  # Handle NaN and empty strings
        return None