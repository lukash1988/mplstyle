# coding=utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler
from .base import PLTbase


class PLTdiss(PLTbase):
    """ PLTewk class, child of PLTbase"""

    _EWK_GGPLT = 'ewk_ggplt'
    _EWK = 'ewk'
    _ENERGY = 'energy'
    _SINGLE = 'single'
    _DOUBLE = 'double'

    def __init__(self):
        PLTbase.__init__(self)

        available_styles = {
            'color_style': [self._EWK_GGPLT, self._EWK,self._ENERGY],
            'color_order_style': [self._EWK_GGPLT, self._EWK],
            'plt_style': [self._EWK_GGPLT, self._EWK,self._DOUBLE,self._SINGLE]}

        self._add_available_styles(available_styles)

    def _get_colors(self, style):
        if style == self._EWK_GGPLT:
            return {
                'mdarkred': (187, 63, 63),
                'mediumred': (244, 54, 5),
                'lightred': (255, 177, 154),
                'darkgreen': (10, 72, 30),
                'mediumgreen': (82, 171, 82),
                'mlightgreen': (131, 191, 150),
                'lightgreen': (178, 213, 189),
                'darkblue': (1, 21, 62),
                'mediumblue': (100, 149, 237),
                'lightblue': (208, 227, 253),
                'darkred': (157, 2, 22),
                'black': (0, 0, 0),
                'darkgrey': (76, 76, 76),
                'mediumgrey': (127, 127, 127),
                'mlightgrey': (178, 178, 178),
            }
        elif style == self._EWK:
            return {
                'c0': '#1f77b4',
                'c1': '#ff7f0e',
                'c2': '#2ca02c',
                'c3': '#d62728',
                'c4': '#9467bd',
                'c5': '#8c564b',
                'c6': '#e377c2',
                'c7': '#7f7f7f',
                'c8': '#bcbd22',
                'c9': '#17becf'
            }
        elif style == self._ENERGY:
            return {
                u'Nutzenergie': (102,204,0),
                u'Endenergie': (255,153,51),
                u'Primärenergie': (102,102,0),
                u'Verluste1': (204,102,0),
                u'Verluste2': (204,0,0),
                u'Gewinne': (0,204,102),
                u'Hersteller': (100,149,237),
                'c3': '#d62728',
                'c4': '#9467bd',
                'c5': '#8c564b',
                'c6': '#e377c2',
                'c7': '#7f7f7f',
                'c8': '#bcbd22',
                'c9': '#17becf'
            }
        return None

    def _get_colors_order(self, style):

        if style == self._EWK_GGPLT:
            return ['mediumblue', 'mediumgreen', 'lightred', 'darkgreen',
                    'lightgreen','mediumblue',
                    'mdarkred', 'lightblue', 'darkred', 'black', 'darkgrey',
                    'mediumgrey', 'mlightgrey']
        elif style == self._EWK:
            return ['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9']
        return None

    def _set_plt_style(self, style, colors, prop_cycle_colors):

        if style == self._EWK_GGPLT:
            plt.style.use('ggplot')
            figsz = 12
            fntsz = 18
            lw = 2
            fntcol = 'dimgray'
            font = {'family': 'arial', 'weight': 'light', 'size': fntsz}
            mpl.rc('font', **font)
            mpl.rc('figure', figsize=(figsz, figsz / 1.8), titlesize=fntsz)
            mpl.rc('legend', framealpha=None, fancybox=True,
                   edgecolor=colors['mlightgrey'], fontsize=fntsz - 2,
                   numpoints=1, handlelength=1,
                   loc='best')
            mpl.rcParams['text.color'] = fntcol
            mpl.rc('axes', edgecolor='w', grid=True,
                   xmargin=0, labelsize=fntsz - 2, titlesize=fntsz)
            mpl.rc('grid', color='w', linestyle='-', linewidth=0.5)
            mpl.rc('lines', lw=lw, markersize=10)
            mpl.rc('xtick', color=fntcol, labelsize=fntsz - 2)
            mpl.rc('ytick', color=fntcol, labelsize=fntsz - 2)
            mpl.rcParams['axes.prop_cycle'] = cycler('color',
                                                     prop_cycle_colors)
            return True
        elif style == self._EWK:
            plt.style.use('default')
            fntsz = 10
            lw = 2
            fntcol = 'black'
            font = {'family': 'arial', 'weight': 'normal', 'size': fntsz}
            mpl.rc('font', **font)
            mpl.rc('figure', figsize=[6, 6], titlesize=fntsz)
            mpl.rc('legend', framealpha=None,
                   edgecolor='gainsboro',
                   fontsize=fntsz - 2, numpoints=1, handlelength=1,
                   loc='best', frameon=True, shadow=False,
                   fancybox=False)
            mpl.rcParams['text.color'] = fntcol
            mpl.rc('axes', edgecolor=fntcol, grid=True,
                   xmargin=0, labelsize=fntsz - 1, titlesize=fntsz,
                   linewidth=0.9)
            mpl.rcParams['axes.spines.right'] = False
            mpl.rcParams['axes.spines.top'] = False
            mpl.rc('grid', linestyle=':', color='darkgrey',
                   linewidth=0.5)
            mpl.rc('lines', lw=lw, markersize=10)
            mpl.rc('xtick', color=fntcol, labelsize=fntsz - 2)
            mpl.rc('ytick', color=fntcol, labelsize=fntsz - 2)
            # add default colors to first postion (default color order)
            mpl.rcParams['axes.prop_cycle'] = cycler('color',
                                                     prop_cycle_colors)
            return True
        elif style == self._SINGLE:
            plt.style.use('default')
            fntsz = 10
            lw = 2
            fntcol = 'black'
            font = {'family': 'arial', 'weight': 'normal', 'size': fntsz}
            mpl.rc('font', **font)
            mpl.rc('figure', figsize=[6, 3], titlesize=fntsz)
            mpl.rc('legend', framealpha=None,
                   edgecolor='grey',
                   fontsize=fntsz - 2, numpoints=1, handlelength=1,
                   loc='best', frameon=True, shadow=False,
                   fancybox=False)
            mpl.rcParams['text.color'] = fntcol
            mpl.rc('axes', edgecolor=fntcol, grid=True,
                   xmargin=0, labelsize=fntsz - 1, titlesize=fntsz,
                   linewidth=0.9)
            mpl.rcParams['axes.spines.right'] = False
            mpl.rcParams['axes.spines.top'] = False
            mpl.rc('grid', linestyle=':', color='darkgrey',
                   linewidth=0.5)
            mpl.rc('lines', lw=lw, markersize=5)
            mpl.rc('xtick', color=fntcol, labelsize=fntsz - 2)
            mpl.rc('ytick', color=fntcol, labelsize=fntsz - 2)
            # add default colors to first postion (default color order)
            mpl.rcParams['axes.prop_cycle'] = cycler('color',
                                                     prop_cycle_colors)
            return True
        elif style == self._DOUBLE:
            plt.style.use('default')
            fntsz = 10
            lw = 2
            fntcol = 'black'
            font = {'family': 'arial', 'weight': 'normal', 'size': fntsz}
            mpl.rc('font', **font)
            mpl.rc('figure', figsize=[6, 6], titlesize=fntsz)
            mpl.rc('legend', framealpha=None,
                   edgecolor='gainsboro',
                   fontsize=fntsz - 2, numpoints=1, handlelength=1,
                   loc='best', frameon=True, shadow=False,
                   fancybox=False)
            mpl.rcParams['text.color'] = fntcol
            mpl.rc('axes', edgecolor=fntcol, grid=True,
                   xmargin=0, labelsize=fntsz - 1, titlesize=fntsz,
                   linewidth=0.9)
            mpl.rcParams['axes.spines.right'] = False
            mpl.rcParams['axes.spines.top'] = False
            mpl.rc('grid', linestyle=':', color='darkgrey',
                   linewidth=0.5)
            mpl.rc('lines', lw=lw, markersize=10)
            mpl.rc('xtick', color=fntcol, labelsize=fntsz - 2)
            mpl.rc('ytick', color=fntcol, labelsize=fntsz - 2)
            # add default colors to first postion (default color order)
            mpl.rcParams['axes.prop_cycle'] = cycler('color',
                                                     prop_cycle_colors)
            return True
        return False
