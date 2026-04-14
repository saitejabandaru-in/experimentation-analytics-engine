<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1D4350,100:A43931&height=200&section=header&text=A%2FB%20Testing%20Lab&fontSize=40&fontColor=E6EEF3&animation=fadeIn&fontAlignY=40" />
</p>

<p align="center">
  🧪 Experimentation Platform &nbsp;|&nbsp; 📊 Statistical Testing &nbsp;|&nbsp; 📈 Data-Driven Decisions
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Statistics-SciPy-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Bayesian-PyMC-purple?style=flat-square"/>
  <img src="https://img.shields.io/badge/Visualization-Plotly-brightgreen?style=flat-square"/>
  <img src="https://img.shields.io/badge/Data-Pandas-lightgrey?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square"/>
</p>

---

# 🧪 A/B Testing Lab

A **statistical experimentation platform** designed for **rigorous A/B testing, Bayesian analysis, and decision optimization**.

This project simulates how modern product teams and data scientists run **controlled experiments to drive product growth and user engagement**.

---

## 🧠 Overview

The **A/B Testing Lab** enables:

- Frequentist and Bayesian hypothesis testing  
- Sequential experimentation with early stopping  
- Conversion funnel analysis  
- Effect size estimation and power analysis  
- Multi-variant (A/B/C/n) experimentation  

Built to reflect **real-world experimentation platforms used in tech and product analytics**.

---

## ⚙️ Core Features

### 🔮 Bayesian A/B Analysis
- Posterior probability distributions  
- Credible intervals for uncertainty estimation  
- More intuitive decision-making vs p-values  

### 📊 Conversion Funnel Analysis
- Multi-stage tracking:
  - Visit → Signup → Activate → Convert  
- Identifies drop-off points in user journey  

### 📏 Statistical Significance
- p-value computation  
- Confidence intervals  
- Effect size (Cohen’s d)  

### ⏱️ Sequential Testing
- Early stopping rules  
- Alpha-spending functions  
- Reduces experiment runtime  

### 📐 Power Analysis
- Sample size estimation  
- Minimum Detectable Effect (MDE)  
- Power curves for experiment planning  

### 🔀 Multi-Variant Testing
- Supports A/B/C/n experiments  
- Multiple comparison corrections  

---

## 🧬 System Workflow


Experiment Data (User Interactions)
↓
Data Processing & Cleaning
↓
Statistical Analysis (Frequentist / Bayesian)
↓
Sequential Testing & Power Analysis
↓
Visualization (Funnel + Posterior + Dashboard)
↓
Decision Insights

```id="abflow1"

---

## 🗂️ Project Structure

```

data/
└── experiment_logs/

analysis/
├── bayesian_ab.py
├── frequentist.py
├── sequential_test.py
└── power_analysis.py

visualization/
├── funnel_chart.py
├── posterior_plot.py
└── significance_dashboard.py

tests/

````id="abstruct1"

---

## 🚀 Quick Start

### Install dependencies
```bash
pip install -r requirements.txt
````

### Run experiment analysis

```bash id="abrun1"
python -m abtesting.analyze --experiment homepage_cta --method bayesian
```

---

## 🧪 Tech Stack

* Python 3.10+
* SciPy
* PyMC
* Plotly
* Pandas

---

## 📈 What This Project Demonstrates

✔ A/B testing and experimentation design
✔ Bayesian vs frequentist analysis
✔ Sequential hypothesis testing
✔ Power and sample size estimation
✔ Funnel analytics and product insights
✔ Data-driven decision frameworks

---

## 👨‍💻 Author

**Sai Teja Bandaru**
*Data Scientist & AI Researcher*

🌐 Portfolio
💼 LinkedIn
💻 GitHub

---

## 📄 License

MIT License — see `LICENSE` for details.

---

## ⭐ Support

If you find this useful:

⭐ Star the repo
🍴 Fork it
📢 Share it

---

> Making product decisions statistically sound and data-driven.
