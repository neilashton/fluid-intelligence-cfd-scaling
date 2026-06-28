import numpy as np
import matplotlib.pyplot as plt


plt.rcParams.update({
    'font.size': 22,
    'axes.labelsize': 22,
    'axes.titlesize': 22,
    'xtick.labelsize': 22,
    'ytick.labelsize': 22,
    'legend.fontsize': 16,
    'figure.figsize': (10, 6),
    'axes.grid': True,
    'grid.alpha': 0.3,
    'lines.linewidth': 5.5,
})

# Constants & Pre-calculations
N, S, FX = np.linspace(0, 2e6, 100), 1e6, '#1f77b4'
K_DG = 8.0 / (0.15 * 8e13 * 3600)
K_MT = 8.0 / (0.6 * 5e15 * 3600) * 5.2
SZ = (5e8 / 64) * 1024 * 6


# Cost Functions
def c_dg(n, f=2800, c=5e8, t=2e5):
    return n * c * t * f * K_DG


def c_mt(n, a=.24, b=.43, e=100):
    return n * 50 * e * (SZ + 32**3 * (n**(b/a))) * K_MT


# Base Costs
yd, yt = c_dg(N), c_mt(N)

# Plot Configurations:
# (Name, Title, Range, CostFn, LabelFn, FixedY, FixedLbl, FixedLS, FixedLW, VaryLS)
cfgs = [
    (
        'alpha',
        r'$\alpha$',
        np.linspace(.22, .26, 5),
        lambda v: c_mt(N, a=v, b=.425),
        lambda v: fr'Training cost ($\alpha$={v:.3f})',
        yd,
        'Data generation cost',
        '--',
        2.5,
        '-',
    ),
    (
        'beta',
        r'$\beta$',
        np.linspace(.4, .47, 5),
        lambda v: c_mt(N, b=v),
        lambda v: fr'Training cost ($\beta$={v:.3f})',
        yd,
        'Data generation cost',
        '--',
        2.5,
        '-',
    ),
    (
        'epochs',
        'Epochs',
        [10, 50, 100, 200, 500],
        lambda v: c_mt(N, e=v),
        lambda v: f'Training cost (Epochs={int(v)})',
        yd,
        'Data generation cost',
        '--',
        2.5,
        '-',
    ),
    (
        'datagen_flops',
        'FLOPS/cell/step',
        np.linspace(2e3, 1e4, 5),
        lambda v: c_dg(N, f=v),
        lambda v: f'Data gen cost ({int(v)} FLOPS)',
        yt,
        'Training cost (Fixed)',
        '-',
        3,
        '--',
    ),
    (
        'cells',
        'cells',
        np.linspace(1e8, 1e9, 5),
        lambda v: c_dg(N, c=v),
        lambda v: (
            f'Data gen cost ({v / 1e9:.1f}B cells)'
            if v >= 1e9
            else f'Data gen cost ({int(v / S)}M cells)'
        ),
        yt,
        'Training cost (Fixed)',
        '-',
        3,
        '--',
    ),
    (
        'timesteps',
        'timesteps',
        np.linspace(5e4, 5e5, 5),
        lambda v: c_dg(N, t=v),
        lambda v: f'Data gen cost ({int(v / 1000)}k Steps)',
        yt,
        'Training cost (Fixed)',
        '-',
        3,
        '--',
    ),
]

for nm, tit, vals, fn, lbl, fy, fl, fls, flw, vls in cfgs:
    fig, ax = plt.subplots()
    ax.plot(N / S, fy / S, label=fl, color=FX, ls=fls, lw=flw)
    for v, color in zip(vals, plt.cm.magma(np.linspace(0.2, 0.8, len(vals)))):
        ax.plot(N / S, fn(v) / S, label=lbl(v), color=color, linewidth=2.5, ls=vls)
    ax.set(
        xlabel='Sample size (millions)',
        ylabel='Cost ($ millions)',
        title=f'Cost vs. sample size (varying {tit})',
        yscale='log',
        ylim=(1, 1000),
        xlim=(0, 2),
    )
    ax.legend(loc='lower right')
    fig.tight_layout()
    fig.savefig(f'cost_analysis_{nm}.png', dpi=300)

plt.show()
