import math
from typing import List

class CountVectorizer:
    """ Класс для подсчета количества слов в предложении"""

    def __init__(self):
        self.vocabulary = {}

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """Метод для подсчета слов в предложении
        :param corpus: входной корпус
        :type corpus: List[str]

        :rtype: List[List[int]]
        :return: матрица количества вхождений слов
        """
        line_in_corpus = len(corpus)
        words_in_corpus_orig = [x.lower().split() for x in corpus]

        all_low_words_in_corpus = []
        for line in range(len(words_in_corpus_orig)):
            for words in range(len(words_in_corpus_orig[line])):
                all_low_words_in_corpus.append(words_in_corpus_orig[line][words].lower())

        dict_words = list(dict.fromkeys(all_low_words_in_corpus))
        self.vocabulary = dict_words

        all_low_words_in_line = [
            [words_in_corpus_orig[line][words].lower()
             for words in range(len(words_in_corpus_orig[line]))] for line in range(line_in_corpus)]

        counter = []
        for line in range(len(all_low_words_in_line)):
            dict_counter = {k: 0 for k in dict_words}
            for word in all_low_words_in_line[line]:
                dict_counter[word] += 1
            counter.append(list(dict_counter.values()))
        return counter

    def get_feature_names(self):
        """Метод возвращает уникальный список слов из corpus"""
        return self.vocabulary

class TfidfTransformer:
    """Класс tf-idf transformer"""

    @staticmethod
    def tf_transform(count_matrix:  List[List[int]]) ->  List[List[float]]:
        """Функция считает частоту повторений слов в каждом предложении
        :param count_matrix: матрицы количества слов в предложении
        :type count_matrix: List[List[int]]

        :rtype: List[List[float]]
        :return: матрица частоты повторений слов
        """

        tf_matrix = []
        for line in range(len(count_matrix)):
            n = sum(count_matrix[line])
            vector = [round(element / n, 3) for element in count_matrix[line]]
            tf_matrix.append(vector)
        return tf_matrix

    @staticmethod
    def idf_transform(count_matrix:  List[List[int]]) -> List[float]:
        """Функция считает обратную частоту слов в каждом предложении
        :param count_matrix: матрицы количества слов в предложении
        :type count_matrix: List[List[int]]

        :rtype: List[float]
        :return: матрица idf слов
        """
        count_documents = len(count_matrix)
        count_words_in_doc = [0] * len(count_matrix[0]) #создали пустой массив для слов
        for i in range(len(count_matrix[0])):
            for line in count_matrix:
                if line[i] > 0:
                    count_words_in_doc[i] += 1
        idf_matrix = [
            round((math.log((count_documents + 1) / (document + 1)) + 1), 3) for document in count_words_in_doc
        ]
        return idf_matrix

    @staticmethod
    def tf_idf_transform(tf_matrix: List[List[float]], idf_matrix: List[float]) -> List[List[float]]:
        """Метод для создания tf-idf матрицы
        :param tf_matrix,  idf_matrix

        :rtype: List[List[float]]
        :return: матрица tf-idf слов
        """

        tf_idf = [ [ round( row_tf[row] * idf_matrix[row], 3) for row in range(len(idf_matrix))]
            for row_tf in tf_matrix ]
        return tf_idf

    def fit_transform(self, count_matrix: List[List[int]]) -> list:
        return self.tf_idf_transform(self.tf_transform(count_matrix), self.idf_transform(count_matrix))

class TfidfVectorizer(CountVectorizer):
    """Превращение корпуса в tf-idf матрицу"""

    def fit_transform( self, corpus: List[str]) -> List[List[float]]:
        "Метод для превращение корпуса в tf-idf матрицу"
        count_matrix = super().fit_transform(corpus)
        tf_idf_matrix = TfidfTransformer().fit_transform(count_matrix)
        return tf_idf_matrix

if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print('feature_names: ', vectorizer.get_feature_names())
    print('count_matrix: ', count_matrix)

    transformer = TfidfTransformer()
    tf_matrix = transformer.tf_transform(count_matrix)
    print('tf_matrix: ', tf_matrix)

    idf_matrix = transformer.idf_transform(count_matrix)
    print('idf_matrix: ', idf_matrix)

    tfidf_matrix = transformer.fit_transform(count_matrix)
    print('tfidf_matrix: ', tfidf_matrix)

    vectorizer2 = TfidfVectorizer()
    tfidf_matrix2 = vectorizer2.fit_transform(corpus)
    print('feature_names_vers2: ', vectorizer2.get_feature_names())
    print('tfidf_matrix2: ', tfidf_matrix2)
