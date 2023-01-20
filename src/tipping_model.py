import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class TippingPointSimulator():
    """
    Quick and dirty model to simulate in what temperature we might end up
    The model assumes that run for a hundred years
    """
    def __init__(self, temp_series):
        """
        Args:
            temp_series (list-like): The time series to be simulated. This should be the additional temperature that is to be expected per year
        Returns:
            None
        """
        self.temp_series = temp_series
        self.tipping_points = {}

    def add_tipping_point(self, name, min_temp, max_temp, distribution, min_add_warming, max_add_warming, min_lag, max_lag, min_chance, max_chance):
        """
        Adds a new tipping point to the model
        Args:
            name (str): Name of the tipping point
            min_temp (float): Minimum temperature for the tipping point to occur
            max_temp (float): Maximum temperature for the tipping point to occur
            distribution (str): Distribution of the tipping point. Options are 'uniform' and 'normal'
            min_add_warming (float): Minimum additional warming caused by the tipping point
            max_add_warming (float): Maximum additional warming caused by the tipping point
            min_lag (float): Minimum lag time of the tipping point
            max_lag (float): Maximum lag time of the tipping point
            min_chance (float): Minimum chance of the tipping point to occur
            max_chance (float): Maximum chance of the tipping point to occur
        Returns:
            None
        """
        # Add a tipping point to the modeldata
        self.tipping_points[name] = {
            'min_temp': min_temp,
            'max_temp': max_temp,
            'distribution': distribution,
            'min_add_warming': min_add_warming,
            'max_add_warming': max_add_warming,
            # Indicate if the tipping point has already been triggered
            "triggered": False
        }
        
    def tipping_point_probability(self):
        

    def initialize_tipping_points(self):
        """
        Initialize tipping points in their given range with the given distribution
        """
        # Check if there are tipping points
        assert len(self.tipping_points) > 0, "No tipping points defined"
        # Iterate over all tippings points
        for name, tipping_point_data in self.tipping_points.items():
            # Sample the actual temperature of the tipping point with the given distribution
            if tipping_point_data["distribution"] == "uniform":
                self.tipping_points["actual_tip_temp"] = np.random.uniform(tipping_point_data["min_temp"], tipping_point_data["max_temp"])
            elif tipping_point_data["distribution"] == "normal":
                self.tipping_points["actual_tip_temp"] = np.random.normal(tipping_point_data["min_temp"], tipping_point_data["max_temp"])
            # Sample the additional warming caused by the tipping point given the distribution
            if tipping_point_data["distribution"] == "uniform":
                self.tipping_points["actual_add_warming"] = np.random.uniform(tipping_point_data["min_add_warming"], tipping_point_data["max_add_warming"])
            elif tipping_point_data["distribution"] == "normal":
                self.tipping_points["actual_add_warming"] = np.random.normal(tipping_point_data["min_add_warming"], tipping_point_data["max_add_warming"])
            # Sample the lag time of the tipping point given the distribution
            if tipping_point_data["distribution"] == "uniform":
                self.tipping_points["actual_lag"] = np.random.uniform(tipping_point_data["min_lag"], tipping_point_data["max_lag"])
            elif tipping_point_data["distribution"] == "normal":
                self.tipping_points["actual_lag"] = np.random.normal(tipping_point_data["min_lag"], tipping_point_data["max_lag"])
            # Sample the chance of the tipping point to occur given the distribution
            if tipping_point_data["distribution"] == "uniform":
                self.tipping_points["actual_chance"] = np.random.uniform(tipping_point_data["min_chance"], tipping_point_data["max_chance"])
            elif tipping_point_data["distribution"] == "normal":
                self.tipping_points["actual_chance"] = np.random.normal(tipping_point_data["min_chance"], tipping_point_data["max_chance"])


    def run_1(self):
        """
        Run the model for one iteration
        """
        # Create a dataframe to save the results
        temp_df = pd.DataFrame(self.temp_series)
        # Create values for the tipping points
        self.initialize_tipping_points()
        # Go through each year and check if any of the tipping points is triggered
        for year in range(101):

        
            




    def run_n(self, n):