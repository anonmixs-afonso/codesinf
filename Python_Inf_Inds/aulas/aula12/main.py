#Utilize um dicionário para armazenar os parâmetros de um inversor de frequência.

#Data of the Parameters
dados0 = {'Description': 'Access to Parameters', 'Range Values': '0 a 9999', 'Factory Adjustment': '0', 'User Adjustment': 'NULL', 'Propr': 'no', 'Grup': 'NULL', 'Page': '5-2'}
dados1 = {'Description': 'Speed Reference', 'Range Values': '0 a 65535', 'Factory Adjustment': 'NULL', 'User Adjustment': 'NULL', 'Propr': 'no', 'Grup': 'READ', 'Page': '17-1'}

#The Parameters
Parameters = {'P0000': dados0, 'P0001': dados1}


print(f'Description: {Parameters["P0001"]["Description"]}')



def num (a):
    a += a

a = 2
print(f'"a" before the function {a}.')
num(a)
print(f'"a" after the function {a}.')


def listtest (listv):
    listv.append(2)

listf = [1,2,3]
print(f'List before function {listf}.')
listtest(listf)
print(f'List after function {listf}.')
    