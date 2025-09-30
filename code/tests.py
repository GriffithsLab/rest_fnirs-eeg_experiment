
"""
Run experiment script
"""

from eegnb.experiments.rest.eoec import RestEyesOpenCloseAlternating

exp = RestEyesOpenCloseAlternating()

exp.duration = 20

exp.use_fullscr = False

exp.run()


