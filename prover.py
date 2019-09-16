import requests


def search(username):
    url = 'https://github.com/' + username
    r = requests.get(url)
    if r.status_code == 200:
        result = {
            'Success!'
            'exists': True,
            'link': url
        }

    elif r.status_code == 404:
        result = {
            'Not Found! '
            'exists': False,

        }
    return result


if __name__ == '__main__':
    print(search('NikolayVatan'))
