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
threshold = slider("Threshold For Area", min_val=0, max_val=150000, default=75000)
table(df[df["AREA"] > threshold], title="Dynamic Data View")


thershold_area_df = df[df["AREA"] > threshold]

fig1 = px.scatter(thershold_area_df, x="AREA", y="PERIMETER", color="Class")
plotly(fig1)

threshold1 = slider("Threshold For ECCENTRICITY", min_val=0, max_val=100, default=50)
threshold1 /= 100 # Convert to a percentage
threshold_eccentricity_df = thershold_area_df[thershold_area_df["ECCENTRICITY"] > threshold1]
fig2 = px.histogram(threshold_eccentricity_df, x="ECCENTRICITY", color="Class", barmode="group")
plotly(fig2)

