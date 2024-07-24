# src/processing.py

def filter_by_state(data, state='EXECUTED'):
    return [entry for entry in data if entry.get('state') == state]

def sort_by_date(data, reverse=True):
    return sorted(data, key=lambda x: x['date'], reverse=reverse)
