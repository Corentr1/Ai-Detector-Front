import os
import streamlit as st
import requests
import time
from PIL import Image




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
st.markdown("<h3 style='text-align: center; color: #E73D53;'>Upload your picture</h3>", unsafe_allow_html=True)

st.set_option('deprecation.showfileUploaderEncoding', False)
img_file_buffer = st.file_uploader("Upload an image", type=['png', 'jpg'])


if img_file_buffer is not None:
    ### Display the image user uploaded
    st.image(Image.open(img_file_buffer))

    ### Get bytes from the file buffer
    img_bytes = img_file_buffer.getvalue()

    ### Make request to  API
    #res = requests.post(url + "/upload_image", files={'img': img_bytes})

    ### Animation
    trigger=False
    col1, col2, col3 , col4, col5 = st.columns(5)
    with col1: pass
    with col2: pass
    with col4: pass
    with col5: pass
    with col3 :
        if st.button("Is it fake?"):
            #response = fetch_aidetector(params)
            with st.spinner('Wait for it...'):
                time.sleep(1)
                st.toast('Extracting elements from picture')
                time.sleep(1.5)
                st.toast('Searching for the info on Kitt Le Wagon')
                time.sleep(1.5)
                st.toast('Raised a ticket with Jules van Rie ')
                time.sleep(1.5)
                st.toast('Checking Stackoverflow to make sure')
                time.sleep(1.5)
                st.toast('git status, add, commit "test"')
                time.sleep(2)
                st.toast('Hooray! We found something', icon='🎉')
            trigger = True

    if trigger:
        st.markdown("<h3 style='text-align: center; color: #E73D53;'>Definitely not AI bwahhh!!!</h3>", unsafe_allow_html=True)
        st.progress(0.64, text=f"Your accuracy is around {0.64*100}%")

        # TO UNCOMMENT WHEN API READY
        # if res.status_code == 200:
        #     accuracy = res["accuracy"]
        #     if res["is_ai?"]=0:
        #         st.markdown("<h3 style='text-align: center; color: #E73D53;'>Definitely not AI bwahhh!!!</h3>", unsafe_allow_html=True)
        #         st.progress(accuracy, text=f"Your accuracy is around {accuracy*100}%")
        #     else:
        #         st.markdown("<h3 style='text-align: center; color: #E73D53;'>Definitely AI bwahhh!!!</h3>", unsafe_allow_html=True)
        #         st.progress(accuracy, text=f"Your accuracy is around {accuracy*100}%")
        # else:
        #     st.markdown("<h3 style='text-align: center; color: #E73D53;'>Oops, something went wrong 😓 Please try again.</h3>", unsafe_allow_html=True)
        #     print(res.status_code, res.content)

    # TODO: [OPTIONAL] maybe you can add some other pages?
    #   - some statistical data you collected in graphs
    #   - description of your product
    #   - a 'Who are we?'-page
