from app.config.api_consumption import api_url
import requests, time


def get_api_response():
    stack_overflow = requests.get(api_url)
    data_stack_overflow = stack_overflow.json()
    return data_stack_overflow


def answered_and_no():
    json = get_api_response()
    answers = {
        'answered': 0,
        'not_answered': 0,
    }
    for answer in json['items']:
        if answer['is_answered']:
            answers['answered'] += 1
        else:
            answers['not_answered'] += 1

    return answers


def greater_reputation():
    response = get_api_response()
    answers = response['items']
    answers.sort(key=lambda x: x['view_count'], reverse=True)

    return {
        'score': answers[0]['score'],
        'answer': answers[0],
    }


def less_views():
    response = get_api_response()
    answers = response['items']
    answers.sort(key=lambda x: x['view_count'])
    return {
        'answer': answers[0],
        'answer_views': answers[0]['view_count'],
    }


def old_and_recent():
    response = get_api_response()
    answers = response['items']
    answers.sort(key=lambda x: x['creation_date'])

    old_answer = answers[0]
    recent_answer = answers.pop()

    old_date = old_answer['creation_date']
    old_date_formatted = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(old_date))
    recent_date = recent_answer['creation_date']
    recent_date_formatted = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(recent_date))

    # return answers
    return {
        "old": {
            'creation_date': old_date_formatted,
            'answer': old_answer,
        },
        "recent": {
            'creation_date': recent_date_formatted,
            'answer': recent_answer,
        },
    }


def previous_services():
    return {
        'answered_and_no': answered_and_no(),
        'greater_reputation': greater_reputation(),
        'less_views': less_views(),
        'old_and_recent': old_and_recent(),
    }
