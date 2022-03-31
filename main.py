import pandas as pd
import numpy as np
pd.set_option("display.max_columns", 50)
pd.set_option("display.max_rows", 50)
pd.set_option("display.width", 1000)

df_hosting = pd.read_excel(
    "/Users/grantglazer/Downloads/National Grid Hosting Capacity Feeder Level Data 3 Phase (MW).xlsx",
    sheet_name="data",
)
df_ev = pd.read_excel(
    "/Users/grantglazer/Downloads/National Grid EV Load Serving Capacity Feeder Level Data 3 Phase.xlsx",
    sheet_name="data",
)

gb_hosting = df_hosting.groupby("Feeder").sum()

print(df_hosting.Feeder.unique)

print(df_hosting.head())
print(df_ev.head())

print(df_hosting.columns)
print(df_ev.columns)


