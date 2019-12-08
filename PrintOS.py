import platform


def get_os():
    system = platform.system()
    return system


os = get_os()
print(os)
