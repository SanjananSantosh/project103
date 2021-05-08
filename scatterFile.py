import pandas as pd
import plotly.express as px

df = pd.read_csv("coviddata.csv")
fig = px.scatter(df, x="date", y="case",
	          size="Percentage",color="Country",
                   size_max=60)
fig.show()
