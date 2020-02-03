class _Command(object):

    def __init__(self, name, params=[]):
        self.name = name
        self.params = params

    def __repr__(self):
        return ' '.join([self.name] + self.params)

    @staticmethod
    def parse(command_str):
        cmd = command_str.strip(' \n').split()
        return _Command(cmd[0], cmd[1:]) if len(cmd) > 0 \
            else None


def handle(command):
    cmd = _Command.parse(command)
    # TODO: Handle the command
    print(cmd)


# def main():
#     handle('command p1    p2 p3  \n')
#
#
# if __name__ == '__main__':
#     main()
