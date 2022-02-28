import pandas as pd
import plotly.graph_objects as go
import csv

df=pd.read_csv('data.csv')
student_df=df.loc[df['student_id']=="TRL_987"]
print(student_df.groupby("level")["attempt"].mean())

fig=go.Figure(go.Bar(
    x=['Level 1','Level 2','Level 3','Level 4'],
    y=student_df.groupby("level")["attempt"].mean()
))
fig.show()