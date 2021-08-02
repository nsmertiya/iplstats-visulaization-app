'''
Main File for the IPL Stats Applications
'''
import streamlit as st
import batsmen_app_page
import bowler_app_page
import team_stats_page
from config_file import timeline_list


def main():
    '''
    main page to navigate to other pages
    '''

    navigation_pages = {
        "Batsmen": batsmen_app_page,
        "Bowler": bowler_app_page,
        "Teams": team_stats_page
            }
    st.sidebar.title('Navigation')
    page_selection = st.sidebar.radio("Go to", list(navigation_pages.keys()))
    timeline_selection = st.sidebar.selectbox("Year",timeline_list)
    page = navigation_pages[page_selection]
    page.app(timeline_selection)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
