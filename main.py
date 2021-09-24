from tkinter.constants import LEFT
import pandas as pd
from os import mkdir, system, listdir
from os.path import isdir, isfile, join
    
path = 'planilhas'

if not isdir(path):
    mkdir(path)



system('cls')
while True:
    
    input('Tecle ENTER para continuar...')
    system('cls')
    nome_pasta = input('Digite o nome da pasta de saída - Ex: 23-09-21: ')
    
    if not isdir(f'{path}\\{nome_pasta}'):
        mkdir(f'{path}\\{nome_pasta}')  
    
    files = [f for f in listdir(path) if isfile(join(path,f))]
    print('Lendo arquivos: \n%s' % '\n'.join(files))
    
    count = 0
    
    if not files:
        print('Você precisa ter arquivos .xlsx dentro da pasta "planilhas" para continuar.')
        continue
    
    print(f'\n---------------------- Convertendo -----------------------')
    for i in files:
        
        leitura = pd.read_excel(f'{path}\\{i}')
        
        print('> %s' % i.replace('.xlsx', '.csv') )

        arquivo = i.replace('.xlsx', '')
        
        leitura.to_csv(f'{path}\\{nome_pasta}\\{arquivo}.csv', sep=',', quoting=1, index=False, encoding='utf-8')
        
        count += 1
    if count < 2:  
        print(f'Foi convertido um total de {count} arquivo.')
    else:
        print(f'Foram convertidos um total de {count} arquivos')
    
    print('----------------- Conversão concluída ----------------------')

