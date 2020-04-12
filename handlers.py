import utils
from pathlib import Path
import subprocess


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


def _respond(response, res_path):
    with open(res_path, 'w') as f:
        f.write(response)


def _error(desc):
    return f'Error: {desc}'


def _handle_list_files(params):
    root = Path.home().joinpath('Desktop')
    if len(params) > 0 and Path(params[0]).is_dir():
        root = Path(params[0])
    res = f'List of files rooted at {root} :-\n'
    return res + '\n'.join([line for line in utils.tree(root)])


def _handle_execute_shell(params):
    if len(params) == 0:
        return 'Please pass a command to execute'
    command = ' '.join(params)
    exec_result = subprocess.run(
                    command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True
                    )

    stdout_output = '\n'.join(
                            map(
                                lambda l: '\t' + l,
                                exec_result.stdout.decode(
                                        encoding='utf8'
                                        ).split('\n')
                                )
                            )
    stderr_output = '\n'.join(
                            map(
                                lambda l: '\t' + l,
                                exec_result.stderr.decode(
                                        encoding='utf8'
                                        ).split('\n')
                                )
                            )
    blocks = [
        f'Command:\n\t{command}',
        (
            f'Return Code:\n\t'
            f"{exec_result.returncode}"
            f" => {'Success' if exec_result.returncode == 0 else 'Failure'}"
        ),
        f'Stdout:\n{stdout_output}',
        f'Stderr:\n{stderr_output}'
    ]

    res = '\n\n'.join(blocks)
    return res


_HANDLERS = {
    'list': _handle_list_files,
    'shell': _handle_execute_shell
}


def handle(command, res_path):
    """Handles a command."""
    cmd = _Command.parse(command)
    if cmd:
        if cmd.name in _HANDLERS:
            res = _HANDLERS[cmd.name](cmd.params)
        else:
            res = 'Command not supported'
    else:
        res = 'Bad formatted command'
    _respond(res, res_path)


# def main():
#     handle('list p1 p2', '.')
#
#
# if __name__ == '__main__':
#     main()
