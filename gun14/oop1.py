# -*- coding: utf-8 -*-
"""

"""

class Bilgisayar:
    def __init__(self, marka, model, cpu, ram_size, fiyat):
        self.marka = marka  # public
        self._model = model  # protected
        self.__cpu = cpu  # private

    def set_cpu(self, cpu_model):
        # TODO: CPU modeline gore fiyati guncelle
        pass

    cpu = property(None, set_cpu, None, None)

    def __str__(self):
        return f"{self.marka} {self._model} {self.__cpu}"

def main():
    pc1 = Bilgisayar("Fujitsu-Siemens", "x320", "i5", 8, 4000)
    print(pc1)

    pc1.marka = "Lenovo"
    pc1._model = "x390"
    pc1.__cpu = "i7"  # yeni birsey enjekte etmis oldu.
    pc1._Bilgisayar__cpu = "i9"  # bu, asil sinif icindeki __cpu

    attributes = dir(pc1)
    print(attributes)
    print(pc1)


if __name__ == "__main__":
    main()
