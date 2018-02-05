import os
from IPython.lib import passwd

c.NotebookApp.ip = '*'
c.NotebookApp.port = int(os.getenv('PORT', 8888))
c.NotebookApp.open_browser = False

# sets a password if PASSWORD is set in the environment
DEFAULT_PASSWORD = 'test123'

password = os.environ.get('JUPYTER_PASSWORD', DEFAULT_PASSWORD)
c.NotebookApp.password = passwd(password)
