import requests


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
print('Repositories returned:', len(repo_dicts))

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
print('Second key in dict:', response_dict['rate'], '\n\n')