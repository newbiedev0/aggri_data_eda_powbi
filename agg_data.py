# %%
import pandas as pd

# %%
df = pd.read_csv('C:/Users/venka/Downloads/agg_data.csv')

# %%
df

# %%
df.info()

# %%
df.describe()

# %%
df.isnull().sum()

# %%
df.dtypes

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# %%
df['Year'].unique()

# %%
top_7_states_rice_production = df.groupby('State Name')['RICE PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(7)

# %%
top_7_states_rice_production.plot(kind='bar', color='green')
plt.title('Top 7 States by Rice Production')
plt.xlabel('State')    
plt.ylabel('Rice Production in 1000 tons')
plt.show()

# %%
top_5_states_wheat_production = df.groupby('State Name')['WHEAT PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(5)

# %%
top_5_states_wheat_production.plot(kind='bar', color='yellow')
plt.title('Top 5 States by Wheat Production')
plt.xlabel('State')    
plt.ylabel('Wheat Production in 1000 tons')
plt.show()

# %%
top_5_states_wheat_production.plot(kind='pie', autopct='%1.1f%%', startangle=150, shadow=True)
plt.title('Top 5 States by Wheat Production')
plt.ylabel('') 
plt.show()

# %%
top_5_states_OILSEEDS_production = df.groupby('State Name')['OILSEEDS PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(5)

# %%
px.pie(top_5_states_OILSEEDS_production, values=top_5_states_OILSEEDS_production, names=top_5_states_OILSEEDS_production.index) 

# %%
top_7_states_SUNFLOWER_production = df.groupby('State Name')['SUNFLOWER PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(7)

# %%
top_7_states_SUNFLOWER_production.plot(kind='bar', color='orange')
plt.title('Top 7 States by Sunflower Production')
plt.xlabel('State')    
plt.ylabel('Sunflower Production in 1000 tons')
plt.show()      

# %%
fig = px.scatter_3d(df, x='Year', y='RICE PRODUCTION (1000 tons)', z='WHEAT PRODUCTION (1000 tons)', color='State Name', title='3D Scatter Plot of Rice and Wheat Production Over Years by State')
fig.show()

# %%
px.pie(top_7_states_SUNFLOWER_production, values=top_7_states_SUNFLOWER_production, names=top_7_states_SUNFLOWER_production.index)

# %%
india_sugarcane_production_last50_years = df.groupby('Year')['SUGARCANE PRODUCTION (1000 tons)'].sum()

# %%
india_sugarcane_production_last50_years.plot(kind='line', marker='o', color='brown')
plt.title('India Sugarcane Production Over the Last 50 Years')
plt.xlabel('Year')    
plt.ylabel('Sugarcane Production in 1000 tons')
plt.show()

# %%
rice_vs_wheat_production_india = df.groupby('Year')[['RICE PRODUCTION (1000 tons)', 'WHEAT PRODUCTION (1000 tons)']].sum()
rice_vs_wheat_production_india.plot(kind='line', marker='o')
plt.title('Rice vs Wheat Production in India Over Years')
plt.xlabel('Year')    
plt.ylabel('Production in 1000 tons')
plt.show()

# %%
px.line(rice_vs_wheat_production_india, x=rice_vs_wheat_production_india.index, y=['RICE PRODUCTION (1000 tons)', 'WHEAT PRODUCTION (1000 tons)'], title='Rice vs Wheat Production in India Over Years')

# %%
df['State Name'].unique().tolist()

# %%
west_bengal_df = df[df['State Name'] == 'West Bengal']
rice_production_westbengal_districts = west_bengal_df.groupby('Dist Name')['RICE PRODUCTION (1000 tons)'].sum().sort_values(ascending=False)
 
  


# %%
rice_production_westbengal_districts.plot(kind='bar', color='skyblue')
plt.title('Rice Production by Districts in West Bengal')            
plt.xlabel('District')                                          
plt.ylabel('Rice Production in 1000 tons')
plt.show()

# %%
wheat_prod_up=df[df['State Name']=='Uttar Pradesh'].groupby('Year')['WHEAT PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(10)


# %%
wheat_prod_up.plot(kind='bar', color='purple')
plt.title('Top 10 Years of Wheat Production in Uttar Pradesh')
plt.xlabel('Year')                  
plt.ylabel('Wheat Production in 1000 tons')
plt.show()

# %%
Finger_millet_production_last50years = df.groupby('Year')['FINGER MILLET PRODUCTION (1000 tons)'].sum()
Finger_millet_production_last50years.plot(kind='line', marker='o', color='lightgreen')
plt.title('India Finger Millet Production Over the Last 50 Years')
plt.xlabel('Year')    
plt.ylabel('Finger Millet Production in 1000 tons')
plt.show()

# %%
pearl_millet_production_last50years = df.groupby('Year')['PEARL MILLET PRODUCTION (1000 tons)'].sum()
pearl_millet_production_last50years.plot(kind='line', marker='o', color='indigo')
plt.title('India Pearl Millet Production Over the Last 50 Years')
plt.xlabel('Year')    
plt.ylabel('Pearl Millet Production in 1000 tons')
plt.show()

# %%
kharif_sorghum_prod_india = df.groupby('Year')['KHARIF SORGHUM PRODUCTION (1000 tons)'].sum().sort_values(ascending=False)
px.bar(x=kharif_sorghum_prod_india.index, y=kharif_sorghum_prod_india.values, labels={'x': 'Year', 'y': 'KHARIF SORGHUM PRODUCTION (1000 tons)'}, title='Kharif Sorghum Production in India Over Years')

# %%
rabi_sorghum_prod_india = df.groupby('Year')['RABI SORGHUM PRODUCTION (1000 tons)'].sum().sort_values(ascending=False)
px.bar(x=rabi_sorghum_prod_india.index, y=rabi_sorghum_prod_india.values, labels={'x': 'Year', 'y': 'RABI SORGHUM PRODUCTION (1000 tons)'}, title='Rabi Sorghum Production in India Over Years')

# %%
top_7_states_groundnut_production = df.groupby('State Name')['GROUNDNUT PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(7)
px.pie(top_7_states_groundnut_production, values=top_7_states_groundnut_production, names=top_7_states_groundnut_production.index, title='Top 7 States by Groundnut Production')

# %%
soyabean_production = df.groupby('State Name')['SOYABEAN PRODUCTION (1000 tons)'].mean().sort_values(ascending=False).head(5)

# %%
soyabean_production.plot(kind='bar', color='green')
plt.title('Top 5 States by Soyabean Production')
plt.xlabel('State')    
plt.ylabel('Soyabean Production in 1000 tons')
plt.show()

# %%
production_col = 'SOYABEAN PRODUCTION (1000 tons)'
area_col = 'SOYABEAN AREA (1000 ha)'
state_col = 'State Name'

top_5_production = df.groupby(state_col)[production_col].sum().sort_values(ascending=False).head(5).index

top_5_states_df = df[df[state_col].isin(top_5_production)]

grouped_data = top_5_states_df.groupby(state_col).agg(
    total_production=(production_col, 'sum'),
    total_area=(area_col, 'sum')
).reset_index()

grouped_data['Calculated Yield (Kg per ha)'] = (grouped_data['total_production'] * 1000) / grouped_data['total_area']

print(grouped_data[[state_col, 'Calculated Yield (Kg per ha)']])

# %%
grouped_data.plot(kind='bar', x=state_col, y='Calculated Yield (Kg per ha)', color='teal')
plt.title('Calculated Yield of Soyabean for Top 5 States')
plt.xlabel('State')    
plt.ylabel('Calculated Yield (Kg per ha)')
plt.show()

# %%
oilseed_porduction_majorstates = df.groupby('State Name')['OILSEEDS PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(5)
oilseed_porduction_majorstates.plot(kind='bar', color='lightyellow')      
plt.title('Top 5 States by Oilseed Production')          
plt.xlabel('State')    
plt.ylabel('Oilseed Production in 1000 tons')            
plt.show()

# %%
impact_of_area_on_prod_rice= df.groupby('Year')[['RICE PRODUCTION (1000 tons)', 'RICE AREA (1000 ha)']].sum()
impact_of_area_on_prod_rice.plot(kind='line', marker='o')
plt.title('Impact of Area on Rice Production Over Years')
plt.xlabel('Year')    
plt.ylabel('Production in 1000 tons')
plt.show()


# %%
impact_of_area_on_prod_maize= df.groupby('Year')[['MAIZE PRODUCTION (1000 tons)', 'MAIZE AREA (1000 ha)']].sum()
impact_of_area_on_prod_maize.plot(kind='line', marker='o', color='goldenrod')
plt.title('Impact of Area on Maize Production Over Years')            
plt.xlabel('Year')            
plt.ylabel('Production in 1000 tons')            
plt.show()

# %%
impact_of_area_on_prod_wheat= df.groupby('Year')[['WHEAT PRODUCTION (1000 tons)', 'WHEAT AREA (1000 ha)']].sum()
impact_of_area_on_prod_wheat.plot(kind='line', marker='o', color='sienna')
plt.title('Impact of Area on Wheat Production Over Years')            
plt.xlabel('Year')
plt.ylabel('Production in 1000 tons')            
plt.show()

# %%
rice_vs_wheat_yield_states = df.groupby('State Name')[['RICE YIELD (Kg per ha)', 'WHEAT YIELD (Kg per ha)']].sum()
rice_vs_wheat_yield_states.plot(kind='line', marker='o')
plt.title('Rice vs Wheat Yield Over States')
plt.xlabel('State Name')
plt.ylabel('Yield (Kg/hector)')
plt.show()


