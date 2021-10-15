import requests
import time
import os
import sys

Br = '\033[1;37m'
Vm = '\033[1;31m'
Vd = '\033[1;32m'
Am = '\033[1;33m'
Az = '\033[1;34m'
Rx = '\033[1;35m'
Cn = '\033[1;36m'
f = '\033[m'


os.system('clear')
os.system('pkg install figlet')
os.system('clear')
def retorno():
    os.system('python3 main.py')
try:
    import requests
except:
    os.system('pip install -r requirements.txt');retorno()
def cep():
    os.system('clear')
    os.system('figlet PROXY')
    cep_input = input(f'{Am}+=>{Br}')
    
    if len(cep_input) !=9:
        print(f'{Cn}+=>{Az}CEP NÃO ENCONTRADO!!{Cn}<=+')
        time.sleep(4)
        os.system('python3 main.py')
        
    req = requests.get(f'https://viacep.com.br/ws/{cep_input}/json/')
    
    address_data = req.json()
    time.sleep(3)
    print(f'{Cn}[{Az}i{Cn}]Buscando CEP...{Cn}[{Az}i{Cn}]')
    time.sleep(4)
    if 'erro' not in address_data:
        print('CEP: {}'.format(address_data['cep']))
        print('BAIRRO: {}'.format(address_data['bairro']))
        print('LOCALIDADE: {}'.format(address_data['localidade']))
        print('UF: {}'.format(address_data['uf']))
        print('GIA: {}'.format(address_data['gia']))
        print('IBGE: {}'.format(address_data['ibge']))
    print(f'====\n{Cn}[{Az}01{Cn}] Nova Consulta\n{Cn}[{Az}02{Cn}] Menu\n====')
    op = input(f'{Am}+=>{Br}')
    if(op=='1'):
        print(f'{Az}Okay!!')
        time.sleep(4)
        os.system('clear')
        cep()
    if(op=='2'):
        print(f'{Az}Okay!!')
        os.system('python3 main.py')
def ip():
    os.system('clear')
    os.system('figlet [PROXY]')
    ip_input = input(f'{Am}+=>{Br}')
    
    if len(ip_input) !=15:
        print(f'{Cn}+=>{Az}CEP NÃO ENCONTRADO!!{Cn}<=+')
        time.sleep(4)
        retorno()
        
    api=requests.get("http://ipwhois.app/json/")
    
    api_data=api.json()
    time.sleep(3)
    print(f'{Cn}[{Az}i{Cn}]Buscando IP...{Cn}[{Az}i{Cn}]')
    time.sleep(4)
    if 'erro' not in api_data:
        print('IP: {}'.format(api_data['ip']))
        print('TIPO: {}'.format(api_data['type']))
        print('CONTINENTE: {}'.format(api_data['continent']))
        print('CODIGO DO CONTINENTE: {}'.format(api_data['continent_code']))
        print('PAÍS: {}'.format(api_data['country']))
        print('CAPITAL DO PAÍS: {}'.format(api_data['coutry_capital']))
        print(f'====\n{Cn}[{Az}01{Cn}] Nova Consulta\n{Cn}[{Az}02{Cn}] Menu\n====')
        op = input(f'{Am}+=>{Br}')
        if(op=='1'):
            print(f'{Cn}Okay!!')
            time.sleep(4)
            ip()
        if(op=='2'):
            print(f'{Az}Okay!!')
            os.system('python3 main.py')
def cnpj():
    os.system('clear')
    os.system('figlet PROXY')
    cnpj_input = input(f'{Am}+=>')
    
    if len(cnpj_input) !=14:
        print(f'{Cn}[{Az}i{Cn}]CNPJ NÃO ENCONTRADO!!{Cn}[{Az}i{Cn}]')
        time.sleep(4)
        cnpj()
    
    cnpj=requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj_input}')
    
    cnpj_data=cnpj.json()
    time.sleep(3)
    print(f'{Cn}[{Az}i{Cn}]Buscando CNPJ...{Cn}[{Az}i{Cn}]')
    time.sleep(4)
    if 'erro' not in cnpj_data:
        print('Situação: {}'.format(cnpj_data['situacao']))
        print('Uf: {}'.format(cnpj_data['uf']))
        print('Municipio: {}'.format(cnpj_data['municipio']))
        print('Logradouro: {}'.format(cnpj_data['logradouro']))
        print('Numero: {}'.format(cnpj_data['numero']))
        print('Complemento: {}'.format(cnpj_data['complemento']))
        print(f'====\n{Cn}[{Az}01{Cn}] Nova Consulta\n{Cn}[{Az}02{Cn}] Menu\n====')
        op = input(f'{Am}+=>{Br}')
        if(op=='1'):
            print(f'{Cn}Okay!!')
            time.sleep(4)
            cnpj()
        if(op=='2'):
            print(f'{Az}Okay!!')
            retorno()
def cpf():
    os.system('clear')
    os.system('figlet PROXY')
    cpf_input = input(f'{Am}+=>')
    if len(cpf_input) !=11:
        print(f'{Cn}[{Az}i{Cn}]CPF NÃO ENCONTRADO!!{Cn}[{Az}i{Cn}]')
        time.sleep(4)
        cpf()
    
    
    req = requests.post(f'https://gateway.apiserpro.serpro.gov.br/consulta-cpf-df-trial/v1/cpf/{cpf_input}', {"code": "", "type": "", "message": "", "description": "", "id": ""})
    
    resposta = json.loads(req.content)
    time.sleep(3)
    print(f'{Cn}[{Az}i{Cn}]Buscando CNPJ...{Cn}[{Az}i{Cn}]')
    time.sleep(4)
    print('Code: {}'.format(resposta['code']))
    print('Type: {}'.format(resposta['type']))
    print('Message: {}'.format(resposta['message']))
    print('Description: {}'.format(resposta['description']))
    print('ID: {}'.format(resposta['id']))
    print(f'====\n{Cn}[{Az}01{Cn}] Nova Consulta\n{Cn}[{Az}02{Cn}] Menu\n====')
    op = input(f'{Am}+=>{Br}')
    if(op=='1'):
        print(f'{Cn}Okay!!')
        time.sleep(4)
        cpf()
    if(op=='2'):
        print(f'{Az}Okay!!')
        retorno()
def sair():
    os.system('clear')
    time.sleep(2)
    print(f'{Az}Saindo...{Br}')
    time.sleep(3)
    exit()


os.system('clear')
os.system('figlet PROXY')
print(f'''
{Cn}[{Az}1{Cn}]Buscar CEP
{Cn}[{Az}2{Cn}]Buscar CNPJ
{Cn}[{Az}3{Cn}]Buscar IP
{Cn}[{Az}4{Cn}]Buscar CPF
{Cn}[{Rx}5{Cn}]Sair
''')
option = input(f'{Am}+=>{Br}')

if(option=='1'):
    cep()
if(option=='2'):
    cnpj()
if(option=='3'):
    ip()
if(option=='4'):
    cpf()
if(option=='5'):
    sair()
else:
    os.system('python3 main.py')