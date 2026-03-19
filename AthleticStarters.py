import streamlit as st
import pandas as pd
import requests

CSV_URL = "https://raw.githubusercontent.com/stretchinnovation/SCMAthleticStarters/AthleticStarters/StartersData.csv"

@st.cache_data(ttl=5)
def load_lines(url):
    response = requests.get(url)
    response.raise_for_status()
    return [line.strip().split(",") for line in response.text.splitlines()]

lines = load_lines(CSV_URL)

header1 = lines[0]
header2 = lines[2]
data1 = [lines[1]]
data2 = lines[3:]

df1 = pd.DataFrame(data1, columns=header1)
df2 = pd.DataFrame(data2, columns=header2)

# --- Build single string from df1 ---
# Specify the order of fields you want
df1.columns = df1.columns.str.strip()

# Allocate each field into its own string variable
round = str(df1.iloc[0]["Round"])
heat = str(df1.iloc[0]["Heat"])
gender = str(df1.iloc[0]["Gender"])
age = int(df1.iloc[0]["Age"])
item = str(df1.iloc[0]["Item"])

if round == "F":
    round = "FINAL"
else: 
    round = "HEAT "+heat

if age in range(24,30):
    age = "SENIOR"
elif age in range(35,40):
    age = "MASTERS 35-39"
elif age in range(45,50):
    age = "MASTERS 45-49"
elif age in range(55,60):
    age = "MASTERS 55-59"
elif age in range(65,70):
    age = "MASTERS 65-69"
elif age in range(75,80):
    age = "MASTERS 75-79"
elif age in range(85,90):
    age = "MASTERS 85-89"
elif age in range(95,100):
    age = "MASTERS 95-99"
elif age > 99:
    age = "MASTERS 99+"
else: 
    age = "U"+str(age)

# Now you can build your head string in any order you like
head = f"{round} {gender} {age} {item}"

# Display the string instead of the DataFrame
#st.subheader("Header Row 1 Data")
#st.write(head)

# Specify which columns you want to show
match item:
    case i if "90m" in i:
        columns_to_show = ["Lane", "Surname", "Firstname", "Number", "Team"]
    case i if "100m" in i:
        columns_to_show = ["Lane", "Surname", "Firstname", "Number", "Team"]
    case i if "110m" in i:
        columns_to_show = ["Lane", "Surname", "Firstname", "Number", "Team"]
    case i if "200m" in i:
        columns_to_show = ["Lane", "Surname", "Firstname", "Number", "Team"]
    case i if "400m" in i:
        columns_to_show = ["Lane", "Surname", "Firstname", "Number", "Team"]
    case i if "800m" in i:
        columns_to_show = ["Lane", "Surname", "Firstname", "Number", "Team"]
    case i if "relay" in i:
        columns_to_show = ["Lane", "Surname", "Firstname", "Number", "Team"]
    case _:
        columns_to_show = ["Surname", "Firstname", "Number", "Team"]


# Load Poppins font globally
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
    <style>
    .stApp {
        background-color: #00ff00;
    }
    </style>
    <style>
    .custom-subheader {
        font-family: 'Poppins', sans-serif;
        font-size: 1.5em;
        font-weight: 800;
        color: #000000 !important;
        #background-color: #00ff00;
        #background-image: linear-gradient(135deg, #EF7C19, #FCCB27) !important;
        background-image: url("app/static/KZNA_StartList_Title_Bar.png") !important;
        background-size: cover;
        background-repeat: no-repeat;
        padding: 6px 0px 10px 30px;
        #width: 100%;
        text-transform: uppercase;
        margin-top: 0em;
        margin-bottom: 0em;
        margin-left: 2px;
        margin-right: 2px;
    }
        <style>
        /* Center the RESULTS div in the page */
        #STARTERS {
            display: flex;
            justify-content: left;   /* horizontal center */
            align-items: top;       /* vertical center */
            flex-direction: column;    /* stack header + table */
            min-height: 100vh;         /* take full viewport height */
        }
        </style>
    
    </style>
    """,
    unsafe_allow_html=True
) 


# Create a Styler with transparent backgrounds
styled = (
    df2[columns_to_show]
    .style
    .hide(axis="index")
    .set_table_styles(
        [
            # Table dimensions
            {"selector": "table", "props": [
                #("width", "100%"),
                ("max-height", "240px"),
                ("margin", "0px"),
                ("padding", "0px 0px"),
                ("border-collapse", "collapse")  # ensure borders collapse
            ]},
            # Header styling 
            {"selector": "th", "props": [
                ("font-family", "Poppins"),
                ("font-weight", "bold"),
                ("color", "#ffffff"),
                ("background-image", "linear-gradient(135deg, #E5007E,#E5007E,#E5007E,#E5007E,#E5007E,#b00466,#7a084f, #101020) !important"),
                ("text-transform", "uppercase"),
                ("margin", "0px"),
                ("padding", "0px 0px"),
                ("border", "none"),
                ("font-size", "18px"),
                ("white-space", "nowrap")  # prevent wrapping in headers
            ]},
            # Cell styling
            {"selector": "td", "props": [
                ("font-family", "Poppins"),
                ("text-transform", "uppercase"),
                ("background-image", "linear-gradient(150deg, #101020,#101020,#101020, #303060) !important"),
                ("margin", "0px"),
                ("padding", "0px 0px"),
                ("font-size", "18px"),
                ("white-space", "nowrap")  # prevent wrapping in headers
            ]},
            # Force fixed widths with !important
            {"selector": "td.col0, th.col0", "props": [
                ("text-align", "center"),
                ("width", "30px !important"),
                ("padding", "0px 30px"),
            ]},
            {"selector": "td.col1, th.col1", "props": [
                ("text-align", "left"),
                ("width", "auto"),
                ("padding", "0px 30px"),
            ]},
            {"selector": "td.col2, th.col2", "props": [
                ("text-align", "left"),
                ("width", "auto"),
                ("padding", "0px 30px"),
            ]},
            {"selector": "td.col3, th.col3", "props": [
                ("text-align", "center"),
                ("text-align", "center"),
                ("width", "40px !important"),
                ("padding", "0px 30px"),
            ]},
            {"selector": "td.col4, th.col4", "props": [
                ("text-align", "center"),
                ("text-align", "center"),
                ("width", "100px !important"),
                ("padding", "0px 30px"),
            ]},
            #{"selector": "td.col5, th.col5", "props": [
            #    ("text-align", "center"),
            #    ("text-align", "center"),
            #    ("width", "100px !important"),
            #    ("padding", "0px 30px"),
            #]},
            # Alignment overrides
            {"selector": "td.col0", "props": [("text-align", "center")]}, # Place
            {"selector": "td.col3", "props": [("text-align", "center")]}, # Number
            {"selector": "td.col4", "props": [("text-align", "center")]}, # Team
            #{"selector": "td.col5", "props": [("text-align", "center")]}, # Performance
        ]
    )
)



# Render styled table and head string inside a RESULTS div
st.html(
    f"""
    <div id="STARTERS">
        <div class="custom-subheader">{head}</div>
        <div>{styled.to_html()}</div>
        
    </div>
    """
)
