from datetime import datetime
import timedelta

FIXED_VALUE = 0.36
MINUTE_VALUE = 0.09
HOURS_CHARGE = tuple(range(6, 22))

# lista de dicionários identada para não ferir a PEP8
records = [
    {
        'source': '48-996355555',
        'destination': '48-666666666',
        'end': 1564610974,
        'start': 1564610674
    },
    {
        'source': '41-885633788',
        'destination': '41-886383097',
        'end': 1564506121,
        'start': 1564504821
    },
    {
        'source': '48-996383697',
        'destination': '41-886383097',
        'end': 1564630198,
        'start': 1564629838
    },
    {
        'source': '48-999999999',
        'destination': '41-885633788',
        'end': 1564697158,
        'start': 1564696258
    },
    {
        'source': '41-833333333',
        'destination': '41-885633788',
        'end': 1564707276,
        'start': 1564704317
    },
    {
        'source': '41-886383097',
        'destination': '48-996384099',
        'end': 1564505621,
        'start': 1564504821
    },
    {
        'source': '48-999999999',
        'destination': '48-996383697',
        'end': 1564505721,
        'start': 1564504821
    },
    {
        'source': '41-885633788',
        'destination': '48-996384099',
        'end': 1564505721,
        'start': 1564504821
    },
    {
        'source': '48-996355555',
        'destination': '48-996383697',
        'end': 1564505821,
        'start': 1564504821
    },
    {
        'source': '48-999999999',
        'destination': '41-886383097',
        'end': 1564610750,
        'start': 1564610150
    },
    {
        'source': '48-996383697',
        'destination': '41-885633788',
        'end': 1564505021,
        'start': 1564504821
    },
    {
        'source': '48-996383697',
        'destination': '41-885633788',
        'end': 1564627800,
        'start': 1564626000
    }
]


def classify_by_phone_number(records):
    '''
    Retorna uma lista de dicionários agrupada pele source e ordenada pelo total
    em ordem decrescente.
    '''
    records = sorted(records, key=lambda k: k['source'], reverse=True)
    records_group = []

    for i in range(len(records)):
        hour_start = convert_data(records[i]["start"])
        hour_end = convert_data(records[i]["end"])

        total = calculates_call_value(hour_start, hour_end)

        dict_aux = {'source': records[i]['source'], 'total': total}
        if i == 0:
            records_group.append(dict_aux)
        elif records[i]['source'] == records[i - 1]['source']:
            records_group[-1]['total'] += total
        else:
            records_group.append(dict_aux)

    return sorted(records_group, key=lambda k: k['total'], reverse=True)


def convert_data(data):
    return datetime.fromtimestamp(data)


def calculates_call_value(hour_start, hour_end):
    '''
    Retorna o valor da chamada telefônica
    '''
    total = FIXED_VALUE

    while hour_start <= (hour_end - timedelta(minutes=1)):
        if hour_start.hour in HOURS_CHARGE:
            total += MINUTE_VALUE

        hour_start += timedelta(minutes=1)

    return round(total, 2)
