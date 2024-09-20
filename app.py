import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # Utilizada para plotar gráficos e histogramas
import seaborn as sns # Complemento da matplotlib para plotar gráficos mais bonitos e informativos
import os # Utilizada para manipular arquivos e diretórios

dir_path = "./data"

if os.path.exists(dir_path):
    for dirname, _, filenames in os.walk(dir_path):
        for filename in filenames:
            print(os.path.join(dirname, filename))
else:
    print(f"O diretório {dir_path} não foi encontrado. Verifique o caminho.")
    
csv_path = "./data/diabetes_dataset00.csv"

os.path.join(dir_path, csv_path)

if os.path.exists(csv_path):
    # Carrega o CSV em um DataFrame do Pandas
    df = pd.read_csv(csv_path)
    print(df.head())  # Exibe as primeiras linhas do DataFram
    
    df.isnull().sum()  # Verifica se existem valores nulos
    
    plt.figure(figsize=(8, 6))
    sns.histplot(df['Age'], bins=20, kde=True)
    plt.title('Distribuição de Idade')
    plt.xlabel('Idade')
    plt.ylabel('Frequência')
    plt.show()


    plt.figure(figsize=(8, 6))
    sns.histplot(df['BMI'], bins=20, kde=True)
    plt.title('Distribuição do IMC')
    plt.xlabel('BMI')
    plt.ylabel('Frequência')
    plt.show()


    plt.figure(figsize=(8, 6))
    sns.histplot(df['Insulin Levels'], bins=20, kde=True)
    plt.title('Distribuição de níveis de insulina')
    plt.xlabel('Níveis de insulina')
    plt.ylabel('Frequência')
    plt.show()
    
    
else:
    print(f"Arquivo {csv_path} não encontrado.")
    