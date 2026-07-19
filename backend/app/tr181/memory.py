class Memory:

    def __init__(self, router):
        self.router = router

    def get(self):

        data = self.router.run("cat /proc/meminfo")

        result = {}

        for line in data.splitlines():

            if ":" in line:

                k, v = line.split(":", 1)

                result[k.strip()] = v.strip()

        return {
            "Total": result.get("MemTotal"),
            "Free": result.get("MemFree"),
            "Available": result.get("MemAvailable")
        }