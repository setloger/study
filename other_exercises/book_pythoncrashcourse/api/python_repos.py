import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


#1. Создание вызова API и сохранения ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

#Сохранение ответа API в переменной
response_dict = r.json()

#Обработка результатов
print(response_dict.keys())
print('Total repositories:', response_dict['total_count'])

#Анализ информации в репозиториях
repo_dicts = response_dict['items']

"""print('Repositories returned:', len(repo_dicts))

#Анализ первого репозитория
repo_dict = repo_dicts[0]
print('\nKeys:', len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

print('\n\n\tВывод информации')
for repo_dict in repo_dicts:
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])    
    print('Description:', repo_dict['description'])
    print('Language:', repo_dict['language'], '\n\n')


#2. Получаем ответ на лимит запросов
url = 'https://api.github.com/rate_limit'
r = requests.get(url)
print('Status code:', r.status_code)
response_dict = r.json()

#Обработка результатов
print(response_dict.keys())
print('First key in dict - :', response_dict['resources'], '\n\n')
print('Second key in dict:', response_dict['rate'], '\n\n')"""


names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

#Построение визуализации
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Наиболее рейтинговые проекты пайтон на Github'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
