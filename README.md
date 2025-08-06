# Economic Analysis Project (Data Analyst Assessment)

This project analyses key GDP and population trends for multiple countries over the past 20 years using World Bank data.  
It focuses on calculating GDP per Capita, visualizing trends, and answering analytical questions.

---

## 🔧 Tools Used
- Python
- Pandas
- Matplotlib
- Openpyxl
- Excel

---

## 💡 Steps Performed

1. Loaded raw GDP and Population data from Excel sheets.
2. Cleaned metadata and selected only relevant year columns.
3. Converted data from wide to long format.
4. Merged GDP & Population on Country Name + Year.
5. Calculated **GDP per Capita**.
6. Built trend line visualizations.
7. Identified best performing country over last 10 years based on GDP per Capita growth.
8. Analysed global GDP per Capita average trend over last 20 years.

---

## 📊 Key Observation Highlights

- **Best performing country (last 10 years)**: *Guyana*  
- Global GDP per Capita has generally risen, with dips around 2009 & 2020 (recession & COVID-19).
- Small emerging economies show rapid improvements compared to developed nations.

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python analysis.py
