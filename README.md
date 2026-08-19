# Fluid Intelligence CFD Scaling

Reproducibility code for the scaling-law and cost-sensitivity analysis in:

> Neil Ashton, Johannes Brandstetter and Siddhartha Mishra, [“Fluid Intelligence: A Forward Look on AI Foundation Models in Computational Fluid Dynamics”](https://arxiv.org/abs/2511.20455), arXiv:2511.20455.

The repository intentionally contains a single plotting program. It reproduces the six sensitivity figures from the analytical model; the paper provides the derivation, interpretation and full discussion of the assumptions.

## Reproduce the figures

Python 3.10 or newer is recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
MPLBACKEND=Agg python3 scaling_plots.py
```

`MPLBACKEND=Agg` makes the command suitable for headless systems. Omit it if you also want Matplotlib to open the figures interactively.

## Model inputs and assumptions

All numerical assumptions are explicit in `scaling_plots.py`. The baseline model evaluates sample counts from zero to two million and compares CFD data-generation cost with model-training cost. In particular:

- data generation uses 2,800 FLOPs per cell per step, 500 million cells and 200,000 time steps;
- model training uses scaling exponents `alpha = 0.24` and `beta = 0.43` over 100 epochs;
- the hardware-throughput, utilisation and price factors are encoded in `K_DG` and `K_MT`; and
- plotted costs are reported in millions of US dollars.

The sensitivity sweeps vary one input at a time while retaining the remaining baseline values:

| Figure | Varied quantity | Range |
| --- | --- | --- |
| `cost_analysis_alpha.png` | Training scaling exponent alpha | 0.22–0.26 |
| `cost_analysis_beta.png` | Training scaling exponent beta | 0.40–0.47 |
| `cost_analysis_epochs.png` | Training epochs | 10, 50, 100, 200, 500 |
| `cost_analysis_datagen_flops.png` | CFD FLOPs per cell per step | 2,000–10,000 |
| `cost_analysis_cells.png` | CFD cells | 100 million–1 billion |
| `cost_analysis_timesteps.png` | CFD time steps | 50,000–500,000 |

These values are analytical scenario assumptions, not universal hardware-price forecasts. Consult the paper before adapting or interpreting them.

## Outputs

Running the script writes the six PNG files listed above to the current working directory. No external input data are required, and no network access is used.

## Citation

Citation metadata are provided in [`CITATION.cff`](CITATION.cff). If you use the analysis or code, please cite the paper and link to this repository.

## Licence

The code is available under the [Apache License 2.0](LICENSE).
