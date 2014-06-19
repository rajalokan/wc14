# -*- coding: utf-8 -*-

'''
Created on 19-Jun-2014

@author: okan
'''




import click
import today
import current
import summary

@click.group()
def cli():
    pass

cli.add_command(today.today)
cli.add_command(current.current)
cli.add_command(summary.summary)
