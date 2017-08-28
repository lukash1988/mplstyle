.. currentmodule:: mpl-style

.. _create:

How to Create
========================
Current section explains the procedure of creating your own class, where all desired styles for each plot setting (**color style**, **color order style**, **plt style**) will be stored. Mentioned before **PLTtz** class is taken as an example. Its script in the ``tz.py`` is explained below. 

tz.py
"""""""""""""""""""""""
::

    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from cycler import cycler
    from .base import PLTbase
    
Four packages are included: 

* `matplotlib`_ is a plotting library which allows present results in a diagram form quite easily;
* `matplotlib.pyplot`_ is a specified module of matplotlib;
* `cycler`_ is the composable style cycles;
* `.base` is the file, where fundamental class **PLTbase** is described.

::

    class PLTtz(PLTbase):
      #PLTtz class, child of PLTbase#

      _BLUE = 'blue'
      _JUPYTER_NOTEBOOK = 'jupyter-notebook'
      _MPL_V2 = 'mpl2_colors'
      
Gives the name to the new class mentioning in brackets the so-called "father". Then links user-friendly names of all available styles stored inside this class with formal ones used in the script.

::

    def __init__(self):
        PLTbase.__init__(self)

        available_styles = {
            'color_style': [self._BLUE, self._MPL_V2],
            'color_order_style': [self._BLUE, self._MPL_V2],
            'plt_style': [self._JUPYTER_NOTEBOOK]}

        self._add_available_styles(available_styles)
        
Function, which connects each plotting setting (**color style**, **color order style** and **plt style**) with corresponding list of available styles. 

::

    def _get_colors(self, style):
        if style == self._BLUE:
            return {
                'darkblue': (11, 85, 159),
                'mdarkblue': (42, 122, 185),
                'mediumblue': (83, 157, 204),
                'mlightblue': (136, 190, 220),
                'lightblue': (186, 214, 234),
                'pastelblue': (218, 232, 245),
            }
        if style == self._MPL_V2:
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
        return None
        
Function, which is responsible for **color style** plot setting. Keeps available colors for corresponding style. Style **blue** uses RGB codes for identification, **mpl2_colors** - HEX codes. 

::

    def _get_colors_order(self, style):
        if style == self._BLUE:
            return ['darkblue', 'mdarkblue', 'mediumblue', 'mlightblue',
                    'lightblue', 'pastelblue']
        elif style == self._MPL_V2:
            return ['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9']
        return None

Current function regulates **color order style** setting. Orders corresponding colors in dependence on style.

::

    def _set_plt_style(self, style, colors, prop_cycle_colors):
        if style == self._JUPYTER_NOTEBOOK:
            plt.style.use('default')
            fntsz = 12
            lw = 2
            fntcol = 'black'
            font = {'family': 'arial', 'weight': 'normal', 'size': fntsz}
            mpl.rc('font', **font)
            mpl.rc('figure', titlesize=fntsz)
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
            mpl.rc('grid', linestyle='-', color='darkgrey',
                   linewidth=0.5, alpha=0.35)
            mpl.rc('lines', lw=lw, markersize=10)
            mpl.rc('xtick', color=fntcol, labelsize=fntsz - 2)
            mpl.rc('ytick', color=fntcol, labelsize=fntsz - 2)
            mpl.rcParams['axes.prop_cycle'] = cycler('color',
                                                     prop_cycle_colors)
            return True
        return False

These strings control **plt style** setting. All terms (font of the text, fontsize, legend, ticks on the axes, etc.), which form the view of the plot, are described here.  








.. _matplotlib.pyplot: https://matplotlib.org/api/pyplot_summary.html
.. _matplotlib: https://matplotlib.org/index.html
.. _cycler: http://matplotlib.org/cycler/

