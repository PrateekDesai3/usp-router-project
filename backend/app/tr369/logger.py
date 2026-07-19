from datetime import datetime


class USPLogger:

    def log(self, operation):

        print(

            f"[{datetime.now()}] {operation}"

        )