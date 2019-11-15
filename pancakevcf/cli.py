from pancakevcf.VcfParse import *
from test.TestFunctions import *
import click

@click.command()
@click.option(
    '--inputfile', '-i',
    help='give it strelka a strelka file!',
)
@click.option(
    '--outputfile', '-o',
    help='give it outputfile!',
)
@click.option(
    '--sample', '-s',
    help='give it a sample',
)
@click.option('--testfile','-t', is_flag=True, help="Will print verbose messages.")
def main(inputfile,outputfile,sample):
    vp = VcfParse(inputfile)
    df = vp.main_parse(input_vcf=inputfile)
    print(df.shape)