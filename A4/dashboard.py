import streamlit as st
def titlePage(data = None): 
    '''
    Print information on top of page. Also includes additional info about the project. 
    '''
    st.markdown("# Visualisation of Power Stations in Australia")
    st.markdown("Please select power stations on the left and generate the map and dashboard!")


def sidebar(): 
    '''
    Print information in sidebar - mostly used for filtering
    '''
    with st.sidebar: 
        st.write("## Select Data and Filter \n This is info in the sidebar! Later we will include filter options!")


def map(): 
    '''
    This function is for creating and updating the map
    '''
    import folium 
    from streamlit_folium import folium_static

    st.markdown("## Map \n This is a placeholder for the interactive map. This is only static (but you may zoom already) :)")
    m = folium.Map([-38, 145], 
                   zoom_start=3)
    # print the map
    folium_static(m)

def dashboard(data = None): 
    ''''
    This function is for printing the relevant statistics and graphs below the map
    '''
    st.markdown("## Statistics and Data \n This is text for the dashboard (=below the map) from the respective function. ")