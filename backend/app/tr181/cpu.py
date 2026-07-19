class CPU:

    def __init__(self, router):
        self.router = router

    def get(self):

        model = self.router.run(
            "cat /proc/cpuinfo | grep 'model name' | head -1 | cut -d ':' -f2"
        ).strip()

        cores = self.router.run(
            "nproc"
        ).strip()

        return {
            "Model": model,
            "Cores": int(cores)
        }