"""Data utils"""

"""
Copyright 2023-2024 Blue Brain Project / EPFL

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import csv
from importlib import resources

import numpy as np


def get_dendritic_data_filepath(data_type):
    """Gets a dendritic data file path.

    Args:
        data_type (str): can be 'ISI_CV' or 'rheobase'

    Raises:
        ValueError if data_type is not 'ISI_CV' nor 'rheobase'
    """
    if data_type == "ISI_CV":
        return resources.files("bluepyemodel") / "data" / "ISI_CV_Shai2015.csv"
    if data_type == "rheobase":
        return (
            resources.files("bluepyemodel") / "data" / "spike_rheobase_pA_BeaulieuLaroche2021.csv"
        )

    raise ValueError(f"read_data expects 'ISI_CV' or 'rheobase' but got {data_type}")


def read_dendritic_data(data_type):
    """Reads a dendritic data file and returns distance and data values.

    rheobase values are returned in nA.

    Args:
        data_type (str): can be 'ISI_CV' or 'rheobase'
    """
    file_path = get_dendritic_data_filepath(data_type)

    data = []
    distances = []
    with open(file_path, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for distance, dat in csvreader:
            distances.append(float(distance))
            data.append(float(dat))

    if data_type == "rheobase":
        data = np.asarray(data) / 1000.0  # pA -> nA
    return np.asarray(distances), data
