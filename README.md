# 🏥 Rural Health Camp Organizer and Patient Risk Analyzer

## 📌 Project Overview

The **Rural Health Camp Organizer and Patient Risk Analyzer** is a Python-based application designed to organize patient information collected during rural health camps and analyze health-related data.

The application stores patient records in CSV files, categorizes patients using predefined blood pressure and blood sugar thresholds, identifies common symptoms in different villages, analyzes age groups, and compares data collected from two health camps.

## 🎯 Objectives

- To maintain patient information collected during rural health camps.
- To store and retrieve patient records using CSV files.
- To categorize patients into illustrative high-risk, medium-risk, and low-risk groups using predefined rules.
- To identify the most frequently reported symptoms in each village.
- To analyze risk categories across different age groups.
- To compare average blood pressure between two health camps.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy
- **Data Storage:** CSV files
- **Tools:** Git and GitHub

## ✨ Features

### 1. Patient Data Entry
Collects patient details, including name, village, age, blood pressure, blood sugar level, weight, and symptoms.

### 2. Data Storage
Saves patient records to CSV files and loads existing records for analysis.

### 3. Patient Risk Analysis
Uses predefined blood pressure and blood sugar thresholds to assign illustrative risk categories.

### 4. Symptom Analysis
Groups patient records by village and identifies the most frequently reported symptom in each village.

### 5. Age Group Analysis
Groups patients by age and displays the distribution of risk categories within each group.

### 6. Health Camp Comparison
Compares the average blood pressure recorded at a previous camp with that of a current camp.

## 📂 Project Structure

```text
Rural-Health-Camp-Organizer-and-Patient-Risk-Analyzer/
│
├── main.py
├── data_entry.py
├── analyzer.py
├── data/
│   ├── camp1.csv
│   └── camp2.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.9 or later
- pip package manager

### Step 1: Clone the repository

```bash
git clone https://github.com/Jeeshu09/Rural-Health-Camp-Organizer-and-Patient-Risk-Analyzer.git
```

### Step 2: Navigate to the project directory

```bash
cd Rural-Health-Camp-Organizer-and-Patient-Risk-Analyzer
```

### Step 3: Install the required libraries

```bash
pip install pandas numpy
```

### Step 4: Run the application

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

## 🖥️ Application Menu

The application provides the following menu options:

1. Add Patient
2. Save Data
3. Analyze Data
4. Compare Camps
5. Exit

Choose an option and follow the instructions displayed in the terminal.

## 📊 Data Fields

| Field | Description |
|---|---|
| Name | Patient's name |
| Village | Patient's village |
| Age | Patient's age in years |
| BP | Recorded blood pressure value |
| Sugar | Recorded blood sugar value |
| Weight | Patient's weight |
| Symptoms | Reported symptoms |

## 🔮 Future Enhancements

- Develop a graphical user interface.
- Add visual charts and graphs for health data.
- Generate downloadable health camp reports.
- Improve data validation and patient record management.
- Add more comprehensive statistical comparisons between camps.
- Introduce secure access controls to protect patient information.

## ⚠️ Limitations and Disclaimer

This project is intended for educational and data-analysis purposes. The risk categories are based on simplified, predefined thresholds and are not medically validated. They must not be used to diagnose diseases or replace professional medical evaluation.

Any real patient information should be handled securely, with appropriate consent and privacy protections.

## 👨‍💻 Author

**Jeeshu09**

GitHub: [Jeeshu09](https://github.com/Jeeshu09)

---

⭐ If you find this project useful, consider starring the repository.
