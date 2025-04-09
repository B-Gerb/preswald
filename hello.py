from preswald import text, plotly, connect, get_df, table, query, slider


import pandas as pd
import plotly.express as px


text("# Welcome to Preswald!")
text("This is your first app. 🎉")
# Load the CSV
connect() # load in all sources, which by default is the sample_csv
df = get_df('pistachio_csv')


sql = "SELECT * FROM pistachio_csv WHERE AREA > 75000"
filtered_df = query(sql, "pistachio_csv")

text("## Data Overview")
threshold = slider("Threshold", min_val=0, max_val=150000, default=75000)
table(df[df["AREA"] > threshold], title="Dynamic Data View")



fig = px.scatter(df[df["AREA"] > threshold], x="AREA", y="PERIMETER", color="Class")
plotly(fig)

text("## Data Overview")
