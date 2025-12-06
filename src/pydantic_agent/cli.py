import asyncio

import typer

from .agent import run_agent

app = typer.Typer()


@app.command()
def run():
    response = asyncio.run(run_agent("What is the weather like in London and in Wiltshire?"))
    print("Response:", response)


def entrypoint():
    app()
