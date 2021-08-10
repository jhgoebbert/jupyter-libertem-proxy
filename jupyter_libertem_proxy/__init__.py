import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel('INFO')

HERE = os.path.dirname(os.path.abspath(__file__))

def _libertem_mappath(path):
    return path


def setup_libertem():
    """ Setup commands and and return a dictionary compatible
        with jupyter-server-proxy.
    """

    # create command
    cmd = [
        os.path.join(HERE, 'share/launch_libertem.sh'),
        'start',
        '--no-browser',
        '--port={port}',
    #   '--local-directory={dask_tmp}'.format(dask_tmp=),
    ]
    logger.info('LiberTEM command: ' + ' '.join(cmd))

    return {
        #'environment': {
        #    'XDG_RUNTIME_DIR': socket_path,
        #},
        'command': cmd,
        'mappath': _libertem_mappath,
        'absolute_url': False,
        'timeout': 90,
        'new_browser_tab': True,
        'launcher_entry': {
            'enabled': True,
            'icon_path': os.path.join(HERE, 'share/libertem-logo.svg'),
            'title': 'LiberTEM',
#            'urlfile': urlfile,
        },
    }
