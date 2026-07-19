class Processor:

    def __init__(self, router):
        self.router = router

    def get(self):

        cpu = self.router.cpu()

        model = ""
        cores = 0

        for line in cpu.splitlines():

            if "model name" in line:
                model = line.split(":")[1].strip()

            if line.startswith("processor"):
                cores += 1

        return {
            "Model": model,
            "Cores": cores
        }