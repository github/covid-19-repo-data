import setuptools

setuptools.setup(
  name="jupyter-datsette-server",
  # py_modules rather than packages, since we only have 1 file
  py_modules=['nbdatasette'],
  entry_points={
      'jupyter_serverproxy_servers': [
          #path = module:entry_function
          'datasette = nbdatasette:setup_datasette',
      ]
  },
)