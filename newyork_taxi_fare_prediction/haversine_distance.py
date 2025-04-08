"""module for haversine distance"""

from typing import Tuple
from dataclasses import dataclass
import numpy as np


@dataclass
class HaversineDistance:
    """class for calculating haversine distance"""
    
    coordinates_1: Tuple
    coordinates_2: Tuple
    
    def calculate_haversine(self, kilometers: float = True) -> float:
        """method calculates haversine distance
           set parameter kilometers = False to get distane in miles.
        """

        radius_of_sphere = 6371.0 if kilometres==True else 3956.0
        lat_1, long_1 = self.coordinates_1
        lat_2, long_2 = self.coordinates_2
        d_lat = np.radians(lat_2) - np.radians(lat_1)
        d_long = np.radians(long_2) - np.radians(long_1)
        a = np.sin(d_lat/2)**2 + np.cos(np.radians(lat_1)) * np.cos(np.radians(lat_2)) * np.sin(d_long/2)**2
        c = 2*np.arcsin(np.sqrt(a))
        haversine_distance = c*radius_of_sphere
        return haversine_distance
