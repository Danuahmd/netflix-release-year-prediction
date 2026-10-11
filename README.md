# Netflix Release Year Prediction

## Project Overview
This project explores the Netflix titles dataset and applies machine learning regression algorithms to predict the release year of Netflix titles.

## Dataset
- File: `netflix_titles.csv`
- Target variable: `release_year`
- Features: Other available columns after preprocessing.

## Machine Learning Algorithms
1. Least Angle Regression (LARS)
2. Linear Regression
3. Gradient Boosting Regressor

## Workflow
1. Load and inspect the dataset.
2. Clean missing values.
3. Separate features and target.
4. Split the dataset into training and testing sets.
5. Preprocess numerical and categorical features.
6. Train the regression models.
7. Evaluate model performance using MAE, MSE, and R².

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run
1. Clone or download this repository.
2. Install the required libraries.
3. Open `Netflix Movies and TV Shows.ipynb` in Jupyter Notebook or VS Code.
4. Run the notebook cells in order.

## Notes
This is an educational machine learning project. Model performance should be evaluated on the test set before drawing conclusions.
