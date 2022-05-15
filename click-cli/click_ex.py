import click

@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)

    ctx.obj['DEBUG'] = debug
    ctx.obj['NETWORK'] = 'on'

@cli.command()
@click.pass_context
def sync(ctx):
    click.echo(ctx.obj) # prints entire context object that's passed in
    click.echo(ctx.parent.obj) # prints entire context object of parent (cli)
    click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))

if __name__ == '__main__':
    cli(obj={})