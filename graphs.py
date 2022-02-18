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


def graph_sound_group(dataframe, lim_y=None, save=False):

    seaborn.set(style='ticks')

    plt.figure(figsize=(30, 30))

    multi_plot = seaborn.catplot(y='Plosion_index',
                                 col='Group', row='Language', col_order=['Bilinguals', 'Monolinguals'],
                                 data=dataframe, kind='box', height=8, aspect=2, legend=False, showfliers=False)
    multi_plot.fig.set_size_inches(8, 5)
    multi_plot.set_ylabels(
        'Plosion Index (log base 2)', fontsize=12, weight='bold')
    multi_plot.despine(left=True, bottom=True)

    for ax, title in zip(multi_plot.axes.flat, ['Bilinguals in French', 'French controls', 'Bilinguals in Spanish', 'Spanish controls']):
        ax.set_title(title)
        ax.yaxis.set_major_locator(plt.MaxNLocator(9))
        ax.tick_params(bottom=False, labelbottom=False)
        plt.grid(axis="y")

    plt.tight_layout()

    if lim_y:
        multi_plot.set(ylim=lim_y)

    # multi_plot.fig.suptitle('Bilinguals French [s] COG')

    # multi_plot.fig.text(0.7, -0.06,'Error Barrs: 95% Confidence Interval', fontsize=10)

    if save:
        multi_plot.savefig(fr'Plots\B across groups.jpg')


def box_PI(dataframe, lim_y=None, save=False):

    seaborn.set(style="ticks")

    multi_plot = seaborn.catplot(
        x="Language",
        y="Plosion_index",
        hue="Group",
        hue_order=["Monolinguals", "Bilinguals"],
        # col='Speaker',
        data=dataframe,
        kind="box",
        order=["Spanish", "French"],
        height=8,
        aspect=2,
        legend=False,
    )

    multi_plot.fig.set_size_inches(15, 12)
    multi_plot.set_ylabels("Plosion Index (log base 2)",
                           fontsize=14, weight="bold")
    multi_plot.set_xlabels("")
    multi_plot.set_xticklabels(
        ["Spanish", "French"], fontsize=14, weight="bold")

    for ax in multi_plot.axes.flat:
        ax.yaxis.set_major_locator(plt.MaxNLocator(23))
    plt.grid(axis="y")

    if lim_y:
        multi_plot.set(ylim=lim_y)

    multi_plot.fig.suptitle(
        "Fig 1. /b/-<b> Plosion index for French-Spanish bilinguals and controls",
        fontsize=23,
        y=1.01,
    )

    plt.legend(
        loc=(0.92, 0.85), fontsize=18, prop={"weight": "bold"}, title="Group",
    )

    # multi_plot.fig.text(0.7, -0.06,'Error Barrs: 95% Confidence Interval', fontsize=10)

    if save:
        multi_plot.savefig(fr"Plots\B box plot.jpg")
