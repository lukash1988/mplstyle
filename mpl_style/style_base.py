import sys
import matplotlib as mpl
import numpy as np
from cycler import cycler


class PLTbase:
    """ Set own plot and color style."""

    _DEFAULT_COLOR_ORDER = ['darkblue', 'mdarkblue', 'mediumblue',
                            'mlightblue', 'lightblue', 'darkred', 'mdarkred',
                            'mediumred', 'mlightred', 'lightred', 'darkgreen',
                            'mdarkgreen', 'mediumgreen', 'mlightgreen',
                            'lightgreen', 'black', 'darkgrey', 'mediumgrey',
                            'mlightgrey', 'lightgrey']

    _DEFAULT_COLORS = {  # (R,G,B) tuples with range (0-255)
        'darkblue': (9, 30, 67),
        'mdarkblue': (21, 71, 157),
        'mediumblue': (53, 117, 227),
        'mlightblue': (143, 178, 240),
        'lightblue': (210, 224, 249),
        'darkred': (65, 12, 12),
        'mdarkred': (151, 28, 28),
        'mediumred': (219, 61, 61),
        'mlightred': (235, 147, 147),
        'lightred': (247, 212, 212),
        'darkgreen': (26, 51, 26),
        'mdarkgreen': (61, 118, 61),
        'mediumgreen': (83, 172, 83),
        'mlightgreen': (152, 205, 152),
        'lightgreen': (204, 229, 204),
        'black': (0, 0, 0),
        'darkgrey': (76, 76, 76),
        'mediumgrey': (127, 127, 127),
        'mlightgrey': (178, 178, 178),
        'lightgrey': (216, 216, 216),
    }

    def _set_default_plt_style(self):
        mpl.style.use('default')
        fntsz = 18
        lw = 2
        fntcol = 'black'
        font = {'family': 'arial', 'weight': 'normal', 'size': fntsz}
        mpl.rc('font', **font)
        mpl.rc('figure', figsize=[11, 7], titlesize=fntsz)
        mpl.rc('legend', framealpha=None,
               edgecolor='dimgray',
               fontsize=fntsz - 2, numpoints=1, handlelength=1,
               loc='best', frameon=True, shadow=False,
               fancybox=False)
        mpl.rcParams['text.color'] = fntcol
        mpl.rc('axes', edgecolor='black', grid=True,
               xmargin=0, labelsize=fntsz - 1, titlesize=fntsz, linewidth=0.9)
        mpl.rcParams['axes.spines.right'] = False
        mpl.rcParams['axes.spines.top'] = False
        mpl.rc('grid', linestyle=':', color='dimgray',
               linewidth=0.5)
        mpl.rc('lines', lw=lw, markersize=10)
        mpl.rc('xtick', color=fntcol, labelsize=fntsz - 2)
        mpl.rc('ytick', color=fntcol, labelsize=fntsz - 2)
        mpl.rcParams['axes.prop_cycle'] = cycler('color',
                                                 self._prop_cycle_colors)

    def __init__(self, plt_style='default', color_style='default',
                 color_order_style='default'):
        """ Set plot style, colors and color order.

        Args:
            plt_style: optional string for plt style; default: ('default')
            color_style: optional string for color order; default: ('default')
            color_order_style: optional string for color order style;
                                default: ('default')
        """
        self._color_style = color_style
        self._color_order_style = color_order_style
        self._plt_style = plt_style
        self._colors_order = None
        self._colors = None
        self._styles_available = {
            'color_style': ['default'],
            'color_order_style': ['default'],
            'plt_style': ['default']}
        self.set_style('default')

    def set_style(self, *args, **kwargs):
        """ Set plot style, colors and color order.

        Args:
            *args: optional string for the uniform style; i.e. non-key worded
                ('default')
            plt_style: optional string for plt style;
                (plt_style='default')
            color_style: optional string for color order;
                (color_style='default')
            color_order_style: optional string for color order style;
                    (color_order_style='default')
        """
        enable_color_order = False

        if len(args) > 1:
            raise ValueError('Only ONE or NO argument is allowed.')
        else:
            for arg in args:
                enable_color_order = self._set_all_style(arg)

        for k, v in kwargs.items():
            if k in self._styles_available.keys():
                setattr(self, '_{}'.format(k), v)
            else:
                raise NotImplementedError(
                    'Invalid style type: {}\n\n'
                    'Possible style types are: color_style, '
                    'color_order_style or plt_style.'.format(k))

        self._set_colors()

        if 'color_order_style' in kwargs.keys() or enable_color_order is True:
            self._set_color_order()
            self._check_color_consistence()
            self.__sort_colors_cycle()

        self._set_selected_plt_style()

    def get_colors(self):
        """ Get colors form chosen style.

        Returns:
            Dictionary of colors
        """
        return self._colors

    def get_color_order(self):
        """ Get ordered color list form chosen style.

        Returns:
            List of ordered colors
        """
        return self._colors_order

    def get_available_styles(self):
        """ Get available style.

        Returns:
            Nothing
        """

        print('Available styles for:\n')
        for i in self._styles_available.keys():
            print('\'{}\': {}\n'.format(i, self._styles_available[i]))

    def get_selected_style(self):
        """ Get selected style.

        Returns:
            Nothing
        """

        print('Selected style:\n \n'
              'plt_style: \'{}\'\n'
              'color_style: \'{}\'\n'
              'color_order_style: \'{}\'\n'.format(self._plt_style,
                                                   self._color_style,
                                                   self._color_order_style))

    def get_cmap(self, colors, position=None, bit=False):
        """ Generate custom color maps for Matplotlib.

        The method allows you to create a list of tuples with 8-bit (0 to 255)
        or arithmetic (0.0 to 1.0) RGB values to create linear color maps.
        Arrange your tuples so that the first color is the lowest value for
        the color bar and the last is the highest.

        Args:
            colors: list of RGB tuples with 8-bit (0 to 255) or
                    arithmetic (0 to 1); default: arithmetic
            position: contains a list from 0 to 1 to dictate the location
                      of each color
            bit: boolean; default: False (arithmetic); True (RGB)

        Returns:
            cmap: a color map with equally spaced colors

        Example:
            >>> cmap = get_cmap(colors=[(255, 0, 0), (0, 157, 0),)], bit=True)
            >>> cmap = get_cmap([(1, 1, 1), (0.5, 0, 0)], position=[0, 1]))
        """

        bit_rgb = np.linspace(0, 1, 256)
        if position is None:
            position = np.linspace(0, 1, len(colors))
        else:
            if len(position) != len(colors):
                sys.exit("position length must be the same as colors")
            elif position[0] != 0 or position[-1] != 1:
                sys.exit("position must start with 0 and end with 1")
        if bit:
            for i in range(len(colors)):
                colors[i] = (bit_rgb[colors[i][0]],
                             bit_rgb[colors[i][1]],
                             bit_rgb[colors[i][2]])
        cdict = {'red': [], 'green': [], 'blue': []}
        for pos, color in zip(position, colors):
            cdict['red'].append((pos, color[0], color[0]))
            cdict['green'].append((pos, color[1], color[1]))
            cdict['blue'].append((pos, color[2], color[2]))

        return mpl.colors.LinearSegmentedColormap('my_colormap', cdict, 256)

    def add_zbild(self, ax, xloc, yloc, zbild, tum=True, fontsize=10,
                  color='grey'):
        """ Set ZBild number as text in the chart.

        Args:
            ax: a matplotlib Axes instance
            xloc: float for position; ymin = 0, ymax = 1
            yloc: float for position; xmin = 0, xmax = 1
            zbild: string for text
            tum: optional boolean; for copyright; default: (tum=True)
            fontsize: optional float for font size; default: (10)
            color: optional string for mpl color; default: ('gray')
        """
        x_min = ax.get_xlim()[0]
        x_max = ax.get_xlim()[1]
        y_min = ax.get_ylim()[0]
        y_max = ax.get_ylim()[1]

        x = x_min + xloc * (x_max - x_min)
        y = y_min + yloc * (y_max - y_min)

        if tum is True:
            zbild = '$\copyright$ TUM IfE {}'.format(zbild)

        ax.text(x, y, zbild, fontsize=fontsize, color=color)

    def _set_all_style(self, all_style):
        """ Set same style for all options.

        Args:
            all_style: string for chosen style; default: ('default')
        """

        enable_color_order = self._check_style_consistence(all_style)

        if enable_color_order is True:
            self._color_style = all_style
            self._color_order_style = all_style
            self._plt_style = all_style

        else:
            self._color_style = all_style
            self._plt_style = all_style

        return enable_color_order

    def _set_color_order(self):
        if self._color_order_style == 'default':
            self._colors_order = self._DEFAULT_COLOR_ORDER
        else:
            self._colors_order = self._get_colors_order(
                self._color_order_style)
        if self._colors_order is None:
            raise NotImplementedError(
                'Color order style \'{}\' not defined'.format(
                    self._color_order_style))

    def _set_selected_plt_style(self):
        if self._plt_style == 'default':
            self._set_default_plt_style()
        else:
            success = self._set_plt_style(self._plt_style, self._colors,
                                          self._prop_cycle_colors)
            if not success:
                raise NotImplementedError(
                    'Plt style \'{}\' not defined'.format(self._plt_style))

    def _set_colors(self):
        if self._color_style == 'default':
            _colors = self._DEFAULT_COLORS.copy()
        else:
            _colors = self._get_colors(self._color_style).copy()
        if _colors is None:
            raise NotImplementedError(
                'Color style \'{}\' not defined'.format(self._color_style))

        self._colors = self._to_rgb_mpl(_colors)

    def _to_rgb_mpl(self, _colors):
        _to_rgb = lambda r, g, b: tuple(x / 255. for x in (r, g, b))
        for key, val in _colors.items():
            if isinstance(val, tuple):
                _colors[key] = _to_rgb(*val)
            else:
                _colors[key] = mpl.colors.to_rgb(val)
        return _colors

    def _check_color_consistence(self):
        colors = self._colors
        sort_order = self._colors_order
        for c in sort_order:
            if c not in colors:
                raise AttributeError(
                    'The color \'{}\' in the sort order style \'{}\''
                    ' is not defined in the colors style \'{}\''.format(
                        c, self._color_order_style, self._color_style))

    def __sort_colors_cycle(self):
        colors = self._colors
        sort_order = self._colors_order

        color_list = []
        for i, l in enumerate(sort_order):
            color_list.append(colors[l])

        self._prop_cycle_colors = color_list

    def _get_colors(self, style):
        return self._DEFAULT_COLORS

    def _get_colors_order(self, style):
        return self._DEFAULT_COLOR_ORDER

    def _set_plt_style(self, style, colors, prop_cycle_colors):
        self._set_default_plt_style()

    def _add_available_styles(self, available_styles=None):
        if available_styles is not None:
            styles = {}
            for i in self._styles_available.keys():
                try:
                    styles[i] = self._styles_available[i] + available_styles[i]
                except KeyError:
                    styles[i] = self._styles_available[i]

            self._styles_available = styles

    def _check_style_consistence(self, all_style):
        plt_style = set(self._styles_available['plt_style'])
        color_style = set(self._styles_available['color_style'])
        color_order_style = set(self._styles_available['color_order_style'])

        # check consistence for all options
        if set([all_style]).intersection(color_style, plt_style,
                                         color_order_style):
            enable_color_order = True
        # check consistence for color_style and plt_style
        elif set([all_style]).intersection(color_style, plt_style):
            enable_color_order = False
        else:
            raise AttributeError(
                'Selected style \'{}\' does not exist for plt_style'
                ' and color_style'.format(
                    all_style))
        return enable_color_order
