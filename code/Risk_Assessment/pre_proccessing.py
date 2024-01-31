import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sleep_Dict_Generator import sleep_time_mapping

#Seed that adds determinism to sampling
RANDOM_SEED = 326


#Data Integration

file_path1 = 'NYSDOH_BRFSS_SurveyData_2010.sas7bdat'  #2010
file_path2 = 'NYSDOH_BRFSS_SurveyData_2012.sas7bdat'  #2012
file_path3 = 'NYSDOH_BRFSS_SurveyData_2013.sas7bdat'  #2013
file_path4 = 'nysdoh_brfss_surveydata_2014.sas7bdat'  #2014
file_path5 = 'NYSDOH_BRFSS_SurveyData_2015.sas7bdat'  #2015


df1 = pd.read_sas(file_path1)
df2 = pd.read_sas(file_path2)
df3 = pd.read_sas(file_path3)
df4 = pd.read_sas(file_path4)
df5 = pd.read_sas(file_path5)


# Concatenate datasets together
df = pd.concat([df1, df2, df3, df4, df5 ], ignore_index=True)


#Data decodeing

diabetes_mapping = {1: 'Diabetes', 2: 'Diabetes', 3: 'Dropable', 4: 'Pre-diabetes', 7: 'Unknown', 9: 'Unkown', '.': 'Unknown', '.D': 'Unknown', '.R': 'Unknown'}                                                                                                                                                                           

age_mapping = {1: "18-29", 2: "18-29", 3: "30-39", 4: "30-39", 
               5: "40-49", 6: "40-49", 7: "50-59", 8: "50-59", 
               9: "60-69", 10: "60-69", 11: "70-79", 12: '70-79',
                13: '80+','.D': 'Unknown', '.R': 'Unknown', 14: 'Unknown' }

smoking_mapping = {
    '.': 'Unknown','.D': 'Unknown','.R': 'Unknown', 9: 'Unknown',
    1: 'smokes_every_day',2: 'smokes_some_days',
    3: 'Former_smoker',4: 'Never_smoked',
}

drinking_mapping = {
    '.': 'Dropable', 1: 'Dropable',
    '.D': 'Unknwon', '.R': 'Unknown', 9: 'Unkown',
    2: 'Heavy_Drinker',
}

generic_mapping = {
    '.': 'Unknown',
    '.D': 'Unknown',
    '.R': 'Unknown',
    1: 'Yes',
    2: 'Dropable',
    7: 'Unknown',
    9: 'Unknown'
}

sleep_mapping = {value: sleep_time_mapping(value) for value in range(1, 100)}

df['_TOTINDA'] = df['_TOTINDA'].map(generic_mapping)  #Activity
df['DIABETE3'] = df['DIABETE3'].map(diabetes_mapping) #Diabetes
df['ADDEPEV2'] = df['ADDEPEV2'].map(generic_mapping)
df['_AGEG5YR'] = df['_AGEG5YR'].map(age_mapping)
df['_SMOKER3'] = df['_SMOKER3'].map(smoking_mapping)

df['_RFDRMN4'] = df['_RFDRMN4'].map(drinking_mapping)
df['_RFDRWM4'] = df['_RFDRWM4'].map(drinking_mapping)


df['CHCCOPD'] = df['CHCCOPD'].map(generic_mapping)  #COPD
df['CHCKIDNY'] = df['CHCKIDNY'].map(generic_mapping) #Kidney disease
df['CVDCRHD4'] = df['CVDCRHD4'].map(generic_mapping) #angina or coronary heart disease
df['CHCSCNCR'] = df['CHCSCNCR'].map(generic_mapping) #Skin cancer
df['CVDINFR4'] = df['CVDINFR4'].map(generic_mapping)  #myocardial infarction i.e Heart attack
df['CVDSTRK3'] = df['CVDSTRK3'].map(generic_mapping) #Stroke

df['HAVARTH3'] = df['HAVARTH3'].map(generic_mapping) #Arthritis, rheumatoid arthritis, gout, lupus, or fibromyalgia?
 
df['SLEPTIM1'] = df['SLEPTIM1'].map(sleep_mapping)

#Data Cleaning

df_filtered = df[(df['_TOTINDA'] != 'Unknown') &
                  (df['DIABETE3'] != 'Unknown') &
                  (df['ADDEPEV2'] != 'Unknown') &
                  (df['_AGEG5YR'] != 'Unknown') &
                  (df['_SMOKER3'] != 'Unknown') &
                  (df['_RFDRMN4'] != 'Unknown') &
                  (df['_RFDRWM4'] != 'Unknown') &
                  (df['CHCCOPD'] != 'Unknown') &
                  (df['CHCKIDNY'] != 'Unknown') &
                  (df['CVDCRHD4'] != 'Unknown') &
                  (df['CVDINFR4'] != 'Unknown') &
                  (df['CVDSTRK3'] != 'Unknown') &
                  (df['HAVARTH3'] != 'Unknown') &
                  (df['SLEPTIM1'] != 'Unknown') 
                  ]
                  
# Spitting relavant columns into boolean columns per unique value
df_filtered = pd.get_dummies(df_filtered, columns=['_TOTINDA', 'DIABETE3', 'ADDEPEV2', '_AGEG5YR', '_SMOKER3', '_RFDRMN4', '_RFDRWM4','CHCCOPD', 'CHCKIDNY', 'CVDCRHD4', 'CHCSCNCR' , 'CVDINFR4', 'CVDSTRK3' , 'HAVARTH3', 'SLEPTIM1'])

# Merging heaving drinking female with heavy drinking male as heavy drinker
df_filtered['Heavy_Drinker'] = df_filtered['_RFDRMN4_Heavy_Drinker'] | df_filtered['_RFDRWM4_Heavy_Drinker']

# Dropping irelavant columns
df_filtered = df_filtered.loc[:,[
                '_AGEG5YR_18-29',
                '_AGEG5YR_30-39',
                '_AGEG5YR_40-49',
                '_AGEG5YR_50-59',
                '_AGEG5YR_60-69',
                '_AGEG5YR_70-79',
                '_AGEG5YR_80+',
                'SLEPTIM1_1-4',
                'SLEPTIM1_4-8',
                'SLEPTIM1_8-12',
                'SLEPTIM1_12+',
                'Heavy_Drinker',
                '_TOTINDA_Yes',
                '_SMOKER3_smokes_every_day',
                '_SMOKER3_smokes_some_days',
                '_SMOKER3_Former_smoker' ,
                 '_SMOKER3_Never_smoked',
                'DIABETE3_Diabetes',
                'DIABETE3_Pre-diabetes',
                'ADDEPEV2_Yes',
                'CHCCOPD_Yes',
                'CHCKIDNY_Yes',
                'CVDCRHD4_Yes',
                'CHCSCNCR_Yes',
                'CVDINFR4_Yes',
                'CVDSTRK3_Yes',
                'HAVARTH3_Yes'
]] 


# Renaming columns
df_filtered = df_filtered.rename(columns={ '_AGEG5YR_18-29': 'Age:18-29',
                                            '_AGEG5YR_30-39':'Age:30-39',
                                            '_AGEG5YR_40-49':'Age:40-49',
                                            '_AGEG5YR_50-59':'Age:50-59',
                                            '_AGEG5YR_60-69':'Age:60-69',
                                            '_AGEG5YR_70-79':'Age:70-79',
                                            '_AGEG5YR_80+':  'Age:80+',
                                            'SLEPTIM1_1-4': 'Sleep:1-4',
                                            'SLEPTIM1_4-8':  'Sleep:4-8',
                                            'SLEPTIM1_8-12':  'Sleep:8-12',
                                            'SLEPTIM1_12+':  'Sleep:12+',
                                            'Heavy_Drinker': "Heavy_Drinker",
                                            '_TOTINDA_Yes' : 'Active',
                                            '_SMOKER3_smokes_every_day' : 'Smokes_Every_Day',
                                            '_SMOKER3_smokes_some_days' : 'Smokes_Some_Days',
                                            '_SMOKER3_Former_smoker' : 'Former_smoker',
                                            '_SMOKER3_Never_smoked': 'Never_Smoked',
                                            'DIABETE3_Diabetes':'Diabetes',
                                            'DIABETE3_Pre-diabetes':'Pre_Diabetes',
                                            'ADDEPEV2_Yes':'Depression',
                                            'CHCCOPD_Yes': 'COPD' ,
                                            'CHCKIDNY_Yes':'Kidney_disease',
                                            'CVDCRHD4_Yes':'Angina_Coronary_heart_disease',
                                            'CVDINFR4_Yes':'Myocardial_infarction',
                                            'CVDSTRK3_Yes':'Stroke',
                                            'HAVARTH3_Yes':'Arthritis,Gout,Lupus,Fibromyalgia',
                                            'CHCSCNCR_Yes': 'Skin_cancer',
                                            })

df_tmp = df
df = df_filtered


#Data Balancing


behaviours = ['Age:18-29', 'Age:30-39', 'Age:40-49', 'Age:50-59', 'Age:60-69',  'Age:70-79', 'Age:80+', 'Sleep:1-4',
                    'Sleep:4-8', 'Sleep:8-12', 'Sleep:12+', 'Heavy_Drinker', 'Active' , 'Smokes_Every_Day',
                    'Smokes_Some_Days', 'Former_smoker', 'Never_Smoked']

Illnesses = ['Diabetes', 'Pre_Diabetes', 'Depression', 'COPD', 'Kidney_disease', 'Angina_Coronary_heart_disease', 'Myocardial_infarction',
                'Stroke', 'Arthritis,Gout,Lupus,Fibromyalgia', 'Skin_cancer' ]

#experementing
Illnessesv2 = ['Diabetes', 'Depression', 'COPD','Arthritis,Gout,Lupus,Fibromyalgia' ]


Illness_analysis = df.copy()

#Column that is the number of Illnesses per entry
Illness_analysis['num_Illnesses'] = Illness_analysis[Illnessesv2].sum(axis=1)


############################################

#One Ilness Distrabution generation

""" 
plt.ylabel('No. of People')
plt.xlabel('No. of Illnesses')

plt.title("Multi Illness Distribution")
plt.hist(Illness_analysis['num_Illnesses'], bins=10)
plt.savefig('images/Multi_Ilness_Distrabution.png')

"""

############################################

#Creating a column that is the illnesses of the user as tuple
Illness_analysis['Illnesses'] = Illness_analysis.apply(lambda row: tuple([illness for illness in Illnesses if row.get(illness, False)]), axis=1)


############################################

#Illess distrabution generation

""" Illness_analysis.to_csv("Illness_analysis.csv" )

exploded_df = Illness_analysis.explode('Illnesses')
grouped = exploded_df.groupby('Illnesses').size()
print(grouped.index)

y_pos = np.arange(len(grouped))

print(y_pos)

# Calculate the mean and median (using numpy)
mean_occurrences = np.mean(grouped)
median_occurrences = np.median(grouped)

# Create the bar chart
plt.bar(y_pos, grouped, align='center', alpha=0.5)

# Adding the labels and title
plt.xticks(y_pos, grouped.index, rotation='vertical')
plt.ylabel('No. of entries')
plt.title('Illness Distribution')

# Add the mean and median lines (red and green respectively)
plt.axhline(y=mean_occurrences, color='r', linestyle='-', label=f'Mean: {mean_occurrences:.2f}')
plt.axhline(y=median_occurrences, color='g', linestyle='--', label=f'Median: {median_occurrences:.2f}')

# Show illustration
plt.legend()
plt.savefig('images/IllnessDistrabution.png')
 """
################################################


balanced_df = pd.DataFrame()


# Balancing Illnesses to incorperate illness combinations
for n in range(1,5):
    #divinding df by number of illnesses per entry
    n_Illness = Illness_analysis[Illness_analysis['num_Illnesses']==n]
    n_Illness_stats = n_Illness.groupby('Illnesses').size()
    mean = int(n_Illness_stats.mean())
    unique_combinations = set()
    for _, row in n_Illness.iterrows():
        unique_combinations.add(tuple(sorted(row['Illnesses'])))
    for combinations in unique_combinations:
        #df of all entries that have the same combination of ilnesses
        n_Illness_df = n_Illness[n_Illness['Illnesses'].apply(lambda x: all(illness in x for illness in combinations))]   
        count = len(n_Illness_df)
        if count > mean:
            # Undersample
            sampled_df = n_Illness_df.sample(n=mean, random_state=RANDOM_SEED)
        elif count < mean:
            # Oversample
            sampled_df = n_Illness_df.sample(n=mean, replace=True, random_state=RANDOM_SEED)
        else:
            sampled_df = n_Illness_df
        balanced_df = pd.concat([balanced_df, sampled_df], ignore_index=True)


# Adding no illness entries to the balance to prevent over-fitting
no_Illness_df = Illness_analysis[Illness_analysis['num_Illnesses']==0]
exploded_df = balanced_df.explode('Illnesses')
balanced_df_stats = exploded_df.groupby('Illnesses').size()
mean = int(balanced_df_stats.mean())
print(f"mean:{mean}")
if count > mean:
    # Undersample
    sampled_df = no_Illness_df.sample(n=mean, random_state=RANDOM_SEED)
elif count < mean:
    # Oversample
    sampled_df = no_Illness_df.sample(n=mean, replace=True, random_state=RANDOM_SEED)
else:
    sampled_df = n_Illness_df
balanced_df = pd.concat([balanced_df, sampled_df], ignore_index=True)

natural_df = df
df = balanced_df


################################################

# Balanced distrabution generation

""" exploded_df = df.explode('Illnesses')
grouped = exploded_df.groupby('Illnesses').size()
print(grouped.index)

y_pos = np.arange(len(grouped))
print(y_pos)

# Calculate the mean and median (using numpy)
mean_occurrences = np.mean(grouped)
median_occurrences = np.median(grouped)

# Create the bar chart
plt.bar(y_pos, grouped, align='center', alpha=0.5)

# Adding the labels and title
plt.xticks(y_pos, grouped.index, rotation='vertical')
plt.ylabel('No. of entries')
plt.title('Illness Distribution')

# Add the mean and median lines (red and green respectively)
plt.axhline(y=mean_occurrences, color='r', linestyle='-', label=f'Mean: {mean_occurrences:.2f}')
plt.axhline(y=median_occurrences, color='g', linestyle='--', label=f'Median: {median_occurrences:.2f}')

# Show illustration
plt.legend()
plt.savefig('images/BalancedIllnessDistrabution.png')

 """
################################################

#Data Normilisation

df_normalised_balanced = pd.DataFrame({'Behaviour': df[behaviours].astype(int).values.tolist() ,
                              'Illnesses': df[Illnesses].astype(int).values.tolist(), })

df_normalised_natural = pd.DataFrame({'Behaviour': natural_df[behaviours].astype(int).values.tolist() ,
                              'Illnesses': natural_df[Illnesses].astype(int).values.tolist(), })




df_normalised_balanced.to_csv("balanced_distrabution.csv" )
df_normalised_natural.to_csv("natural_distrabution.csv" )


df_filtered.to_csv('filtered_data.csv', index=False)
balanced_df.to_csv('balanced_data.csv', index=False) 


print(f"Original DataFrame size: {len(df_tmp)}")
print(f"Filtered DataFrame size: {len(df)}")
print(f"Number of rows removed: {len(df_tmp) - len(df)}")