import pandas as pd 

inCSV = 'data/input/All-NBM-CAI-June-2014/All-NBM-CAI-June-2014.csv'

df = pd.read_csv(inCSV, delimiter='|')

ouCSV = 'data/processing/all-nbm-cai-june-2014.csv'
 
df.to_csv(ouCSV, index=False)