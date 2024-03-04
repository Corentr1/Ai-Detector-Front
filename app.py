import os
import streamlit as st
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg




# Define the base URI of the API
#   - Potential sources are in `.streamlit/secrets.toml` or in the Secrets section
#     on Streamlit Cloud
#   - The source selected is based on the shell variable passend when launching streamlit
#     (shortcuts are included in Makefile). By default it takes the cloud API url
if 'API_URI' in os.environ:
    BASE_URI = st.secrets[os.environ.get('API_URI')]
else:
    BASE_URI = st.secrets['cloud_api_uri']
# Add a '/' at the end if it's not there
BASE_URI = BASE_URI if BASE_URI.endswith('/') else BASE_URI + '/'
# Define the url to be used by requests.get to get a prediction (adapt if needed)
url = BASE_URI + 'predict'

# Just displaying the source for the API. Remove this in your final version.
#st.markdown(f"Working with {url}")

# TODO: Add some titles, introduction, ...

st.image('media/logo.png')
#st.markdown("<h1 style='text-align: center;'>AI Detector</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>Uncover the Origins of Your Images with Cutting-Edge AI Technology</h2>", unsafe_allow_html=True)
st.markdown("</p>", unsafe_allow_html=True)
st.markdown("""Step into the world of AI Detector – your ultimate solution for \
            unraveling the mysteries behind images. Leveraging state-of-the-art \
            artificial intelligence, our app distinguishes between images generated \
            by AI algorithms and those crafted by human hands. Simply upload an image, \
            and let our intelligent algorithms dissect its nuances. Gain profound \
            insights into the authenticity of your visuals with unmatched accuracy. \
            Embark on a journey into the future of image verification with AI Detector!""")

# TODO: Request user input
st.markdown("</p>", unsafe_allow_html=True)
st.markdown("</p>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Upload your picture</h3>", unsafe_allow_html=True)

st.set_option('deprecation.showfileUploaderEncoding', False)
uploaded_file = st.file_uploader("Upload an image", type=['png', 'jpg'])


if uploaded_file is not None:
    data = mpimg.imread(uploaded_file)
    st.image(data)


# TODO: Call the API using the user's input

params = {

}

def fetch_aidetector(params):
    """
    Get lyrics from Seeds Lyrics API. Returns empty string if song not found
    """
    response = requests.get(url=url, params = params).json()
    return round(response["fare"],2)

#   - url is already defined above
#   - create a params dict based on the user's input
#   - finally call your API using the requests package

# if st.button("Is it fake?"):
#     response = fetch_aidetector(params)
#     st.write(f"Your image is {response}$")

# TODO: retrieve the results
#   - add a little check if you got an ok response (status code 200) or something else
#   - retrieve the prediction from the JSON


# TODO: display the prediction in some fancy way to the user


# TODO: [OPTIONAL] maybe you can add some other pages?
#   - some statistical data you collected in graphs
#   - description of your product
#   - a 'Who are we?'-page
