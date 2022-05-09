import pandas as pd
import numpy as np
import re
import csv
import string
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
np.random.seed(500)

EVENTS_TO_PROCESS = 50000

df_prescriptions = pd.read_csv(
    'C:/Users/harim/OneDrive/Documents/GitHub/dl4h_final_project_1/data/processed/ndc_codes_extracted.csv', dtype=str)
print("Pres counts:", df_prescriptions.count())

ndc_to_drug_names = {}
drug_to_ndc_names = {}
durg_name_set = set()

for index, record in df_prescriptions.iterrows():
    drug, ndc = record['DRUG'], record['NDC']
    drug = drug.strip()
    ndc = ndc.strip()

    if ndc not in ndc_to_drug_names:
        ndc_to_drug_names[ndc] = []

    # Remove non alpha numeric characters and make lowercase
    drug = re.sub('[^A-Za-z0-9]+', '', drug)
    drug = drug.lower()
    ndc_to_drug_names[ndc].append(drug)

    if len(drug) >= 3:
        durg_name_set.add(drug)

    if drug not in drug_to_ndc_names:
        drug_to_ndc_names[drug] = [ndc]
    else:
        drug_to_ndc_names[drug].append(ndc)

print("Unique Durg counts:", len(drug_to_ndc_names))


df_noteevents = pd.read_csv(
    'C:/Users/harim/OneDrive/Documents/GitHub/dl4h_final_project_1/data/mimic-iii-clinical-database-demo-14/NOTEEVENTS.csv', dtype=str)

df_noteevents.sort_values('CHARTDATE')

df_noteevents = df_noteevents.head(EVENTS_TO_PROCESS)

print("Event counts:", df_noteevents.count())

stopset = set(stopwords.words('english') + list(string.punctuation))

progress_count = 0
event_count = df_noteevents.count()


def getAllNDCs(drugs):
    codes = []
    for drug in drugs:
        codes.extend(drug_to_ndc_names[drug])

    return codes


process_count = 0


def clean_up_text(row):
    text = row['TEXT']
    tokens = word_tokenize(text.lower())
    clean_tokens = [re.sub('[^A-Za-z0-9]+', '', i)
                    for i in tokens if i not in stopset]

    drugs_ext = durg_name_set.intersection(clean_tokens)
    codes = getAllNDCs(drugs_ext)

    cleaned_text = ' '.join(clean_tokens)
    codes_joined = ''
    if len(codes) > 0:
        codes_joined = ','.join(codes)

    return cleaned_text, codes_joined


print("Finished Normalizing....")

df_noteevents[['CLEAN_TEXT', 'DRUGS_PRESENT']] = df_noteevents.apply(
    clean_up_text, axis=1, result_type="expand")

print("Finished labeling....")

df_noteevents.to_csv('C:/Users/harim/OneDrive/Documents/GitHub/dl4h_final_project_1/data/processed/NOTE_EVENTS_WITH_DRUGS.csv',
                     index=False, quoting=csv.QUOTE_ALL, quotechar='"')
