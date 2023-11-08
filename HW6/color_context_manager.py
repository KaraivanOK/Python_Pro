from contextlib import contextmanager
from colorama import Fore


@contextmanager
def colorizer(color):
    color_dict = {'black': Fore.BLACK, 'red': Fore.RED, 'green': Fore.GREEN,
                  'yellow': Fore.YELLOW,
                  'blue': Fore.BLUE, 'magenta': Fore.MAGENTA, 'cyan': Fore.CYAN,
                  'white': Fore.WHITE}
    print(color_dict[color], end='')
    try:
        yield
    finally:
        print(Fore.RESET, end='')


color_list = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan',
              'white']
for color_text in color_list:
    with colorizer(color_text):
        print(f'printed in {color_text}')
    print('printed in default color')
