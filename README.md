# CS 598: Deep Learning For Healthcare Final Project

By: Armaan R. Butt and Harikrishna Bojja
{arbutt2, hbojja2}@illinois.edu

Group ID: 213, Paper ID: 283

## Paper: Categorization of free-text drug orders using character-level recurrent neural networks [[1]](#1)

---

## Dependencies

### Computer Specs

### Runtime

### Python Libraries

- Numpy
- Pandas
- scikit-learn
- Pytorch
- Keras
- Matplotlib
- Seaborn
- Regex
- NLTK
- CSV
- Pickle
- Pandarallel
- JSON
- Statistics

## Data Download Instructions

Please download the and extract the `NOTEEVENTS.csv` and `PRESCRIPTIONS.csv` to `/data/real-mimic-iii-database`.

## Data Pre-Processing Code

Run the following jupyter notebooks in order. It takes approximatey 1 hour to finish the data preprocessing.

1. `/src/data_processing/extract_drug_codes.ipynb`
2. `/src/data_processing/note_events_processing.ipynb`

Once complete it will generate two new files in `/data/processed/`:

- `NOTEEVENTS_ML_DATASET.csv`
- `ndc_codes_extracted.csv`

## Train and Evaluate Models Code

To train and evaluate the SVM and GRU Models run the following jupyter notebooks:

1. `/src/ml/multi_class_svm.ipynb`
2. `/src/ml/gru_model.ipynb`

Results will be persisted in two csvs in the `/data/results` directory.

- `GRU_RESULTS.csv`
- `SVM_results.csv`

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

| Model             | Hidden State Size | Number of Epochs | Mean Training Accuracy (%) | Mean Test Accuracy (%) | Mean Training Loss (%) | Mean Test Loss (%) |
| ----------------- | ----------------- | ---------------- | -------------------------- | ---------------------- | ---------------------- | ------------------ |
| Bidirectional GRU | 32                | 3                | 75.44                      | 75.69                  | 56.44                  | 55.49              |
| Bidirectional GRU | 64                | 3                | 75.45                      | 75.69                  | 56.22                  | 55.52              |
| Bidirectional GRU | 128               | 3                | 75.44                      | 75.69                  | 56.26                  | 55.66              |

## References

<a id="1">[1]</a>
Raiskin Y, Eickhoff C, Beeler PE. Categorization of free-text drug orders using character-level recurrent neural networks. Int J Med Inform. 2019 Sep;129:20-28. doi: 10.1016/j.ijmedinf.2019.05.020. Epub 2019 May 23. PMID: 31445256.
