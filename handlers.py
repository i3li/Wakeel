class _Command(object):

    def __init__(self, name, params=[]):
        self.name = name
        self.params = params

    def __repr__(self):
        return ' '.join([self.name] + self.params)

    @staticmethod
    def parse(command_str):
        cmd = command_str.strip(' \n').lower().split()
        return _Command(cmd[0], cmd[1:]) if len(cmd) > 0 \
            else None


def _handle_list_files(params):
    # TODO: Implementation
    pass


_HANDLERS = {
    'list': _handle_list_files
}


def handle(command):
    cmd = _Command.parse(command)
    if cmd and cmd.name in _HANDLERS:
        _HANDLERS[cmd.name](cmd.params)


# def main():
#     handle('list p1 p2')
#
#
# if __name__ == '__main__':
#     main()
