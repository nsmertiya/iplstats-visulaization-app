'''
Script for Displaying and Visualising the Points Table for Various Years
'''
import streamlit as st
import altair as alt
from get_stats import player_stats_dataframe

def app(timeline):
    '''
        Function: to render the points table page on the main app.
        params: timeline
            Either a particular year or all time for displaying stats.
        returns:
            Rendered Page with all streamlit Elements
    '''
    # Since 'all-time' doesnt exist for points table, changing to default 2021
    if timeline=='all-time':
        timeline=2021


    # Main Elements
    st.title(f"IPL Points Table {timeline}")
    st.markdown('''
    Match Stats and Point Table of Indian Premier League Teams
    ''')


    # Display Points Table
    data = player_stats_dataframe(timeline)
    st.dataframe(data)
    st.header("Plot Feature")
    selected_feature = st.selectbox('Feature',list(['Won','Lost','Tied','N/R'
    'Net RR','Pts']))


    # Plot Selected Feature as Bar Chart
    plot_data = data.rename(columns={'Team':'index'}).set_index('index')
    plot_data = plot_data[selected_feature]
    st.write("Matches Won by Each Team")
    st.bar_chart(plot_data.sort_values(ascending=False))


    # Plot Wins and Losses
    st.write(" ")
    st.write("Altair Map to see the Impact of Boundaries on Total Runs")
    vega_plot_data = data
    st.write(" ")
    chart = alt.Chart(vega_plot_data).mark_circle().encode(
         x='Won', y='Lost', size='Team', tooltip=['Won', 'Lost', 'Team'])
    st.write(chart)


if __name__ == '__main__':
    try:
        app(2021)
    except Exception as e:
        print(e)
