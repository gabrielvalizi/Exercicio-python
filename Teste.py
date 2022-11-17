import pandas as pd

#definição para a função de comparação dos valores dos arquivos
def Comparacao (df1, df2):

  comp = df1.eq(df2)
  fat = []
  fibo = []
  
  for i in range(df1.shape[0]):

    if not comp.iloc[i].iat[1]:
    
     fat.append(i)

    if not comp.iloc[i].iat[2]:
     
     fibo.append(i)

  return fat,fibo

#Leitura dos arquivos em tabela 
Certo = pd.DataFrame([linhas.strip().split() for linhas in open("Arquivo_certo.data").readlines()])
Errado = pd.DataFrame([linhas.strip().split() for linhas in open("Arquivo_errado.data").readlines()])

print("Comparação:")

fatorial1, fibonacci1 = Comparacao (Certo,Errado)

if fatorial1 == []:

  if fibonacci1 == []:

    #caso 1: valor de fibo e fat estão certos
    print("Tudo certo")

  else:

    #caso 2: valor de fibo está errado e fat está certo
    print("Fibo errado na linha:",fibonacci1)
    print("Fat certo") 

else:

  print("Fat errado na linha:",fatorial1)

  if fibonacci1 == []:

    #caso 3: valor de fibo está certo e fat está errado
    print("Fibo certo")

  else:

    #caso 4: valor de fibo e fat estão errados
    print("Fibo errado na linha:",fibonacci1)