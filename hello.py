from preswald import text, plotly, connect, get_df, table, query, slider
import plotly.express as px

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFE
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np

text("# Welcome to Preswald!")
text("This is your first app. 🎉")
# Load the CSV
connect() # load in all sources, which by default is the sample_csv
df = get_df('pistachio_csv')

markdown_content = "## Data Columns\n" + "\n".join([f"- {col}" for col in df.columns])
text(markdown_content)

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


#does not work with seaborn
#sns.pairplot(df, hue="class")

fig3 = px.scatter_matrix(
    df,
    dimensions=df.columns[:-1],  # All columns except 'class'
    color="Class",
    symbol="Class",
    title="Scatter Plot Matrix by Class",
    opacity=0.7
)
fig3.update_layout(
    width=1000,
    height=1000,
    autosize=False
)
plotly(fig3)
features = [
    'AREA', 'PERIMETER', 'MAJOR_AXIS', 'MINOR_AXIS', 'ECCENTRICITY', 
    'EQDIASQ', 'SOLIDITY', 'CONVEX_AREA', 'EXTENT', 'ASPECT_RATIO', 
    'ROUNDNESS', 'COMPACTNESS', 'SHAPEFACTOR_1', 'SHAPEFACTOR_2', 
    'SHAPEFACTOR_3', 'SHAPEFACTOR_4'
]
X = df[features]
y = df['Class']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
svm_linear = SVC(kernel='linear')
svm_linear.fit(X_scaled, y)
importance = np.abs(svm_linear.coef_[0])
indices = np.argsort(importance)[::-1]

importance = np.abs(svm_linear.coef_[0])
indices = np.argsort(importance)[::-1]
feature_importance_df = pd.DataFrame({
    'Feature': [features[i] for i in indices],
    'Importance': importance[indices]
})
fig4 = px.bar(feature_importance_df, x='Feature', y='Importance', title="Feature Importance")
fig4.update_layout(
    xaxis_title="Feature",
    yaxis_title="Importance",
    width=800,
    height=400,
    showlegend=False
)
plotly(fig4)