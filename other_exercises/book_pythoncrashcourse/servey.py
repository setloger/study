

class AnonymousSurvey():
    """Сбор анонимных ответов на опросы"""

    def __init__(self, ques):
        """Сохраняет вопрос и готовится к сохранению ответов"""
        self.ques = ques
        self.responces = []

    def show_question(self):
        """Выводит вопрос."""
        print(self.ques)
    
    def store_responce(self, new_responce):
        """Сохраняет один ответ на вопрос"""
        self.responces.append(new_responce)

    def show_results(self):
        """Выводит все полученные ответы."""
        print('Survey results:')
        for response in self.responces:
            print('- ' + response)

        
