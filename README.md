# Monte Carlo VaR & CVaR Simulator

**Goal:** Simulate portfolio returns via Geometric Brownian Motion; compute empirical and parametric VaR/CVaR.

## Structure

- `data/` — raw historical price CSVs  
- `src/`  — core modules (`simulation.py`, `risk.py`, `utils.py`)  
- `notebooks/` — exploratory analysis and plots  
- `reports/`   — final PDF report  

## Quick Start

```bash
# 1. Activate environment
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run notebook
jupyter lab notebooks/analysis.ipynb

