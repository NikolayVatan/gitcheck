import requests


def search(username):
    url = 'https://github.com/' + username
    r = requests.get(url)
    if r.status_code == 200:
        result = {

            'exists': True,
            'link': url
        }

    elif r.status_code == 404:
        result = {

            'exists': False,

        }
    else:
        return 'error, please try again'

    return result


if __name__ == '__main__':
    print(search('NikolayVatan'))
