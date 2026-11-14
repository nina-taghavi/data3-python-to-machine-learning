"""Bar chart comparing target vs calculated snoring distribution by sleep phase.

Usage:
    python report.py                 # show the chart
    python report.py --save out.png  # save it instead

Note: the target values (68 + 13 + 11) sum to 92%, while the calculated values
(74 + 14 + 12) sum to 100%. Both are plotted as given; the script prints a
warning when a series does not sum to 100%.
"""

import argparse

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

PHASES = ["N2 (light)", "N3 (deep)", "REM"]
TARGET_PCT = [68, 13, 11]
CALCULATED_PCT = [74, 14, 12]

COLOR_TARGET = "#3f51b5"      # deep blue
COLOR_CALCULATED = "#ff9800"  # orange
BAR_WIDTH = 0.35


def build_data() -> pd.DataFrame:
    df = pd.DataFrame(
        {"Target": TARGET_PCT, "Calculated": CALCULATED_PCT},
        index=pd.Index(PHASES, name="Sleep phase"),
    )
    for column, total in df.sum().items():
        if total != 100:
            print(f"Warning: {column} values sum to {total}%, not 100%.")
    return df


def plot(df: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(df))

    bars_target = ax.bar(x - BAR_WIDTH / 2, df["Target"], BAR_WIDTH,
                         label="Target distribution", color=COLOR_TARGET)
    bars_calc = ax.bar(x + BAR_WIDTH / 2, df["Calculated"], BAR_WIDTH,
                       label="Calculated distribution", color=COLOR_CALCULATED)

    # Percentage label above each bar
    for bars in (bars_target, bars_calc):
        ax.bar_label(bars, fmt="%.0f%%", padding=3, fontsize=10)

    ax.set_xticks(x, df.index)
    ax.set_xlabel("Sleep phase", fontsize=12, labelpad=10)
    ax.set_ylabel("Share of total snoring time (%)", fontsize=12, labelpad=10)
    ax.set_title("Snoring Distribution by Sleep Phase: Target vs Calculated",
                 fontsize=14, pad=20)
    ax.set_ylim(0, df.to_numpy().max() * 1.15)  # headroom for the labels
    ax.grid(axis="y", linestyle="--", alpha=0.6)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper right")

    fig.tight_layout()
    return fig


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--save", metavar="PATH",
                        help="save the chart to PATH instead of showing it")
    args = parser.parse_args()

    fig = plot(build_data())
    if args.save:
        fig.savefig(args.save, dpi=150)
        print(f"Saved chart to {args.save}")
    else:
        plt.show()


if __name__ == "__main__":
    main()
