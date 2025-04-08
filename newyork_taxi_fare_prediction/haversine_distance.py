"""module for haversine distance"""

from dataclasses import dataclass

@dataclass
class HaversineDistance:
    """class for calculating haversine distance"""
    
    latitude: float
    longitude: float
    
    def calculate_haversine(self) -> float:
        """method calculates haversine distance"""

        pass