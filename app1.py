import streamlit as st
import pandas as pd

# ------------------------------
# Custom CSS for colors
# ------------------------------
st.markdown(
    """
    <style>
    /* Background color */
    .stApp {
        background-color: #FFFACD;  /* light yellow */
    }
    /* Title style */
    h1 {
        color: red;
        text-align: center;
    }
    /* All other text in black */
    body, p, h2, h3, h4, h5, h6, .stText, .stMarkdown {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------
# Load dataset
# ------------------------------
try:
    df = pd.read_csv('raw.csv')
except FileNotFoundError:
    st.error("❌ raw.csv not found! Put it in the same folder as app.py")
    st.stop()

# ------------------------------
# App Title
# ------------------------------
st.markdown("<h1>💎 Diamond Price Lookup App</h1>", unsafe_allow_html=True)
st.markdown("---")

# ------------------------------
# 3 columns for user input
# ------------------------------
cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<p>Cut</p>", unsafe_allow_html=True)
    cut = st.selectbox("", cut_categories)

with col2:
    st.markdown("<p>Color</p>", unsafe_allow_html=True)
    color = st.selectbox("", color_categories)

with col3:
    st.markdown("<p>Clarity</p>", unsafe_allow_html=True)
    clarity = st.selectbox("", clarity_categories)

st.markdown("---")

# ------------------------------
# Button to get price
# ------------------------------
if st.button("💰 GET PRICE"):
    filtered_df = df[(df['cut'] == cut) &
                     (df['color'] == color) &
                     (df['clarity'] == clarity)]
    
    if not filtered_df.empty:
        avg_price = filtered_df['price'].mean()
        min_price = filtered_df['price'].min()
        max_price = filtered_df['price'].max()
        
        # Estimated price heading
        st.markdown(f"<h2>Estimated Price: ₹{avg_price:.2f}</h2>", unsafe_allow_html=True)

        st.markdown("---")
        
        st.markdown("Matching Diamonds:")
        st.dataframe(filtered_df[['id','carat','cut','color','clarity','price']])
        
        # Display Min, Avg, Max using markdown with black text
        stat_col1, stat_col2, stat_col3 = st.columns(3)
        stat_col1.markdown(f"<h3>Minimum Price:<br>₹{min_price:.2f}</h3>", unsafe_allow_html=True)
stat_col2.markdown(f"<h3>Average Price:<br>₹{avg_price:.2f}</h3>", unsafe_allow_html=True)
stat_col3.markdown(f"<h3>Maximum Price:<br>₹{max_price:.2f}</h3>", unsafe_allow_html=True)

        
    else:
        st.warning("❌ No diamonds found with this combination.")
