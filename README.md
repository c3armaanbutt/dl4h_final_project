# CS 598: Deep Learning For Healthcare Final Project

By: Armaan R. Butt and Harikrishna Bojja
{arbutt2, hbojja2}@illinois.edu

Group ID: 213, Paper ID: 283

## Paper: Categorization of free-text drug orders using character-level recurrent neural networks [[1]](#1)

---

## Dependencies

Download the files below from MIMIC III dataset and copy them to "data" directory under root.

#### PRESCRIPTIONS.CSV
#### NOTEEVENTS.CSV


## Exploratory Data Analysis(EDA)

The jupyter notebooks below show the code on how we performed data analysis and prescriptions and noteevents csv files.

#### \src\data_profiling\profile_free_text.ipynb
#### \src\data_profiling\profile_prescription_data.ipynb


## Data Processing

After finishing the dependecies step use the notebook below to extract the drug codes from prescriptions data.


#### \src\data_processing\extract_drug_codes.ipynb


The jupyter notebook below reads the Note events and pre-processes the data and write the data to "/data/processed" folder.

####  \src\data_processing\note_events_processing.ipynb

## Training Code

## Evaluation Code

## Pre-trained Models

## Results

### Baseline SVM

The baseline model SVM model was trained on the top 22 common drugs in our dataset (NDC). The SVM model used a linear kernel (LinearSVC) with the input text data being vectorized at the character level using `TfidVectoriezer` using `scikit-learn`. `TfidVectoriezer` was configure to generate trigrams from the text data.

| NDC         | Accuracy (%) | Precision (%) | Recall (%) |
| ----------- | ------------ | ------------- | ---------- |
| 00713016550 | 90           | 83            | 76         |
| 00487950125 | 92           | 89            | 76         |
| 00517391025 | 92           | 92            | 91         |
| 51079001920 | 90           | 90            | 91         |
| 11098003002 | 95           | 88            | 44         |
| 00054829725 | 93           | 88            | 72         |
| 00045025501 | 98           | 80            | 5          |
| 00338055002 | 86           | 88            | 91         |
| 00409131230 | 94           | 90            | 59         |
| 00045152510 | 93           | 87            | 65         |
| 00074407532 | 87           | 87            | 77         |
| 51079080120 | 91           | 90            | 85         |
| 51079025520 | 91           | 90            | 85         |
| 00074176201 | 87           | 86            | 71         |
| 00781305714 | 97           | 87            | 13         |
| 00054465025 | 95           | 86            | 65         |
| 00008084199 | 94           | 91            | 74         |
| 58177000104 | 93           | 95            | 91         |
| 00781188313 | 96           | 93            | 55         |
| 00517293025 | 93           | 94            | 95         |
| 00338355248 | 90           | 84            | 71         |
| 00002735501 | 89           | 89            | 83         |
| **Average** | 92           | 88            | 70         |

### GRU - RNN

## References

<a id="1">[1]</a>
Raiskin Y, Eickhoff C, Beeler PE. Categorization of free-text drug orders using character-level recurrent neural networks. Int J Med Inform. 2019 Sep;129:20-28. doi: 10.1016/j.ijmedinf.2019.05.020. Epub 2019 May 23. PMID: 31445256.
