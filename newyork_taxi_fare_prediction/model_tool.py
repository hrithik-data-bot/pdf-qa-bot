"""streamlit app for model"""

import streamlit as st


def main_app():
    """method for running main app"""

    lat_1 = st.number_input("Enter the source latitude:- ")
    long_1 = st.number_input("Enter the source longitude:- ")
    lat_2 = st.number_input("Enter the destination latitude:- ")
    long_2 = st.number_input("Enter the destination longitude:- ")


if __name__ == "__main__":
    main_app()
