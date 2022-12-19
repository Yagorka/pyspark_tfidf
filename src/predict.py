import os
import json
import sys
def load(path: str = '/home/yagor/Рабочий стол/mipt/lab2/pyspark_tfidf/recomend_films.json'):
    with open(path) as json_file:
        data = json.load(json_file)
    return data

def predict(data_user_films: dict(), data_films: dict(), index_user: str='8'):
    try:
        similar_films = data_films[data_user_films[index_user]]
        return similar_films
    except:
        print('For this user films not defind')


if __name__ == '__main__':
    index_user = sys.argv[1]
    data_user_films = load('/home/yagor/Рабочий стол/mipt/lab2/pyspark_tfidf/user_and_recomend_films.json')
    data_films = load('/home/yagor/Рабочий стол/mipt/lab2/pyspark_tfidf/recomend_films.json')
    print(*predict(data_user_films, data_films, index_user))

