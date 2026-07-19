class Uptime:

    def __init__(self, router):
        self.router = router

    def get(self):

        uptime = self.router.run(
            "cat /proc/uptime"
        ).split()[0]

        return float(uptime)