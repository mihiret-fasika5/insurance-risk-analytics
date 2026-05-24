Objective as Marketing Analytics Engineer
The objective of your analyses is to help optimise the marketing strategy and discover "low-risk" targets for which the premium could be reduced, thereby creating an opportunity to attract new clients.

To deliver the business objectives, you will need to:

Build a deep understanding of insurance terminology and risk metrics.
Statistically validate or reject key hypotheses about risk drivers across provinces, zip codes, and gender; forming the basis of a new segmentation strategy.
Develop predictive models that estimate claim severity and the probability of a claim, which together form the core of a dynamic, risk-based pricing system.
Communicate findings and recommendations in a clear, business-facing report that ACIS leadership can act on.

## DVC Setup

### Install DVC

pip install dvc

### Initialize DVC

dvc init

### Configure Local Remote Storage

mkdir ~/dvc-storage

dvc remote add -d localstorage ~/dvc-storage

### Pull Dataset Versions

dvc pull

---

## Running the Project

### Run EDA Notebook

jupyter notebook notebooks/

### Run Data Cleaning Script

python scripts/data_cleaning.py

---

## Dataset Versioning

Tracked datasets:
- Raw dataset
- Cleaned dataset

Use:

dvc pull
dvc push

to synchronize data versions.

---

## Key Technologies

- Python
- Pandas
- Seaborn
- Matplotlib
- DVC
- Git
