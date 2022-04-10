import unittest
from servey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey"""


    def test_store_single_responce(self):
        """Проверяет, что один ответ сохранен правильно."""
        ques = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(ques)
        my_survey.store_responce('English')

        self.assertIn('English', my_survey.responces)

    def test_store_three_responces(self):
        """Проверка на три ответа, что сохранены правильно."""
        ques = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(ques)
        responces = ['English', 'Spanish', 'Mandarin']
        for responce in responces:
            my_survey.store_responce(responce)

        for responce in responces:
            self.assertIn(responce, my_survey.responces)



unittest.main()


