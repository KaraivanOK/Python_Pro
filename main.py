import requests


def parse(query: str) -> dict:
    response = requests.get(query)
    return response.json()


if __name__ == '__main__':
    assert parse('http://127.0.0.1:5000/?name=ferret&color=purple') == {
        'name': 'ferret', 'color': 'purple'}
    assert parse('http://127.0.0.1:5000/?name=ferret&color=purple&') == {
        'name': 'ferret', 'color': 'purple'}
    assert parse('http://127.0.0.1:5000?') == {}
    assert parse('http://127.0.0.1:5000?') == {}
    assert parse('http://127.0.0.1:5000?name=Dima') == {'name': 'Dima'}
    assert parse('http://127.0.0.1:5000?name=Dima') == {'name': 'Dima'}
    assert parse('http://127.0.0.1:5000?name=Dima&age=28') == {'name': 'Dima',
                                                               'age': '28'}
    assert parse('http://127.0.0.1:5000?name=Dima&age=28') == {'name': 'Dima',
                                                               'age': '28'}
    assert parse('http://127.0.0.1:5000?name=Dima=User&age=28') == {
        'name': 'Dima=User', 'age': '28'}
    assert parse('http://127.0.0.1:5000?name=Dima=User&age=28') == {
        'name': 'Dima=User', 'age': '28'}



