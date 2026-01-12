# Financial Engineering and Quantitative Analysis Portfolio

Welcome to my portfolio. This repository contains a collection of projects focused on Financial Technology, Risk Simulation, and Automated Data Processing. My objective is to develop computational tools that transform raw financial data into structured, actionable insights for valuation and risk management.

---

## Current Projects

### 1. Stock Data Parser
A Python-based utility designed to extract and normalize ticker symbols and pricing data from unstructured trading logs.

* **Core Logic:** Utilizes anchor-tagging and dynamic string slicing to process variable-length data (e.g., 3-letter vs. 4-letter tickers) without hardcoded indices.
* **Key Feature:** Implements a dynamic search window (`loc`) that shifts programmatically to ensure efficient parsing of complex log strings.
* **Data Integrity:** Normalizes mixed-case inputs and standardizes raw pricing strings into validated floating-point numbers.

---

## Active Development: Financial Modeling and Risk

I am currently developing the following modules focused on valuation and market uncertainty:

### 1. Automated DCF (Discounted Cash Flow) Engine
* **Objective:** Determine the intrinsic value of an asset by projecting and discounting future Free Cash Flows (FCF).
* **Methodology:** Implementing Time Value of Money (TVM) principles to discount cash flows using a Weighted Average Cost of Capital (WACC).
* **Planned Feature:** A sensitivity analysis matrix to evaluate share price volatility relative to terminal growth and discount rate fluctuations.



### 2. Monte Carlo Risk Simulator
* **Objective:** Model portfolio uncertainty by simulating thousands of potential market outcomes.
* **Technical Focus:** Leveraging Python libraries (NumPy) to model price volatility and calculate Value at Risk (VaR).
* **Application:** Quantitative risk management for equity portfolios during high-volatility market events.



---

## Technical Toolkit

* **Languages:** Python (String Manipulation, Data Casting, Mathematical Modeling)
* **Tools:** Git, VS Code, GitHub
* **Focus Areas:** Financial Modeling, Log Analysis, Data Cleaning, Risk Simulation

---

## Contact and Connect

* **GitHub:** [branozk](https://github.com/branozk)
* **Collaboration:** I am open to discussing Python projects related to financial automation and quantitative research.
