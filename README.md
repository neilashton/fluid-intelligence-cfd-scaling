# Fluid Intelligence CFD Scaling

This repository contains the Python script used to generate the scaling-cost
plots for the CFD foundation-model analysis in:

Neil Ashton, Johannes Brandstetter, and Siddhartha Mishra,
["Fluid Intelligence: A Forward Look on AI Foundation Models in Computational
Fluid Dynamics"](https://arxiv.org/abs/2511.20455), arXiv:2511.20455.

For the full derivation, assumptions, parameter choices, and discussion of the
scaling law, please refer to the arXiv paper.

## Usage

Install the plotting dependencies:

```bash
python3 -m pip install numpy matplotlib
```

Run the script from the repository root:

```bash
python3 scaling_plots.py
```

The script writes six PNG files:

- `cost_analysis_alpha.png`
- `cost_analysis_beta.png`
- `cost_analysis_epochs.png`
- `cost_analysis_datagen_flops.png`
- `cost_analysis_cells.png`
- `cost_analysis_timesteps.png`

## Publication release

Version 1.0.0 preserves the numerical code used for Figure 2 of
"A Forward Look on AI Foundation Models in Computational Fluid Dynamics"
by Neil Ashton, Johannes Brandstetter and Siddhartha Mishra. The earlier
arXiv title linked above includes the prefix "Fluid Intelligence".

All six PNG panels were verified against the manuscript's source images
using Python 3.12.4, NumPy 2.0.0 and Matplotlib 3.9.1. To reproduce them:

```bash
python3 -m pip install -r requirements-reproduce.txt
MPLBACKEND=Agg python3 scaling_plots.py
```

The script uses deterministic analytical parameter grids and requires no
external input data. With the non-interactive Agg backend, the final
`plt.show()` can emit a harmless warning after all six files have been saved.

The archived release's citation metadata are in `CITATION.cff`.
The code is distributed under the Apache License 2.0 in `LICENSE`.
