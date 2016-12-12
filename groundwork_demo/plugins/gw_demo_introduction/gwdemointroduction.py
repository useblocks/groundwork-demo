import os
from groundwork_web.patterns import GwWebPattern


class GwDemoIntroduction( GwWebPattern):
    def __init__(self, *args, **kwargs):
        self.name = self.__class__.__name__
        super().__init__(*args, **kwargs)

    def activate(self):
        self.web.contexts.register("gw",
                                   template_folder=os.path.join(os.path.dirname(__file__), "templates/"),
                                   static_folder=os.path.join(os.path.dirname(__file__), "static/"),
                                   url_prefix="/gw",
                                   description="Context for gw pages")

        self.web.routes.register("/", ["GET"], self.__introduction_view, context="gw")

    def __introduction_view(self):
        return self.web.render("introduction.html")


