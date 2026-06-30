import requests

try:
    url = 'https://pudim.com.br'
    repuesta = requests.get(url)
except:
    print(f'\n\033[91mLa pagina\033[0m \033[94m{url.upper()}\033[0m, \033[91mNO esta disponible\033[0m\n')
else:
    print(f'\n\033[92mLogre acceder a\033[0m \033[94m{url.upper()}\033[0m, \033[92mcon exito\033[0m\n')