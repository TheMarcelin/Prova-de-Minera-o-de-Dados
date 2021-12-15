import pandas as pd
import matplotlib.pyplot as plt
tita = pd.read_csv('titanic.csv')

#Questão A
#print(tita.head(10))

#Questão B
#titan = tita.sort_values('Name')
#print(titan.head(20))

#Questão C
#tita["Sobreviventes"] = tita["Survived"]
#tita["Sobreviventes"] = tita["Sobreviventes"].replace([0,1],["Não","Sim"])
#print(tita.head(10))

#Questão D
#titan = tita.drop(columns=["SibSp","Ticket", "Parch"])
#print(titan.head(10))

#Questão E
#tita.rename(columns={"PassengerId": "ID", "Survived":"Sobrevivente", "Pclass": "Classe", "Fare":"Tarifa", "Name" : "Nome", "Sex":"Gênero", "Age": "Idade", "Cabin":"Cabine", "Embarked":"Embarque"}, inplace=True)
#print(tita.head(10))
#Não renomeei as colunas "Parch", "Ticket" e "SibSp"

#Questão F
#tita['Sex'] = tita['Sex'].replace(["male","female"],["masculino","FEMININO"])
#print(tita.head(10))

#Questão G
#tita['Survived'].fillna(0,inplace=True) #Para marcar os 0's como dígito 0, pois o dataframe não estava reconhecendo o 0. 
#tita.drop(tita.loc[tita['Survived'] == 0].index,inplace=True)
#titan = tita.groupby('Pclass', as_index = False)['Survived'].count()
#print(titan)

#Questão H
#tita['Survived'].fillna(0,inplace=True)
#tita.drop(tita.loc[tita['Survived'] == 1].index,inplace=True)
#titan = tita.groupby('Sex', as_index=False)['Survived'].count()
#print(titan)

#Questão I
#tita['Survived'].fillna(0,inplace=True)
#tita.drop(tita.loc[tita['Survived'] == 0].index,inplace=True)
#titan = tita.groupby('Pclass', as_index = False)['Survived'].count()
#print(titan)
#plt.bar(titan["Pclass"],titan["Survived"])
#plt.xlabel("Classe")
#plt.ylabel("Nº de Sobreviventes")
#plt.show()

#Questão J
#Tive que instalar uma biblioteca específica para realizar a conversão :)
#saida = pd.ExcelWriter("Teste.xlsx")
#tita.to_excel(saida)
#saida.save()


