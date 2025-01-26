import streamlit as st
import pandas as pd
import base64

st.title('Ur Netlifx Buddy')

def load_gif(file_path):
    with open(file_path, "rb") as f:
        contents = f.read()
        data_url = base64.b64encode(contents).decode("utf-8")
    return data_url

gif_path = "clickwisedemo/Video (2).gif" 
gif_data_url = load_gif(gif_path)

def recommendation():

    st.write("Recommendation")
    movies = pd.read_csv('clickwisedemo/movies.csv')
    tvshows = pd.read_csv('clickwisedemo/tvshows.csv')

    options1 = ['TV Shows', 'Movies']
    selected_category = st.selectbox('Choose a category:', options1)

    if selected_category == 'TV Shows':
        uniquecat = tvshows['listed_in'].unique()
        selectedcat = st.selectbox(
            'Select Category',
            options = uniquecat,
            index=0 )
        filtered_tv = tvshows[tvshows['listed_in'] == selectedcat]

        if filtered_tv.empty:
            st.write("No data available for the selected category.")
        else:
            random_items = filtered_tv.sample(n=3)
            for index, row in random_items.iterrows():
                title = row['title']
                rating = row['rating']
                duration = row['duration']
                description = row['description']
                
                st.write("### Movie Title: ", title)
                st.write("**Rating:** ", rating)
                st.write("**Duration:** ", duration)
                st.write("**Description:** ", description)
                st.write("---") 

    else:
        uniquecat = movies['listed_in'].unique()
        selectedcat = st.selectbox(
            'Select Category',
            options = uniquecat,
            index=0 )
        filtered_movies = movies[movies['listed_in'] == selectedcat]

        if filtered_movies.empty:
            st.write("No data available for the selected category.")
        else:
            random_items = filtered_movies.sample(n=3)
            for index, row in random_items.iterrows():
                title = row['title']
                rating = row['rating']
                duration = row['duration']
                description = row['description']
                
                st.write("### Movie Title: ", title)
                st.write("**Rating:** ", rating)
                st.write("**Duration:** ", duration)
                st.write("**Description:** ", description)
                st.write("---") 

def rating():
    st.write("Store Your Movie Ratings")

    movie_title = st.text_input("Movie Title")
    rating = st.slider("Rating", min_value=1, max_value=10)
    submit_button = st.button("Submit Rating")

    if submit_button:

        new_rating = pd.DataFrame({
            'title': [movie_title],
            'rating': [rating]
        })

        try:
            new_rating.to_csv('user_ratings.csv', mode='a', header=False, index=False)
            st.success("Rating submitted successfully!")
        except Exception as e:
            st.error(f"Error saving rating: {e}")

    if st.button("Show My Ratings"):
        try:
            ratings_df = pd.read_csv('user_ratings.csv', names=['title', 'rating'])
            st.write(ratings_df)
        except FileNotFoundError:
            st.warning("No ratings found.")


def home():
    st.write("When life gets boring...")
    st.markdown(
    f'<img src="data:image/gif;base64,{gif_data_url}" alt="GIF">',
    unsafe_allow_html=True)
    st.write("")
    st.write("My name is dingo! Ready to help you with your Netflix needs. Click on the sidebar to get started.")


st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', [
                           'Home', 'Recommendation', 'Rating'])

# choosing options :D
if options == 'Home':
    home()
elif options == 'Recommendation':
    recommendation()
elif options == 'Rating':
    rating()
