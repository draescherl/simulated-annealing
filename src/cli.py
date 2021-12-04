import re
from typing import Dict, List


def interpret_cli_args(argv: List[str]) -> Dict:
    # Looks for the --file=<filename> pattern.
    regex = re.compile('--file=\w*')
    # Return a list of all the matches. Should contain 0 or 1 elements.
    filename_list = list(filter(regex.match, argv))

    # If user hasn't inputed filename, exception will be raised.
    try:
        filename = filename_list[0].split('=')[1]
    except IndexError:
        filename = ''

    return {
        'help': '--help' in argv,
        'generate_gif': '--generate-gif' in argv,
        'show_result': '--show-result' in argv,
        'filename': filename
    }
