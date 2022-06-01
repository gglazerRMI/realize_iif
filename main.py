import pandas as pd
import numpy as np
import datetime as dt
pd.set_option("display.max_columns", 50)
pd.set_option("display.max_rows", 50)
pd.set_option("display.width", 1000)

hosting=False
if hosting:
    df_hosting = pd.read_excel(
        "/Users/grantglazer/Downloads/National Grid Hosting Capacity Feeder Level Data 3 Phase (MW).xlsx",
        sheet_name="data",
    )
    df_ev = pd.read_excel(
        "/Users/grantglazer/Downloads/National Grid EV Load Serving Capacity Feeder Level Data 3 Phase.xlsx",
        sheet_name="data",
    )

    gb_hosting = df_hosting.groupby("Feeder").sum()

df_re = pd.read_excel(
    "/Users/grantglazer/PycharmProjects/cepm/rmi_data/ResourceProfiles.xlsx",
    sheet_name="Sheet1",
    header=9,
    usecols="B:D"
)



# print(df_hosting.Feeder.unique)
#
# print(df_hosting.head())
# print(df_ev.head())
#
# print(df_hosting.columns)
# print(df_ev.columns)

print(df_re.head)
list = []
for col in ["onshore","offshore"]:
    df_re["datetime"] = pd.to_datetime(df_re["datetime"])
    df_re["Date"] = df_re["datetime"].dt.date
    df_re["Hour"] = df_re["datetime"].dt.hour
    piv = df_re.pivot(index="Date", columns="Hour", values=col)
    print(piv.head)
    list.append(piv)

df_csv = pd.DataFrame()
for df in list:
    df_csv = pd.concat([df_csv, df])

df_csv.to_csv("wind_profs.csv")

