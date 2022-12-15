import os
import json
import sys
def load(path: str = '/home/yagor/Рабочий стол/mipt/lab2/pyspark_tfidf/recomend_films.json'):
    with open(path) as json_file:
        data = json.load(json_file)
    return data

def predict(data: dict(), index: int=108171):
    try:
        similar_films = data[str(index)]
        return similar_films
    except:
        print('Films for this index films not defind')


if __name__ == '__main__':
    path = sys.argv[1]
    index_film = sys.argv[2]
    data = load(path)
    print(*predict(data, index_film))

