from abc import ABC, abstractmethod

class Enginee:
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
class Car(Enginee):
    def start(self):
        print("Start")

    def stop(self):
        print("Stop")

    def start_gearbox(self):
        print("Start gear box")

    def drive(self):
        self.start()
        self.start_gearbox()
        self.stop()

c = Car()
c.drive()


