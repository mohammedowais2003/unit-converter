import streamlit as st

# Apply custom CSS with dark-friendly styles and white input text
st.markdown(
    """
    <style>
    :root {
        --primary: #4361ee;
        --secondary: #3f37c9;
        --accent: #4895ef;
        --light: #f8f9fa;
        --dark: #212529;
        --text: white;
        --label: white;
    }

    .stApp {
        background: linear-gradient(135deg, #2c2f33 0%, #1e2124 100%);
        min-height: 100vh;
        color: white !important;
    }

    .main-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem;
        background: #343a40;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        margin-top: 2rem;
        margin-bottom: 2rem;
    }

    h1 {
        text-align: center;
        color: white !important;
        font-size: 2.5rem;
        margin-bottom: 1.5rem;
        font-weight: 700;
    }

    .description {
        text-align: center;
        color: white !important;
        margin-bottom: 2rem;
        font-size: 1.1rem;
    }

    label {
        color: white !important;
        font-weight: 500 !important;
    }

    .stSelectbox div[data-baseweb="select"] {
        border-radius: 12px !important;
        border: 2px solid var(--accent) !important;
        background-color: #212529 !important;
    }

    .stSelectbox div[data-baseweb="select"] div {
        color: white !important;
    }

    .stSelectbox ul[role="listbox"] li {
        color: white !important;
        background-color: #343a40 !important;
    }

    [data-baseweb="popover"] {
        background-color: #343a40 !important;
    }

    .stNumberInput input {
        border-radius: 12px !important;
        border: 2px solid var(--accent) !important;
        font-size: 1rem !important;
        padding: 0.75rem 1rem !important;
        color: white !important;
        background-color: #212529 !important;
    }

    .stButton>button {
        border-radius: 12px !important;
        background: linear-gradient(45deg, var(--primary), var(--secondary)) !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 0.75rem 1.5rem !important;
        border: none !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
        width: 100% !important;
    }

    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15) !important;
        background: linear-gradient(45deg, var(--secondary), var(--primary)) !important;
    }

    .result-box {
        font-size: 1.25rem;
        font-weight: 600;
        text-align: center;
        background: linear-gradient(135deg, #2c2f33 0%, #1e2124 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white !important;
        margin-top: 2rem;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        border-left: 5px solid var(--primary);
    }

    .footer {
        text-align: center;
        margin-top: 3rem;
        font-size: 0.9rem;
        color: white !important;
        opacity: 0.7;
    }

    .conversion-card {
        background: #212529;
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .category-selector {
        background: #343a40 !important;
        border-radius: 15px !important;
        padding: 1rem !important;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05) !important;
    }

    .stSidebar .sidebar-content {
        background: linear-gradient(135deg, #2c2f33 0%, #1e2124 100%) !important;
        color: white !important;
    }

    p, div, span, h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }

    @media (max-width: 768px) {
        .main-container {
            padding: 1rem;
            border-radius: 0;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main container
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# Title and description
st.markdown("<h1>🔢 Advanced Unit Converter</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='description'>Convert between different units of measurement with precision and ease. Select a category and enter your values below.</p>", 
    unsafe_allow_html=True
)

# Sidebar menu with icon
with st.sidebar:
    st.markdown("## ⚙️ Conversion Settings")
    conversion_type = st.selectbox(
        "Select Category", 
        ["Length", "Weight", "Temperature", "Area", "Volume", "Speed"],
        key="conversion_type"
    )

# Input section
st.markdown("<div class='conversion-card'>", unsafe_allow_html=True)
value = st.number_input(
    "Enter Value to Convert", 
    min_value=0.0, 
    format="%.6f",
    key="input_value"
)

# Layout for the conversion
col1, col2 = st.columns(2)

# Unit selection based on category
if conversion_type == "Length":
    units = ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile"]
    with col1:
        from_unit = st.selectbox("From Unit", units, index=2, key="from_length")
    with col2:
        to_unit = st.selectbox("To Unit", units, index=3, key="to_length")

elif conversion_type == "Weight":
    units = ["milligram", "gram", "kilogram", "pound", "ounce", "ton"]
    with col1:
        from_unit = st.selectbox("From Unit", units, index=2, key="from_weight")
    with col2:
        to_unit = st.selectbox("To Unit", units, index=3, key="to_weight")

elif conversion_type == "Temperature":
    units = ["celsius", "fahrenheit", "kelvin"]
    with col1:
        from_unit = st.selectbox("From Unit", units, index=0, key="from_temp")
    with col2:
        to_unit = st.selectbox("To Unit", units, index=1, key="to_temp")

elif conversion_type == "Area":
    units = ["square millimeter", "square centimeter", "square meter", "square kilometer", 
             "square inch", "square foot", "square yard", "acre", "hectare"]
    with col1:
        from_unit = st.selectbox("From Unit", units, index=2, key="from_area")
    with col2:
        to_unit = st.selectbox("To Unit", units, index=3, key="to_area")

elif conversion_type == "Volume":
    units = ["milliliter", "liter", "cubic meter", "cubic centimeter", "cubic inch", 
             "cubic foot", "gallon", "quart", "pint", "fluid ounce"]
    with col1:
        from_unit = st.selectbox("From Unit", units, index=1, key="from_volume")
    with col2:
        to_unit = st.selectbox("To Unit", units, index=0, key="to_volume")

elif conversion_type == "Speed":
    units = ["meters per second", "kilometers per hour", "miles per hour", "knot", "feet per second"]
    with col1:
        from_unit = st.selectbox("From Unit", units, index=1, key="from_speed")
    with col2:
        to_unit = st.selectbox("To Unit", units, index=2, key="to_speed")

st.markdown("</div>", unsafe_allow_html=True)  # Close conversion-card

# Conversion functions
def length_converter(value, from_unit, to_unit):
    factors = {
        "millimeter": 0.001,
        "centimeter": 0.01,
        "meter": 1.0,
        "kilometer": 1000.0,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.344
    }
    return value * factors[from_unit] / factors[to_unit]

def weight_converter(value, from_unit, to_unit):
    factors = {
        "milligram": 0.000001,
        "gram": 0.001,
        "kilogram": 1.0,
        "pound": 0.453592,
        "ounce": 0.0283495,
        "ton": 1000.0
    }
    return value * factors[from_unit] / factors[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value

def area_converter(value, from_unit, to_unit):
    factors = {
        "square millimeter": 0.000001,
        "square centimeter": 0.0001,
        "square meter": 1.0,
        "square kilometer": 1000000.0,
        "square inch": 0.00064516,
        "square foot": 0.092903,
        "square yard": 0.836127,
        "acre": 4046.86,
        "hectare": 10000.0
    }
    return value * factors[from_unit] / factors[to_unit]

def volume_converter(value, from_unit, to_unit):
    factors = {
        "milliliter": 0.001,
        "liter": 1.0,
        "cubic meter": 1000.0,
        "cubic centimeter": 0.001,
        "cubic inch": 0.0163871,
        "cubic foot": 28.3168,
        "gallon": 3.78541,
        "quart": 0.946353,
        "pint": 0.473176,
        "fluid ounce": 0.0295735
    }
    return value * factors[from_unit] / factors[to_unit]

def speed_converter(value, from_unit, to_unit):
    factors = {
        "meters per second": 1.0,
        "kilometers per hour": 0.277778,
        "miles per hour": 0.44704,
        "knot": 0.514444,
        "feet per second": 0.3048
    }
    return value * factors[from_unit] / factors[to_unit]

# Convert and Reset buttons
col_convert, col_reset = st.columns(2)
with col_convert:
    convert_btn = st.button("🚀 Convert", key="convert")
with col_reset:
    reset_btn = st.button("🔄 Reset", key="reset")

# Perform conversion
if convert_btn:
    if from_unit == to_unit:
        result = value
    else:
        try:
            if conversion_type == "Length":
                result = length_converter(value, from_unit, to_unit)
            elif conversion_type == "Weight":
                result = weight_converter(value, from_unit, to_unit)
            elif conversion_type == "Temperature":
                result = temperature_converter(value, from_unit, to_unit)
            elif conversion_type == "Area":
                result = area_converter(value, from_unit, to_unit)
            elif conversion_type == "Volume":
                result = volume_converter(value, from_unit, to_unit)
            elif conversion_type == "Speed":
                result = speed_converter(value, from_unit, to_unit)

            st.markdown(
                f"<div class='result-box'>"
                f"<div style='font-size: 1.1rem; margin-bottom: 0.5rem;'>Conversion Result</div>"
                f"<div style='font-size: 1.5rem;'>{value:.6g} {from_unit} = {result:.6g} {to_unit}</div>"
                f"</div>", 
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"An error occurred during conversion: {str(e)}")

# Reset functionality
if reset_btn:
    st.cache_data.clear()
    st.rerun()

# Footer
st.markdown(
    "<div class='footer'>"
    "© 2023 Advanced Unit Converter | Made with Streamlit"
    "</div>", 
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)  # Close main-container
