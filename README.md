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
