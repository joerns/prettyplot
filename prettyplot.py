#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib as plt

BGCOLOR = (.90, .90, .90)
FONT_FAMILY = "Source Sans Pro"
FONT_SIZE = 9

def set_font():
    plt.rcParams["font.family"] = FONT_FAMILY
    plt.rcParams["font.size"] = FONT_SIZE


def horizontal_grid(ax):
    ax.set_axis_bgcolor(BGCOLOR)
    for loc in ("right", "top", "left"):
        ax.spines[loc].set_visible(False)
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.grid(True, color="white", ls='-', lw=2)
    [line.set_zorder(30) for line in ax.lines]


def position_labels(ax):
    ax.text(0, 1.01, ax.yaxis.label.get_text(), transform=ax.transAxes,
            va='bottom', ha='left', weight='normal', size=FONT_SIZE+1)
    ax.text(0, 1.01, ax.title.get_text()+'\n', transform=ax.transAxes,
            va='bottom', ha='left', weight='bold', size=FONT_SIZE+1)
    ax.set_xlabel(ax.xaxis.label.get_text(), position=(1,0),
                  ha='right', size=FONT_SIZE+1)
    ax.set_ylabel('')
    ax.set_title("")


def set_linestyle(ax):
    for line in ax.lines:
        line.set_marker('o')
        line.set_markersize(3)
        line.set_markeredgewidth(0)
        line.set_linewidth(1.4)
        line.set_alpha(0.6)


def config_plot(ax):
    set_font()
    horizontal_grid(ax)
    position_labels(ax)
    set_linestyle(ax)


def natural_log2_xaxis(ax, ticks):
    ax.set_xscale("log", base=2)
    ax.set_xticks(ticks)
    ticks = ax.get_xticks()
    labels = [item.get_text() for item in ax.get_xticklabels()]
    for i, (t, l) in enumerate(zip(ticks, labels)):
        if   t // (1024**3) >= 1:
            labels[i] = str(t//(1024**3))+'G'
        elif t // (1024**2) >= 1:
            labels[i] = str(t//(1024**2))+'M'
        elif t // (1024**1) >= 1:
            labels[i] = str(t//(1024**1))+'k'
        else: labels[i] = str(t)
    ax.minorticks_off()
    ax.set_xticklabels(labels, ha='center', rotation=45.0)
