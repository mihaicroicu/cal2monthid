import streamlit as st
from datetime import datetime
from ViewsMonth import ViewsMonth

# Title of the app
st.title('Date to month_id')

# User input for the date
selected_date = st.date_input("Select a date", min_value=datetime(1980,1,1), max_value=datetime(2050,12,31))

# Check if the date is selected
if selected_date:
    month_id = ViewsMonth.from_date(selected_date).id
    text_out = f'''<p>Month_id for {selected_date.year} - {selected_date.month:02} is : <br> 
    <span style="font-family:Courier; color:White; font-size: 40px;">{month_id}</s></p><p>Other months in {selected_date.year}: <br>'''
    sub_header = '<span style="font-family:Courier;color:#ced9e4; font-size:12px;">'
    sub_footer = '</s><br>'
    for i in range(12):
        month_id = ViewsMonth.from_year_month(selected_date.year, i+1).id
        text_out += sub_header+f'{selected_date.year}-{i+1:02} : {month_id}'+sub_footer
    text_out += "</p>"
    st.markdown(text_out, unsafe_allow_html=True)

    #st.write(f"The week number for {selected_date} is: {week_number}")
else:
    # Prompt user to select a date
    month_id = ViewsMonth.now().id
    original_title = f'Current month_id is : <span style="font-family:Courier; color:White; font-size: 40px;">{month_id}</s>'
    st.markdown(original_title, unsafe_allow_html=True)

