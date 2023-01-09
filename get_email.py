import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    list = []
    for i in data['results']:
        list.append(i['email'])
    return list
data = get_data.get_data('randomuser_data.json')
print(get_email(data))