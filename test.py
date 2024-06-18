from model.model import Model

myModel = Model()
myModel.crea_grafo("Ahwatukee")
print(myModel.getGraphDetails())
print(myModel.getCammino("Cupz N' Crepes", "Healty and Clean Living Environments"))
