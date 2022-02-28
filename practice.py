import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")

student_df=df.loc[df['student_id']=="TRL_987"]
print(student_df.groupby("level")["attempt"].mean())

fig = px.bar(
student_df , x=['Level 1','Level 2','Level 3','Level 4'],
 y=student_df=df.loc[df['student_id']=="TRL_987"] )
fig.show()