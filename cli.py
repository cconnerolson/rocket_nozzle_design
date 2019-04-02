import click
#from schomate_equation import specific_heat
from isentropic_flow import *


@click.command()
@click.option('--isentropic_flow', type=click.Choice(
		['m2p', 'm2t', 'm2a', 'p2m', 'p2t', 'p2a', 't2m', 't2p', 't2a', 'a2m', 'a2p', 'a2t']), hidden=True,
		prompt='Enter function... '
		)
def isentropic_flow(fn):
	click.echo(fn)






if __name__ == '__main__':
	isentropic_flow()

