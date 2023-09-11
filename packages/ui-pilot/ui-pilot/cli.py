import click



class State(object):
    def __init__(self, debug=False):
        self.debug = debug


@click.group()
@click.option('--debug/--no-debug', default=False, envvar='UIPILOT_DEBUG')
@click.pass_context
def cli(ctx, debug):
    ctx.obj = State(debug)


@cli.command()
@click.argument('name')
def start_session(name):
    print(name)
    pass


if __name__ == '__main__':
    cli()
