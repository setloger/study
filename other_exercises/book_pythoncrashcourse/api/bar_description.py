from matplotlib import style
from matplotlib.pyplot import plot, show
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Проекты на питон'
chart.x_labels = ['httpie', 'django', 'flask']
plot_dicts = [
    {'value': 16101, 'label': 'Описание httpie'},
    {'value': 15028, 'label': 'Описание Django'},
    {'value': 14798, 'label': 'Описание Flask'}
]

chart.add('', plot_dicts)
chart.render_to_file('bar_description.svg')

