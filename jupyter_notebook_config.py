import getpass
import os


paraview = {
    'command': [
        os.getcwd() + "/node_modules/.bin/Visualizer",
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
