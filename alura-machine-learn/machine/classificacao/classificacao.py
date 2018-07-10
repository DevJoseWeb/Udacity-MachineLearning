
porco1 = 	[1, 1, 0]
porco2 = 	[1, 1, 0]
porco3 = 	[1, 1, 0]

cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

# 1 = porco | -1 = cachorro
marcacoes = [1, 1, 1, -1, -1, -1]

misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]

teste = [misterioso1, misterioso2, misterioso3]

marcacoes_teste = [-1, 1, -1]

resultado = modelo.predict(teste)
print (resultado)

# #chamada para a biblioteca de machine learn
# from sklearn.naive_bayes import MultinomialNB

# modelo = MultinomialNB()

# # .fit = treinar
# modelo.fit (dados, marcacoes)

# # mostrar o resultado da premeditação do resultado
# print(modelo.predict(teste))