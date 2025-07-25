import os

# версия пакета - дата, т.к. содержание типов очень сильно зависит
# от даты их генерации. Версия строится по формату:
# год.месяц.день
__version__ = open(os.path.join(os.path.dirname(__file__), 'version.txt')).read().strip()

if __name__ == '__main__':
    print(__version__)
