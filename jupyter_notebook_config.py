import getpass
import os


paraview = {
    'command': [
        'Visualizer',
        '--port', '{port}',
        '--server-only',
        '--paraview', 'paraview',
        '--data', os.getcwd()
    ],
    'timeout': 10
}

c.ServerProxy.servers = {
    'paraview': paraview,
}
