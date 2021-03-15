from abc import ABCMeta
from abc import abstractmethod

# 抽象クラスvehicleの定義
class vehicle(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# vehicleを継承したクラスcarの定義
class car(vehicle):
    def start(self):
        print("car start.")

    def stop(self):
        print("car stop")


# vehicleを継承したクラスmotorcycleの定義
class motorcycle(vehicle):
    def start(self):
        print("moto start.")

    def stop(self):
        print("moto stop")


# テスト部
if __name__ == "__main__":
    mycar = car()
    mycar.start()
    mycar.stop()
