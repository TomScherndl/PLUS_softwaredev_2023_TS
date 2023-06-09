### Main Streamlit Page
'''
This is the main page including all elements (dashboard, map, data preparation) for the final project
'''
## import relevant modules

import streamlit as st
import folium

# import local python files that are used for further 
import dashboard
import preprocess

###---------------
# preprocess / get data
dataPS = preprocess.getPowerStationData()
''''
Here we get data and filter it based on the country: we will focus only on Australia even if many other countries are available as well.
We then show the first 6 data points and show the overall dimensions of the resulting data frame.. 
'''
# show data - only prelim
st.dataframe(dataPS.head(6))
st.write(dataPS.shape)

# this set-ups the sidebar
dashboard.sidebar()

# this sets up the main page (above map)
dashboard.titlePage()

# now we create the map based on information/filter obtained in sidebar
dashboard.map()

# last, this includeds the statistics and plots below the map in the dashboard
dashboard.dashboard()