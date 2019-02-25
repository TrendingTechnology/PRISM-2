# -*- coding: utf-8 -*-

# Future imports
from __future__ import absolute_import, division, print_function

# Package imports
import numpy as np

# PRISM imports
from prism.modellink import ModelLink


# LineLink class definition
class LineLink(ModelLink):
    def __init__(self, *args, **kwargs):
        # No custom operations required
        pass

        # Call ModelLink's __init__()
        super().__init__(*args, **kwargs)

    def get_default_model_parameters(self):
        # Define default parameters (not required)
        par_dict = {
            'A': [-10, 10, 3],  # Intercept in [-10, 10] with estimate of 3
            'B': [0, 5, 1.5]}   # Slope in [0, 5] with estimate of 1.5
        return(par_dict)

    def get_default_model_data(self):
        # Define default data (not required)
        data_dict = {
            1: [4.5, 0.1],    # f(1) = 4.5 +- 0.1
            2.5: [6.8, 0.1],  # f(2.5) = 6.8 +- 0.1
            -2: [0, 0.1]}     # f(-2) = 0 +- 0.1
        return(data_dict)

    # Override call_model method
    def call_model(self, emul_i, par_set, data_idx):
        # Calculate the value on a straight line for requested data_idx
        vals = par_set['A']+np.array(data_idx)*par_set['B']
        return(vals)

    # Override get_md_var method
    def get_md_var(self, emul_i, par_set, data_idx):
        # Calculate the model discrepancy variance
        # For a straight line, this value can be set to a constant
        return(1e-4*np.ones_like(data_idx))
