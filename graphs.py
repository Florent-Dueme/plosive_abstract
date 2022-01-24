import matplotlib.pyplot as plt
import seaborn


def graph_plosives(dataframe, lim_y=None, save=False):

    seaborn.set(style="ticks")

    multi_plot = seaborn.catplot(
        x="Task",
        y="Plosion index",
        hue="Grapheme",
        hue_order=["b", "v"],
        # col='Speaker',
        data=dataframe,
        kind="bar",
        order=["naming", "reading", "PW"],
        height=8,
        aspect=2,
        legend=False,
    )
    multi_plot.fig.set_size_inches(8, 5)
    multi_plot.set_ylabels("Plosion index", fontsize=14, weight="bold")
    multi_plot.set_xlabels("")
    multi_plot.set_xticklabels(
        ["Picture naming", "Word reading", "PW reading"], fontsize=14, weight="bold"
    )

    if lim_y:
        multi_plot.set(ylim=lim_y)

    # multi_plot.fig.suptitle('Bilinguals French [s] COG')

    plt.legend(loc=(0.92, 0.85), fontsize=14, prop={"weight": "bold"})

    # multi_plot.fig.text(0.7, -0.06,'Error Barrs: 95% Confidence Interval', fontsize=10)

    if save:
        multi_plot.savefig(fr"Plots\Bilinguals v data per language")
