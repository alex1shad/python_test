import pytest


def geo_logs_func(geo_logs):
    i = 0
    while i < len(geo_logs):
        if 'Россия' not in list(*geo_logs[i].values()):
            del geo_logs[i]
            i -= 1
        i += 1
    return geo_logs


def ids_func(ids):
    total_list = []
    for user in ids.values():
        for el in user:
            if el not in total_list:
                total_list.append(el)
    return total_list


def queries_func(queries):
    dict_queries = {}
    dict_final = {}
    for query in queries:
        counter = query.strip().count(' ') + 1
        if counter not in dict_queries.keys():
            dict_queries[counter] = 1
        else:
            dict_queries[counter] = dict_queries[counter] + 1
    for key, value in dict_queries.items():
        if str(key)[-1] == '1':
            word = 'слово'
        elif str(key)[-1] in ['5', '6', '7', '8', '9', '0']:
            word = 'слов'
        else:
            word = 'слова'
        dict_final[f'{key} {word}'] = f'{int(value/sum(dict_queries.values())*100)} %'
    return dict_final


@pytest.mark.parametrize('geo_logs, geo_logs_true',
    [([
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ],
    [
        {'visit1': ['Москва', 'Россия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]),
    ([
         {'visit3': ['Владимир', 'Россия']},
         {'visit4': ['Лиссабон', 'Португалия']},
         {'visit5': ['Париж', 'Франция']},
         {'visit6': ['Лиссабон', 'Португалия']},
         {'visit7': ['Тула', 'Россия']},
         {'visit8': ['Тула', 'Россия']},
         {'visit9': ['Курск', 'Россия']},
         {'visit10': ['Архангельск', 'Россия']}
     ],
     [
         {'visit3': ['Владимир', 'Россия']},
         {'visit7': ['Тула', 'Россия']},
         {'visit8': ['Тула', 'Россия']},
         {'visit9': ['Курск', 'Россия']},
         {'visit10': ['Архангельск', 'Россия']}
     ])
    ])
def test_1(geo_logs, geo_logs_true):
    assert geo_logs_func(geo_logs) == geo_logs_true


@pytest.mark.parametrize('ids, ids_true',
    [({
        'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35]
        },
        [213, 15, 54, 119, 98, 35]),
        ({
        'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35, 168]
         },
         [213, 15, 54, 119, 98, 35, 168])
    ])
def test_2(ids, ids_true):
    assert ids_func(ids) == ids_true


@pytest.mark.parametrize('queries, queries_true',
    [([
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
        ],
        {'3 слова': '57 %', '2 слова': '42 %'}),
        ([
        'смотреть онлайн',
        'новости',
        'афиша кино',
        'курс',
        'сериалы этим летом',
        'курс по питону и джаве',
        'сериалы про спорт'
        ],
        {'2 слова': '28 %', '1 слово': '28 %', '3 слова': '28 %', '5 слов': '14 %'})
    ])
def test_3(queries, queries_true):
    assert queries_func(queries) == queries_true
