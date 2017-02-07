#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib as plt

BGCOLOR = (.90, .90, .90)
FONT_FAMILY = "Source Sans Pro"
FONT_SIZE = 9


def set_font():
    """Sets a good font and font size.

    By default 'Source Sans Pro' is used. The font needs to be installed. If
    the font is not picked up, try deleting the matplotlib font cache
    ($HOME/.cache/matplotlib/fontList.py3k.cache) and restart the python
    interpreter.
    """

    plt.rcParams["font.family"] = FONT_FAMILY
    plt.rcParams["font.size"] = FONT_SIZE


def horizontal_grid(ax):
    """Add a horizontal grid.

    Grid lines are white, and the background is set to a light gray. This way
    the grid lines are in the background and do not interfere with plot lines.
    """

    ax.set_axis_bgcolor(BGCOLOR)
    for loc in ("right", "top", "left"):
        ax.spines[loc].set_visible(False)
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.grid(True, color="white", ls='-', lw=2)
    [line.set_zorder(30) for line in ax.lines]


def position_labels(ax):
    """Position labels horizontally.

    The x-label will be positioned on the right side of the x-axis.
    The y-label will be positioned on top of the plot, below the title. Unlike
    the default matplotlib label, the y-label will be printed horizontally.
    The title will be positioned on top of the y-label in a bold font.
    """

    ax.text(0, 1.01, ax.yaxis.label.get_text(), transform=ax.transAxes,
            va='bottom', ha='left', weight='normal', size=FONT_SIZE+1)
    ax.text(0, 1.01, ax.title.get_text()+'\n', transform=ax.transAxes,
            va='bottom', ha='left', weight='bold', size=FONT_SIZE+1)
    ax.set_xlabel(ax.xaxis.label.get_text(), position=(1, 0),
                  ha='right', size=FONT_SIZE+1)
    ax.set_ylabel('')
    ax.set_title("")


def set_linestyle(ax):
    """Set styles for plot lines.

    This adjusts marker, width, and alpha channel of plot lines.
    """
    for line in ax.lines:
        line.set_marker('o')
        line.set_markersize(3)
        line.set_markeredgewidth(0)
        line.set_linewidth(1.4)
        line.set_alpha(0.6)


def config_plot(ax):
    """Configure multiple parameters of a plot.

    This will call set_font, horizontal_grid, position_labels, and set_linestyle.
    """

    set_font()
    horizontal_grid(ax)
    position_labels(ax)
    set_linestyle(ax)


def natural_log2_xaxis(ax, ticks):
    """Natural labels for a logarithmic x-axis with base 2.

    This will set natural x-axis labels with suffixes 'k', 'M', 'G', etc.
    """

    ax.set_xscale("log", base=2)
    ax.set_xticks(ticks)
    ticks = ax.get_xticks()
    labels = [item.get_text() for item in ax.get_xticklabels()]
    for i, (t, l) in enumerate(zip(ticks, labels)):
        if t // (1024**3) >= 1:
            labels[i] = str(t//(1024**3))+'G'
        elif t // (1024**2) >= 1:
            labels[i] = str(t//(1024**2))+'M'
        elif t // (1024**1) >= 1:
            labels[i] = str(t//(1024**1))+'k'
        else:
            labels[i] = str(t)
    ax.minorticks_off()
    ax.set_xticklabels(labels, ha='center', rotation=45.0)
