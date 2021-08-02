'''
Script for Visualising and Dislaying Bowler's Stats IPL
'''
import base64
import streamlit as st
from config_file import bowling_stats_features
from config_file import bowlers_feature_plot_mapping
from get_stats import bowlers_stats_dataframe

def app(timeline):
    '''
    Function: to render the bowler's page on the main app.
    params: timeline
        Either a particular year or all time for displaying stats.
    returns:
        Rendered Page with all streamlit Elements
    '''


    # MAIN SCREEN ELEMENTS
    st.title("IPL Bowler Stats")
    st.markdown('''
    Comparing the Batsmen of Indian Premier League
    ''')


    # Inputs
    st.header("Inputs")
    selected_feature = st.selectbox('Feature',bowling_stats_features)


    # Display the Dataframe for the feature selected
    featurestats = bowlers_stats_dataframe(selected_feature,timeline)
    st.header(selected_feature)
    #st.dataframe(featurestats)


    # Plotting line and Bar Chart of Top 20 in the List
    feature_key = bowlers_feature_plot_mapping[selected_feature]
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


    # Download File as CSV
    st.write(" ")
    def filedownload(data_frame):
        '''
        function for download the dataframe displayed on the page as csv
        '''
        csv = data_frame.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # strings to bytes conversions
        href = f'''<a href="data:file/csv;base64,{b64}" download=
        "playerstats.csv">Download CSV File</a>'''
        return href

    st.markdown(filedownload(featurestats), unsafe_allow_html=True)


if __name__ == '__main__':
    try:
        app(2021)
    except Exception as e:
        print(e)
