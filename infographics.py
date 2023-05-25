import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.gridspec as gridspec

# load data
df = pd.read_csv('brics2.csv')

# Create the dashboard-infographics visualization using gridspec for layout
fig = plt.figure(figsize=(14, 18))
fig.suptitle("INFOGRAPHIC ON GDP, CO2 EMMISIONS AND POPULATION OVER TIME ")

# Add name to infographic with a space between the title and name
fig.text(0.5, 0.94, "Created by :: jackson wambugu ::", wrap=True, horizontalalignment='center', fontsize=14)

gs = gridspec.GridSpec(nrows=5, ncols=2, figure=fig)

# plot 1: line plot of CO2 emissions over time
ax1 = fig.add_subplot(gs[0,0])
sns.lineplot(x='year', y='CO2 emissions', hue='Country', data=df, ax=ax1)
ax1.set_xlabel('Year')
ax1.set_ylabel('CO2 Emissions (metric tons per capita)')
ax1.set_title('CO2 Emissions by Country',color="green")

# plot 2: line plot of GDP over time
ax2 = fig.add_subplot(gs[0,1])
sns.lineplot(x='year', y='GDP', hue='Country', data=df, ax=ax2)
ax2.set_xlabel('Year')
ax2.set_ylabel('GDP (current US$)')
ax2.set_title('GDP over time',color="green")

# plot 3: bar plot of population by country
ax3 = fig.add_subplot(gs[1, 0])
sns.barplot(x='Country', y='Population', data=df, ax=ax3)
ax3.set_xlabel('Country')
ax3.set_ylabel('Population')
ax3.set_title('Population by Country',color="green")


# Plot 4: Emissions vs gdp
ax4 = fig.add_subplot(gs[1,1])
sns.scatterplot(x='CO2 emissions', y='GDP', data=df, ax=ax4)
ax4.set_title('Emissions vs GDP',color="green")
ax4.set_xlabel('CO2 emissions (kt)')
ax4.set_ylabel('GDP (current US$)')

# plot 5: box plot of GDP per capita
ax5 = fig.add_subplot(gs[2, 0])
sns.boxplot(x='Country', y='GDP', data=df, ax=ax5)
ax5.set_xlabel('Country')
ax5.set_ylabel('GDP per capita (current US$)')
ax5.set_title('GDP per Capita by Country',color="green")

# plot 5: box plot of Co2 Emission
ax6 = fig.add_subplot(gs[3, 0])
sns.boxplot(x='Country', y='CO2 emissions', data=df, ax=ax6)
ax6.set_xlabel('Country')
ax6.set_ylabel('CO2 emissions (kt)')
ax6.set_title('Co2 Emission by country',color="green")

# Pivot the DataFrame to create a new DataFrame with columns for each year
df_pivot = df.pivot(index='Country', columns='year', values='CO2 emissions')

# Reset the index of the new DataFrame
df_pivot = df_pivot.reset_index()

# Melt the new DataFrame to create a long-form DataFrame
df_melted = pd.melt(df_pivot, id_vars='Country', var_name='year', value_name='CO2 emissions')

ax7=fig.add_subplot(gs[2,1])
# Create the bar graph using seaborn
sns.barplot(data=df_melted, x='Country', y='CO2 emissions',ax=ax7)

# Set the title and labels of the plot
ax7.set_title('CO2 Emissions by Country and Year')
ax7.set_xlabel('Country')
ax7.set_ylabel('CO2 Emissions (in millions of metric tons)')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# add overall and individual plot explanations in a textbox
textstr = '\n'.join((
    'This infographic shows data on CO2 emissions, GDP per capita, and population for various countries.',
    '',
    'Plot 1: Line plot of CO2 emissions over time, showing how emissions have changed over the years for each country.','',
    'Plot 2: Box plot of GDP per capita, showing the distribution of GDP per capita for each country.','',
    'Plot 3: Bar plot of population, showing the total population for each country.','',
    'Plot 4: Scatter plot  of CO2 emissions vs. GDP per capita.','',
    'Plot 5 : Horizontal bar plot of CO2 emissions by country'))
fig.tight_layout(rect=[0, 0.03, 1, 0.95])
fig.text(0.5, 0.01, textstr, wrap=True, horizontalalignment='center', fontsize=14)

# Show the visualization
plt.show()

plt.savefig('yourstudentid.png',dpi=300)