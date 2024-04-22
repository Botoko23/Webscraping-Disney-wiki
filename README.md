# Disney wikipedia scraping
This project is about scraping data of Disney movies in wikipedia
## 📝 Table of Contents
- [Setup & Requirements](#-setup--requirements)
- [Usage](#-usage)
- [Notes](#-notes)

## 🛠 Setup & Requirements
1. **requirements**: pip install packages from `requirements.txt`
2. **Knowledge required**: beautifulsoup, python, pytest, regex

## 🚀 Usage
1. **Scrape data**: Scrape Disney data from wikipedia, then clean the data as in `disney.ipynb` and save to into folder `dataset`.
2. **Analysis with Mongodb**: Data queries against movies_collection and directors_collection are performed in `mongodb.ipynb`

## 📝 Notes
- `money_conversion.py` is used to develop parsing function for Budget and Box office data. `test_money_conversion.py` is used to help test if the function works for all cases of data.