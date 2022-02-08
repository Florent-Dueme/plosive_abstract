import matplotlib.pyplot as plt
import seaborn


def graph_plosives(dataframe, lim_y=None, save=False):

    seaborn.set(style="ticks")

    multi_plot = seaborn.catplot(
        x="Task",
        y="Plosion_index",
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
    multi_plot.fig.set_size_inches(15, 12)
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
        multi_plot.savefig(fr"Plots\Bar plot.jpg")


def graph_groups_f(dataframe, lim_y=None, save=False):

    seaborn.set(style="ticks")

    multi_plot = seaborn.catplot(
        x="Task",
        y="Plosion_index",
        hue="Grapheme",
        hue_order=["b", "v"],
        col='Group',
        data=dataframe,
        kind="bar",
        order=["naming", "reading", "PW"],
        height=8,
        aspect=2,
        legend=False,
    )
    multi_plot.fig.set_size_inches(15, 12)
    multi_plot.set_ylabels("Plosion index", fontsize=14, weight="bold")
    multi_plot.set_xlabels("")
    multi_plot.set_xticklabels(
        ["Picture naming", "Word reading", "PW reading"], fontsize=14, weight="bold"
    )

    if lim_y:
        multi_plot.set(ylim=lim_y)

    multi_plot.fig.suptitle('French /b/ and /v/ by controls and bilinguals')

    plt.legend(loc=(0.92, 0.85), fontsize=14, prop={"weight": "bold"})

    # multi_plot.fig.text(0.7, -0.06,'Error Barrs: 95% Confidence Interval', fontsize=10)

    if save:
        multi_plot.savefig(fr"Plots\Bar plot French plosives by group.jpg")


def graph_groups_s(dataframe, lim_y=None, save=False):

    seaborn.set(style="ticks")

    multi_plot = seaborn.catplot(
        x="Task",
        y="Plosion_index",
        hue="Grapheme",
        hue_order=["b", "v"],
        col='Group',
        data=dataframe,
        kind="bar",
        order=["naming", "reading", "PW"],
        height=8,
        aspect=2,
        legend=False,
    )
    multi_plot.fig.set_size_inches(15, 12)
    multi_plot.set_ylabels("Plosion index", fontsize=14, weight="bold")
    multi_plot.set_xlabels("")
    multi_plot.set_xticklabels(
        ["Picture naming", "Word reading", "PW reading"], fontsize=14, weight="bold"
    )

    if lim_y:
        multi_plot.set(ylim=lim_y)

    multi_plot.fig.suptitle(
        'Spanish /b/-<b> and /b/-<v> by controls and bilinguals')

    plt.legend(loc=(0.92, 0.85), fontsize=14, prop={"weight": "bold"})

    # multi_plot.fig.text(0.7, -0.06,'Error Barrs: 95% Confidence Interval', fontsize=10)

    if save:
        multi_plot.savefig(fr"Plots\Bar plot Spanish b by group.jpg")


def violin_plosives(dataframe, lim_y=None, save=False):

    seaborn.set(style="ticks")

    multi_plot = seaborn.catplot(
        x="Group",
        y="Plosion_index",
        hue="Grapheme",
        hue_order=["b", "v"],
        # col='Speaker',
        data=dataframe,
        kind="violin",
        order=["Monolinguals", "Bilinguals"],
        height=8,
        aspect=2,
        legend=False,
    )
    multi_plot.fig.set_size_inches(15, 12)
    multi_plot.set_ylabels("Plosion index (log base 2)",
                           fontsize=14, weight="bold")
    multi_plot.set_xlabels("")
    multi_plot.set_xticklabels(
        ["Controls", "Bilinguals"], fontsize=14, weight="bold"
    )

    if lim_y:
        multi_plot.set(ylim=lim_y)

    multi_plot.fig.suptitle(
        'Spanish /b/-<b> and /b/-<v> by controls and bilingual participants', fontsize=22)

    plt.legend(loc=(0.92, 0.85), fontsize=14, prop={"weight": "bold"})

    # multi_plot.fig.text(0.7, -0.06,'Error Barrs: 95% Confidence Interval', fontsize=10)

    if save:
        multi_plot.savefig(fr"Plots\violin plot.jpg")


def violin_burst(dataframe, lim_y=None, save=False):

    seaborn.set(style="ticks")

    multi_plot = seaborn.catplot(
        x="Group",
        y="Plosion_index",
        hue="Grapheme",
        hue_order=["b", "v"],
        # col='Speaker',
        data=dataframe,
        kind="violin",
        order=["Monolinguals", "Bilinguals"],
        height=8,
        aspect=2,
        legend=False,
    )
    multi_plot.fig.set_size_inches(15, 12)
    multi_plot.set_ylabels("Plosion index (log base 2)",
                           fontsize=14, weight="bold")
    multi_plot.set_xlabels("")
    multi_plot.set_xticklabels(
        ["Controls", "Bilinguals"], fontsize=14, weight="bold"
    )

    if lim_y:
        multi_plot.set(ylim=lim_y)

    multi_plot.fig.suptitle(
        'Spanish /b/-<b> and /b/-<v> by controls and bilingual participants - burst tokens ony', fontsize=22)

    plt.legend(loc=(0.92, 0.85), fontsize=14, prop={"weight": "bold"})

    # multi_plot.fig.text(0.7, -0.06,'Error Barrs: 95% Confidence Interval', fontsize=10)

    if save:
        multi_plot.savefig(fr"Plots\violin plot burst data.jpg")
