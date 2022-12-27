import streamlit as st
import textblob

st.title('Sentiment Analysis App')

# Get user input
text = st.text_input('Enter some text:')

# Analyze the sentiment of the text
sentiment = textblob.TextBlob(text).sentiment.polarity

# Display the results
if sentiment > 0:
    st.success('Positive')
elif sentiment < 0:
    st.error('Negative')
else:
    st.info('Neutral')
