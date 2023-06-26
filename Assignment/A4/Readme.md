# General Information
This is code for A4 - it includes a `requirement.txt` for needed packages and some python files including functions that are imported in the `main.py`. I also included a yml file (`A4_env.yml`) to create a conda environment if you prefer to use that. 

This is a streamlit app that will be the basis for our final group project. In the final project we will plot power stations in Australia to a map and create a dashboard showing multiple descriptive statistics. There will also be a filter option based on fuel type, location/state and year. However, in this version, many of these functions are not yet working: instead I focus on the main task of this assignment: using functions, importing them and explaining the reasoning using docstrings. 
# Preparation
Create a conda environment based on the yml file. 
``` conda env create -f Assignment/A4/A4_env.yml ```

If you run into troubles due to problems with streamlit-folium, remove that package first from the `requirements.txt` and rerun. After the environment was successfully created, use the following line to install it directly from conda-forge: 

```conda install -c conda-forge streamlit-folium  ``` 

# How To Start
Start the `main.py` file using streamlit run in the terminal. Beware the file path: Depending on where you set the working path
``` streamlit run Assignment/A4/code/main.py ```

The other two python files contain functions that are called in the `main.py` file and create a simple web page (with not much functionality yet). 