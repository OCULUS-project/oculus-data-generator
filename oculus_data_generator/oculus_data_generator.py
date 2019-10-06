import sys


def oculus_data_generator(host: str, port: int) -> None:
    print('hello', host, port)


if __name__ == '__main__':
    oculus_data_generator(str(sys.argv[1]), int(sys.argv[2]))
