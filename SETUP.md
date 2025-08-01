# 🛠️ Technical Setup Guide

## Prerequisites
- Python 3.7+
- OpenRouter API key

## Quick Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Get OpenRouter API Key
1. Visit [OpenRouter.ai](https://openrouter.ai/)
2. Sign up and get your API key
3. Set environment variable:
```bash
export OPENROUTER_API_KEY="your-api-key-here"
```

### 3. Add Your Dataset
Place your basketball dataset in the `data/` folder as `syracuse_womens_basketball_2023_24.csv`

### 4. Run Analysis
```bash
# Generate baseline statistics and visualizations
python3 scripts/basketball_analyzer.py

# Test LLMs with the data
python3 scripts/llm_tester_updated.py
```

## Scripts Overview

- **`basketball_analyzer.py`**: Generates baseline statistics and visualizations
- **`llm_tester_updated.py`**: Tests multiple LLMs with basketball data
- **`test_setup.py`**: Verifies API key and data loading

## Results
- **Visualizations**: Generated in `results/` folder
- **LLM Responses**: Saved to `results/llm_testing_results.json`
- **Baseline Analysis**: Saved to `results/basketball_analysis.json`

## Troubleshooting
- **API Key Issues**: Ensure `OPENROUTER_API_KEY` is set correctly
- **Model Errors**: Some models may not be available on OpenRouter
- **Data Loading**: Check that your CSV file is in the correct format

For detailed research findings and methodology, see the main [README.md](README.md) file. 