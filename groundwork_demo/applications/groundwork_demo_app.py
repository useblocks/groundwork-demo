import os
from groundwork import App


def start_app():
    app = App([os.path.join(os.path.dirname(__file__), "configuration.py")])
    app.plugins.activate(["GwWeb", "GwPluginsInfo", "GwDemoIntroduction", "GwWebManager"])
    app.commands.start_cli()


if "main" in __name__:
    start_app()