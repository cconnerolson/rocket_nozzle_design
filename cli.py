import click
from isentropic_flow import *
from schomate_equation import specific_heat

print('\nUsage:')

print('  python3 cli.py <command>\n\n')

print('Tools:\n')


print('           Input arg:           Output arg:\n')

print('  -m2p  -  Mach number          Pressure Ratio')
print('  -m2t  -  Mach number          Temperature Ratio')
print('  -m2a  -  Mach number          Area Ratio')
print('  -p2m  -  Pressure Ratio       Mach Number')
print('  -p2t  -  Pressure Ratio       Temperature Ratio')
print('  -p2a  -  Pressure Ratio       Area Ratio')
print('  -t2m  -  Temperature Ratio    Mach Number')
print('  -t2p  -  Temperature Ratio    Pressure Ratio')
print('  -t2a  -  Temperature Ratio    Area Ratio')
print('  -a2m  -  Area Ratio           Mach Number')
print('  -a2p  -  Area Ratio           Pressure Ratio')
print('  -a2t  -  Area Ratio           Mach Number\n')

print('  -cp   -  Temperature          Specific Heat (Cp)')


''''print('Please select an option...\n')
print('    [1] - calculate specific heat')
print('    [2] - isentropic flow table conversions')
print('    [')'''


''''@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name",
              help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo("Hello, %s!" % name)

if __name__ == '__main__':
    hello()'''