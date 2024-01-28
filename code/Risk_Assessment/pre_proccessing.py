import pandas as pd
from sleep_Dict_Generator import sleep_time_mapping

file_path = 'nysdoh_brfss_surveydata_2014.sas7bdat'
df = pd.read_sas(file_path)

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
df['CVDINFR4'] = df['CVDINFR4'].map(generic_mapping)  #myocardial infarction 
df['CVDSTRK3'] = df['CVDSTRK3'].map(generic_mapping) #Stroke

df['HAVARTH3'] = df['HAVARTH3'].map(generic_mapping) #Arthritis, rheumatoid arthritis, gout, lupus, or fibromyalgia?
 
df['SLEPTIM1'] = df['SLEPTIM1'].map(sleep_mapping)


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
                  

df_filtered = pd.get_dummies(df_filtered, columns=['_TOTINDA', 'DIABETE3', 'ADDEPEV2', '_AGEG5YR', '_SMOKER3', '_RFDRMN4', '_RFDRWM4','CHCCOPD', 'CHCKIDNY', 'CVDCRHD4', 'CHCSCNCR' , 'CVDINFR4', 'CVDSTRK3' , 'HAVARTH3', 'SLEPTIM1'])


df_filtered['Heavy_Drinker'] = df_filtered['_RFDRMN4_Heavy_Drinker'] | df_filtered['_RFDRWM4_Heavy_Drinker']


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
                'DIABETE3_Diabetes',
                'DIABETE3_Pre-diabetes',
                'ADDEPEV2_Yes',

                'CHCCOPD_Yes',
                'CHCKIDNY_Yes',
                'CVDCRHD4_Yes',
                'CHCSCNCR_Yes',
                'CVDINFR4_Yes',
                'CVDSTRK3_Yes',
                'HAVARTH3_Yes',
                
                '_SMOKER3_smokes_every_day',
                '_SMOKER3_smokes_some_days',
                '_SMOKER3_Former_smoker' ,
                 '_SMOKER3_Never_smoked'



]] 


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
                                            '_TOTINDA_Active':'Active',
                                            'DIABETE3_Diabetes':'Diabetes',
                                            'DIABETE3_Pre-diabetes':'Pre_Diabetes',
                                            'ADDEPEV2_Yes':'Depression',
                                            'CHCCOPD_Yes': 'COPD' ,
                                            'CHCKIDNY_Yes':'Kidney_disease',
                                            'CVDCRHD4_Yes':'Angina_Coronary_heart_disease',
                                            'CVDINFR4_Yes':'Myocardial_infarction',
                                            'CVDSTRK3_Yes':'Stroke',
                                            'HAVARTH3_Yes':'Arthritis,Gout,Lupus,Fibromyalgia',
                                            'CHCSCNCR_Yes': 'Skin cancer',
                                            '_SMOKER3_smokes_every_day' : 'Smokes_Every_Day',
                                            '_SMOKER3_smokes_some_days' : 'Smokes_Some_Days',
                                            '_SMOKER3_Former_smoker' : 'Former_smoker',
                                            '_SMOKER3_Never_smoked': 'Never_Smoked',
                                            '_TOTINDA_Yes' : 'Active',
                                            })


output_file_path = 'filtered_data.csv'
df_filtered.to_csv(output_file_path, index=False)


print(f"Original DataFrame size: {len(df)}")
print(f"Filtered DataFrame size: {len(df_filtered)}")
print(f"Number of rows removed: {len(df) - len(df_filtered)}")