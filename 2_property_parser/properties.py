# -*- coding: utf-8 -*-
"""
functions to parses 7 supercapacitor properties.

"""
import pandas as pd
import re
import os
import shutil
import json

def specific_capacitance(abstract):
    """
    Do a regex search to find the specific capacitance
    value and its unit mentioned in the abstract.
    
    """
    value, unit = [],[]

    pattern = r"(\d+(?:\.\d+)?)\s*(\bF\s*(?:g−1|\/g|\/cm2|cm-2|cm-3)\b)"
    matches = re.findall(pattern, abstract)

    for match in matches:
        value.append(match[0])
        unit.append(match[1])

    return value, unit 

def surface_area(abstract):
    """
    Do a regex search to find the surface area
    value and its unit mentioned in the abstract.
    
    """
    value, unit = [],[]
    
    pattern = r"(\d+(?:\.\d+)?)\s*(\b(?:m2/g|cm2/g|m2/cm3|m2 g-1)\b)"
    matches = re.findall(pattern, abstract)

    for match in matches:
        value.append(match[0])
        unit.append(match[1])

    return value, unit

def energy_density(abstract):
    """
    Do a regex search to find the energy density
    value and its unit mentioned in the abstract.
    
    """
    value, unit = [],[]
    
    pattern = r"(\d+(?:\.\d+)?)\s*(\b(?:J/m3|Wh/g|Wh/kg|mWh/cm3|mWh/kg)\b)"
    matches = re.findall(pattern, abstract)
    
    for match in matches:
        value.append(match[0])
        unit.append(match[1])

    return value, unit


def power_density(abstract):
    """
    Do a regex search to find the power density
    value and its unit mentioned in the abstract.
    
    """
    value, unit = [],[]
    pattern = r"(\d+(?:\.\d+)?)\s*(\b(?:W/kg|W/L|W/m3|mW/g|kW/kg)\b)"
    matches = re.findall(pattern, abstract)
    
    for match in matches:
        value.append(match[0])
        unit.append(match[1])

    return value, unit

def voltage(abstract):
    """
    Do a regex search to find the Voltage
    value and its unit mentioned in the abstract.
    
    """
    value, unit = [],[]
    pattern = r"(\d+(?:\.\d+)?)\s*(\b(?:V|volts|kilovolt|kilovolts|KV|kV)\b)"
    matches = re.findall(pattern, abstract)
    
    for match in matches:
        value.append(match[0])
        unit.append(match[1])

    return value, unit

def current_density(abstract):
    """
    Do a regex search to find the energy density
    value and its unit mentioned in the abstract.
    
    """
    value, unit = [],[]
    pattern = r"(\d+(?:\.\d+)?)\s*(\b(?:A/m2|μA/cm2|A/cm2|mA/cm2)\b)"
    matches = re.findall(pattern, abstract)
    
    for match in matches:
        value.append(match[0])
        unit.append(match[1])

    return value, unit


def cycles(abstract):
    """
    Do a regex search to find the no of cycle
    value and its unit mentioned in the abstract.
    
    """
    value, unit = [],[]
    pattern = r"(\d+(?:\.\d+)?)\s*(\b(?:cycle|cycles)\b)"
    matches = re.findall(pattern, abstract)
    
    for match in matches:
        value.append(match[0])
        unit.append(match[1])

    return value, unit








