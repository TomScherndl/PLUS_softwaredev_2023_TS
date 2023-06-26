def getPowerStationData(file = "Assignment/A4/data/global_power_plant_database.csv"): 
    """Imports the Powerstation Data (csv) into a data frame and saves it into session_state!

    Args:
        file (str, optional): path to csv file containing power stations  in Australia. Defaults to "FinalProject\PLUS_softwaredev_2023_PowerGeneration\data\global_power_plant_database.csv".

    Returns:
        data (pd.DataFrame): content of csv file 
    """
    
    import pandas as pd
    import streamlit as st

    data = pd.read_csv(filepath_or_buffer=file)
    # put it into session state for later use - also in other modules!
    data = data[data["country_long"] == "Australia"]
    st.session_state["dataPS"] = data
    return data