class RANSimulator:

    def __init__(self):
        self.ru_status = "DOWN"
        self.du_status = "DOWN"
        self.cu_status = "DOWN"

    def start_ru(self):
        self.ru_status = "UP"
        return "RU started"

    def start_du(self):
        self.du_status = "UP"
        return "DU started"

    def start_cu(self):
        self.cu_status = "UP"
        return "CU started"

    def get_status(self):
        return {
            "RU": self.ru_status,
            "DU": self.du_status,
            "CU": self.cu_status
        }


if __name__ == "__main__":

    ran = RANSimulator()

    print(ran.start_ru())
    print(ran.start_du())
    print(ran.start_cu())

    print("RAN Status:")
    print(ran.get_status())