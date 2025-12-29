import queue
import requests
import threading
import sys

AGENT = "Mozilla/5.0 (X11: Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
EXTENSIONS = ['.php', '.bak', '.orig', '.inc']
TARGET = 'http://testphp.vulnweb.com'
THREADS = 10
WORD_LIST = '/Users/martinbullman/Downloads/SVNDigger-master/SVNDigger/all.txt'

def get_words(resume = None):
    def extend_words(word):
        if '.' in word:
            words.put(f'/{word}')
        else:
            words.put(f'/{word}/')

        for extension in EXTENSIONS:
            words.put(f'/{word}{extension}')
    
    with open(WORD_LIST) as f:
        raw_words = f.read()
    
    found_resume = False
    words = queue.Queue()

    for word in raw_words.split():
        if resume and not None:
            if found_resume:
                extend_words(word)
            elif word == resume:
                found_resume = True
                print(f'Resuming from: {resume}')
        else:
            print(word)
            extend_words(word)

    return words

def dir_bruter(words):
    headers = {'User-Agent': AGENT}

    while not words.empty():
        word = words.get()
        url = f'{TARGET}{word}'

        try:
            r = requests.get(url, headers = headers)
        except requests.exceptions.ConnectionError:
            sys.stderr.write('x');sys.stderr.flush()
            continue

        if r.status_code == 200:
            print(f'Success: ({r.status_code}: {url})')
        elif r.status_code == 404:
            sys.stderr.write('');sys.stderr.flush()
        else:
            print(f'{r.status_code} => {url}')


if __name__ == '__main__':
    words = get_words()

    print('Press return to continue...')
    sys.stdin.readline()
    
    for _ in range(THREADS):
        t = threading.Thread(target = dir_bruter, args = (words,))
        t.start()

