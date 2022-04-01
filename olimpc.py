from glob import glob


###voiefdl;c########
class colizeus():

    def __init__(self, link, extension):
        self.link=link
        self.extension=extension



    def varedura(self, string):
        for tudo in glob(self.link + self.extension):
            with open(tudo,"r") as arq:
                karma=arq.read()
                #karma=arq.read()
                if string in karma:
                    print(f"arquivos {tudo}")




pasta=input("digita a pasta ou deixxa em branco se estiver dentro dela")#input("digita a pasta com arquivos")
ext="*."+input("Extencao dos arquivos: ")
arena=colizeus(pasta,ext)

requisito=input("digita a palavra: ")
arena.varedura(requisito)
