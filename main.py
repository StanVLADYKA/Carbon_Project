import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

""" 
Analysis of the level of carbon dioxide depending on:
- fossil fuel extraction
- human population
- global temperature Earth
- global meat production
- sun activity
- mining Bitcoin
-------------------------------

data csv sources:

carbon dioxide:           https://www.co2.earth/co2-datasets   
human population:         https://data.worldbank.org/indicator/SP.POP.TOTL?end=2021&start=1960
global temperature Earth: https://climate.nasa.gov/vital-signs/global-temperature/
fossil fuel extraction    https://ourworldindata.org/fossil-fuels
global meat production    https://ourworldindata.org/meat-production
sun activity              https://www.kaggle.com/datasets/robervalt/sunspots
maning Bitcoin            https://ccaf.io/cbeci/index

 """

# read CSV
# CO2
df = pd.read_csv("co2_mm_mlo.csv")
df.info()
print(df.head(4))

# fossil fuel
df_1 = pd.read_csv("global-fossil-fuel-consumption.csv")
df_1 = df_1.loc[df_1["Year"] > 1958]
df_1.info()
print(df_1.head(4))

# population
df_2 = pd.read_csv("population-and-demography.csv")
df_2 = df_2.loc[df_2["Year"] >= 1958]

# temperature
df_3 = pd.read_csv("temp.csv")
df_3.info()
print(df_3.head(4))
df_3 = df_3.loc[df_3["Year"] > 1958]

# meat
df_4 = pd.read_csv("global-meat-production.csv")
df_4.info()
print(df_4.head(4))
df_4 = df_4.loc[df_4["Entity"] == "World"]
print(df_4.head(9))

# sun
df_5 = pd.read_csv("Sunspots.csv")
df_5 = df_5.loc[df_5["Date"] > "1958"]
df_5.info()
print(df_5.head(4))

# mining bitcoin
df_6 = pd.read_csv("bit_export_2.csv", sep=',')

# create PDF file
pdf = PdfPages("total_carbon.pdf")
# filetypes = {'pdf': 'Album Document Format'}

# Carbon and Global temperature

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(17, 11))

df.plot(x="Year", y="average", ax=axes[0], ylim=(310, 445), title="Carbon Level", color="red",
        linewidth=1.3, xlabel="", ylabel="Level CO2, ppm", label="CO2")

df_3.plot(x="Year", y="Lowess(5)", ax=axes[1], ylim=(-0.1, 1.13), title="Temperature", xlabel="",
          ylabel='Global Land-Ocean Temp. Index,°C',
          label="°C")

pdf.savefig()
plt.show()
plt.close()

# Carbon and Fossil fuel
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(17, 11))

df.plot(x="Year", y="average", ax=axes[0], ylim=(310, 445), title="Carbon Level", color="red",
        linewidth=1.3, xlabel="", ylabel="Level CO2, ppm", label="CO2")
df_1.plot(x="Year", y=["Oil (TWh, direct energy)", "Gas (TWh, direct energy)", "Coal (TWh, direct energy)"],
          title="Global fossil fuel consumptionax", ax=axes[1], ylabel="global-fossil-fuel-consumption", xlabel="")

pdf.savefig()
plt.show()
plt.close()

# Carbon and meat prod
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(17, 11))
df_m = df.loc[df["Year"] >= 1961]
df_m.plot(x="Year", y="average", ax=axes[0], ylim=(310, 445), title="Carbon Level", color="red",
          linewidth=1.3, xlabel="", ylabel="Level CO2, ppm", label="CO2")

df_4.plot(x="Year", y="Meat, total | 00001765 || Production | 005510 || tonnes", title="Global meat production",
          ax=axes[1], ylabel="Global meat production,tonnes 10⁸", xlabel="", label="Meat production")

pdf.savefig()
plt.show()
plt.close()

# Carbon and Sun activity

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(17, 10))
df_s = df.loc[df["Year"] <= 2018]
df_s.plot(x="Year", y="average", ax=axes[0], ylim=(310, 430), title="Carbon Level", color="red",
          linewidth=1.3, xlabel="", ylabel="Level CO2, ppm", label="CO2")

df_5.plot(x="Date", y="Monthly Mean Total Sunspot Number", linewidth=2.3, color="orange",
          title="Mean Total Sunspot Number",
          ax=axes[1], ylabel="Sunspots", xlabel="", label="Sunspots")

pdf.savefig()
plt.show()
plt.close()

# Carbon and population
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(17, 11))

df.plot(x="Year", y="average", ax=axes[0], ylim=(310, 445), title="Carbon Level", color="red",
        linewidth=1.3, xlabel="", ylabel="Level CO2, ppm", label="CO2")
df_2.plot(x="Year", y="Population", title="People on Earth",
          ax=axes[1], ylabel="Population, billion", xlabel="", label="Population", ylim=(2600000000, 8500000000))

pdf.savefig()
plt.show()
plt.close()

# maning bitcoin

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(11, 9))

df_b = df.loc[df["Year"] >= 2010]
df_b.plot(x="Year", y="deseasonalized", ax=axes[0], ylim=(385, 425), color="red",
          linewidth=1.9, xlabel="", ylabel="CO2", label="CO2", marker='h', title="Carbon Level   /   Mining Bitcoin / "
                                                                                 " Temperature   (2010 - 2022)")

df_6.plot(x="Month", y="Monthly consumption TWh",
          ax=axes[1], ylabel="Mining Bitcoin", xlabel="", label="Mining Bitcoin, TWh")

df_3b = df_3.loc[df_3["Year"] >= 2010]
df_3b.plot(x="Year", y="Lowess(5)", ax=axes[2], ylim=(0.6, 1.11), xlabel="", ylabel='Temp. Index,°C',
           label="°C")

pdf.savefig()
plt.show()
plt.close()

pdf.close()