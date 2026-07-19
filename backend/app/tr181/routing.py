class Routing:

    def __init__(self, router):
        self.router = router

    def get(self):

        routes = self.router.routes()

        return {
            "Routes": routes.splitlines()
        }