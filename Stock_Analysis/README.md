# 📈 AI Stock Analysis Assistant

An AI-powered Stock Analysis Assistant built using Python, Gemini AI, Yahoo Finance, and NewsAPI.

The assistant allows users to analyze Indian NSE-listed companies, compare stocks, manage a portfolio, and maintain conversation memory through natural language interactions.

---

# Features

- AI-powered stock analysis using Google Gemini
- Company information lookup
- Live market data from Yahoo Finance
- Financial ratio analysis
- Technical indicators
  - SMA
  - RSI
  - MACD
  - Bollinger Bands
- Latest company news
- Portfolio management
- Company comparison
- Conversation memory
- Intelligent company name recognition
- Follow-up question handling

---

# Technologies Used

- Python
- Google Gemini API
- Yahoo Finance (yfinance)
- NewsAPI
- Pandas
- TA Library
- RapidFuzz

---

# Project Structure

```
Stock_Analysys/

│
├── agents/
│   └── manager_agent.py
│
├── tools/
│   ├── stock_tool.py
│   ├── technical_tool.py
│   ├── news_tool.py
│   ├── portfolio_tool.py
│   └── comparison_tool.py
│
├── utils/
│   ├── helpers.py
│   └── memory_manager.py
│
├── memory/
│   ├── history.json
│   └── portfolio.json
│
├── data/
│   └── nse_symbols.csv
│
├── main.py
├── config.py
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure API keys inside `config.py`.

Run the project

```bash
python main.py
```

---

# Example Commands

Analyze Infosys

Compare Infosys and TCS

What is the PE ratio of Reliance?

Add Infosys to my portfolio

Show portfolio

Analyze portfolio

Should I buy it?

---

# Future Improvements

- Stock price prediction using Machine Learning
- Interactive dashboard using Streamlit
- Email alerts
- Watchlist support
- Sentiment analysis from news and social media
- Price charts and visualizations

---

# Disclaimer

This project is intended for educational purposes only.

The assistant provides analysis based on publicly available financial data and should not be considered financial or investment advice.