![build](https://github.com/jhgoebbert/jupyter-libertem-proxy/workflows/build/badge.svg)

# jupyter-libertem-proxy
Integrates [LiberTEM](https://libertem.github.io/LiberTEM/index.html) in your Jupyter environment.  

## Requirements
- Python 3.6+
- Jupyter Notebook 6.0+
- JupyterLab 2.1+

This package executes the `libertem-server` command. This command assumes the `libertem-server` command is available in the environment's $PATH. You might need to adjust the file [launch_libertem.sh](jupyter_libertem_proxy/share/launch_libertem.sh) to ensure this.

## Security
[LiberTEM](https://libertem.github.io/LiberTEM/index.html) is started without the need for authentication. Everyone who has access to the system's local ports has unlimited access to a running LiberTEM platform. Be aware of that!

### LiberTEM
[LiberTEM](https://libertem.github.io/LiberTEM/index.html) is an open source platform for high-throughput distributed processing of large-scale binary data sets and live data streams using a modified MapReduce programming model.
The current focus is pixelated scanning transmission electron microscopy (STEM) and scanning electron beam diffraction data.

### Jupyter-Server-Proxy
[Jupyter-Server-Proxy](https://jupyter-server-proxy.readthedocs.io) lets you run arbitrary external processes (such as LiberTEM) alongside your notebook, and provide web access to them.

## Install 

#### Create and Activate Environment
```
virtualenv -p python3 venv
source venv/bin/activate
```

#### Install jupyter-libertem-proxy
```
pip install git+https://github.com/jhgoebbert/jupyter-libertem-proxy.git
```

#### Enable jupyter-libertem-proxy Extensions
For Jupyter Classic, activate the jupyter-server-proxy extension:
```
jupyter serverextension enable --sys-prefix jupyter_server_proxy
```

For Jupyter Lab, install the @jupyterlab/server-proxy extension:
```
jupyter labextension install @jupyterlab/server-proxy
jupyter lab build
```

#### Start Jupyter Classic or Jupyter Lab
Click on the LiberTEM icon from the Jupyter Lab Launcher or the LiberTEM item from the new dropdown in Jupyter Classic.  
Connect to your database as instructed in the Quickstart section.

## Configuration
This package calls `libertem-server`. Please read the [LiberTEM manual](https://libertem.github.io/LiberTEM/index.html) if you want to now the details.  
You have to modify `setup_libertem()` in `jupyter_libertem_proxy/__init__.py` for change.

## Credits
- LiberTEM
- jupyter-server-proxy

## License
BSD 3-Clause
