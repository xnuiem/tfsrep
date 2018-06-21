import config
import os, inspect, sys

cmd_folder = os.path.abspath(os.path.join(os.path.split(inspect.getfile(
    inspect.currentframe()))[0], ".."))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from tfsrep import TFSReports

tfsr = TFSReports(config).generate_page()
