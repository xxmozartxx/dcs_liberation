from dataclasses import dataclass
import pickle
from typing import Optional, Tuple, Union
import logging

from shapely import geometry
from shapely.geometry import MultiPolygon, Polygon


@dataclass(frozen=True)
class Landmap:
    inclusion_zones: MultiPolygon
    exclusion_zones: MultiPolygon
    sea_zones: MultiPolygon


def load_landmap(filename: str) -> Optional[Landmap]:
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except:
        logging.exception(f"Failed to load landmap {filename}")
        return None


def poly_contains(x, y, poly: Union[MultiPolygon, Polygon]):
    return poly.contains(geometry.Point(x, y))


def poly_centroid(poly) -> Tuple[float, float]:
    x_list = [vertex[0] for vertex in poly]
    y_list = [vertex[1] for vertex in poly]
    x = sum(x_list) / len(poly)
    y = sum(y_list) / len(poly)
    return (x, y)

