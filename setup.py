from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), 'r', encoding = 'utf-8') as fh:
    long_description = fh.read()

version='0.1.0'
setup(
    name = 'jupyter-libertem-proxy',
    version = version,
    packages = find_packages(),

    url = 'https://github.com/jhgoebbert/jupyter-libertem-proxy',
    download_url = 'https://github.com/jhgoebbert/jupyter-libertem-proxy/archive/v{0}.tar.gz'.format(version),

    author = 'Jens Henrik Goebbert',
    author_email = 'j.goebbert@fz-juelich.de',

    description = 'LiberTEM for JupyterLab',
    long_description = long_description,
    long_description_content_type = 'text/markdown',

    keywords = ['jupyter', 'libertem', 'jupyterhub', 'jupyter-server-proxy'],
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Jupyter',
    ],

    entry_points = {
        'jupyter_serverproxy_servers': [
            'libertem = jupyter_libertem_proxy:setup_libertem',
        ]
    },
    install_requires = ['jupyter-server-proxy>=1.5.0'],
    include_package_data = True,
    zip_safe = False
)
