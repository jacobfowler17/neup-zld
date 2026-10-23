"""
helpers.py

Contains various utility functions that are used multiple times in the neup-zld project code.
"""


def unpack_sweep_params(sweep_params: dict):
    sweep_names  = []
    sweep_values = []
    for k,v in sweep_params.items():
        sweep_names.append(k)
        sweep_values.append(v)
    return sweep_names, sweep_values