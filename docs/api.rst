.. currentmodule:: mplstyle

.. _api:

API
========================
List of commands, which can be applied on initialized instance of the chosen class, is presented in the following.

.. function:: set_style(*args, **kwargs)
  
  Chooses style for **color**, **color order** and **plt style**. Arguments can be entered in two ways. First one assumes, that only a name of a style in the form of string is given. In this case all settings will be changed at one time. Second case allows to change a specific setting (**color**, **color order** and **plt style**) by putting a couple **setting='style'** as an argument. Two or three arguments are also possible in this case. Concept of inputs *args and **kwargs make it possible. More detailed explanation about nature of this concept is written `here`_.

  :param *args: name of the style;
  :param **kwargs: couple in the form setting='style'.

.. function:: get_colors()

  :return: dictionary of colors used in the chosen **color style**.

.. function:: get_color_order()

  :return: list of colors from the chosen **color order style** in order of appearance.

.. function:: get_available_styles()

  :return: all available styles for each plotting setting (**color**, **color order** and **plt style**).

.. function:: get_selected_style()

  :return: chosen style for **color**, **color order** and **plt style**.

.. function:: get_cmap(colors, position=None, bit=False)

  Generates custom color maps for Matplotlib. The method allows to create a list of tuples with 8-bit (0 to 255)
  or arithmetic (0.0 to 1.0) RGB values for making linear color maps. Color tuple placed first characterizes the
  lowest value of the color bar. The last tuple represents the the highest value.

  :param colors: list of RGB tuples with 8-bit (0 to 255) or arithmetic (0 to 1), default: arithmetic;
  :param position: list from 0 to 1, which dictates the location for each color;
  :param bit: boolean, default: False (arithmetic), True (RGB);

  :return: **cmap** - a color map with equally spaced colors.

  :Example1: cmap = mplstyle.get_cmap(colors=[(255, 0, 0), (0, 157, 0)], bit=True)

  :Example2: cmap = mplstyle.get_cmap([(1, 1, 1), (0.5, 0, 0)], position=[0, 1]))

.. function:: add_zbild(ax, x, y, text, tum=True, fontsize=10, color='grey')

  Sets ZBild number as a text in the chart.

  :param ax: instance of matplotlib axes;
  :param x: float for position (xmin=0, xmax=1);
  :param y: float for position (ymin=0, ymax=1);
  :param text: string for the text;
  :param tum: optional boolean for copyright, default: (tum=True);
  :param fontsize: optional float for font size, default: (10);
  :param color: optional string for mpl color, default: (grey).


.. _here: https://stackoverflow.com/questions/3394835/args-and-kwargs



