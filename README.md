# 📊 Distribution Fitter

A Python tool to analyze numeric datasets and determine the **best-fitting statistical distribution** using the **Kolmogorov–Smirnov test**.

This script allows input either through a `.csv` file upload or manual keyboard entry, then fits multiple distributions (Normal, Exponential, Gamma, Log-Normal) and returns the goodness-of-fit results.

---

## ✨ Features

- Fits common continuous distributions:
  - Normal (`stats.norm`)
  - Exponential (`stats.expon`)
  - Gamma (`stats.gamma`)
  - Log-Normal (`stats.lognorm`)
- Performs **Kolmogorov–Smirnov test (K-S test)** for goodness-of-fit
- Accepts data input via:
  - 📁 CSV file (uploaded by user)
  - ⌨️ Manual input (comma-separated numbers)
- Reports:
  - Fitted parameters
  - D-statistic
  - p-value
  - Best-fitting distribution

---

## 📦 Requirements

Install required libraries with:

```bash
pip install numpy scipy
---

## ▶️ How to Use

### 📁 Option 1: Upload CSV
Prepare a `.csv` file with a single column of numeric values (no header or one header row), and upload it when prompted.

```plaintext
1.2
2.4
3.1
...

🔒 Notes
The script does not store or upload any data. It is a local or Colab-based tool.

A higher p-value means the distribution is a better fit for the data (typically p > 0.05 is acceptable).

The tool is suitable for educational, academic or practical analysis purposes.

