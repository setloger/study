from urllib import response
import requests
from operator import itemgetter


# Создание вызова API и сохранение ответа
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status code:', r.status_code)

#Обработка информации о каждой статье
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Создание отдельного вызова API для каждой статьи
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
            str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0) 
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts,
                    key=itemgetter('comments'),
                                reverse=True)
for submission_dict in submission_dicts:
    print('\nЗаголовок:', submission_dict['title'])
    print('Ссылка на дисскуссию:', submission_dict['link'])
    print('Комментарии:', submission_dict['comments'])
    
