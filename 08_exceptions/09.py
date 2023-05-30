import webbrowser
from urllib.error import URLError

def ensure_correct_start(url):
    return url.startswith('https://') or url.startswith('http://')

def ensure_correct_end(url):
    return url.endswith('.pl') or url.endswith('.com')

def get_url():
    url = input("Podaj url")

    if ensure_correct_start(url) and ensure_correct_end(url):
        return url
    elif url.startswith('www.'):
        return 'http://' + url
    else:
        raise URLError('URL w złym formacie')

def main():
    try:
        url = get_url()
        webbrowser.open(url)
    except URLError as err:
        print(err)

    print('Bye!')

if __name__ == '__main__':
    main()