class Musvedde(object):
    def __init__(self, metin, baslik):
        self.metin = metin
        self.baslik = baslik

    def hello(self):
        print("Helloooo..")

    @classmethod
    def greet(cls):
        print("class %r greet you")


def main():
    musvedde = Musvedde("Zeki", "Merhaba")
    musvedde.hello()
    musvedde.greet()


if __name__ == "__main__":
    main()
