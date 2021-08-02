'''
Script for Visualising and Dislaying Batsmen's Stats IPL
'''
import base64
import streamlit as st
import altair as alt
from get_stats import batsmen_stats_dataframe
from config_file import feature_plot_mapping
from config_file import batting_stats_features

def app(timeline):
    '''
    Function: to render the batsman page on the main app.
    params: timeline
        Either a particular year or all time for displaying stats.
    returns:
        Rendered Page with all streamlit Elements
    '''

    # MAIN SCREEN ELEMENTS
    st.title("IPL Batsmens Stats")
    st.markdown('''
    Comparing the Batsmen of Indian Premier League
    ''')


    # Inputs
    st.header("Inputs")
    selected_feature = st.selectbox('Feature',batting_stats_features)


    # Display the Dataframe for the feature selected
    featurestats = batsmen_stats_dataframe(selected_feature,timeline)
    st.header(selected_feature)


    # Plotting line and Bar Chart of Top 20 in the List
    feature_key = feature_plot_mapping[selected_feature]
    plot_data = featurestats.sort_values(by=feature_key, ascending=False)
    plot_data = plot_data[:20]
    st.dataframe(plot_data)
    plot_data = plot_data.rename(columns={'PLAYER':'index'}).set_index('index')
    plot_data = plot_data[feature_key]
    st.write(" ")
    st.write(f"Line Chart for the Top 20 players with {feature_key}")
    st.line_chart(plot_data.sort_values(ascending=False))
    st.write(" ")
    st.write(f"Bar Chart for the Top 20 players with {feature_key}")
    st.bar_chart(plot_data.sort_values(ascending=False))


    # Altair Maps for 4s and 6s
    st.write(" ")
    st.write("Altair Map to see the Impact of Boundaries on Total Runs")
    vega_plot_data = featurestats[["PLAYER","4s","6s","Runs"]][:10]
    st.dataframe(vega_plot_data)
    st.write(" ")
    alt_chart = alt.Chart(vega_plot_data).mark_circle().encode(
         x='4s', y='6s', size='PLAYER', tooltip=['4s', '6s', 'PLAYER'])
    st.write(alt_chart)


    # Download File as CSV
    st.write(" ")
    def filedownload(data_frame):
        '''
        function for download the dataframe displayed on the page as csv
        '''
        csv = data_frame.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'''<a href="data:file/csv;base64,{b64}" download=
        "playerstats.csv">Download CSV File</a>'''
        return href

    st.markdown(filedownload(featurestats), unsafe_allow_html=True)


if __name__ == '__main__':
    try:
        app(2021)
    except Exception as e:
        print(e)
