data={1:'Deep',2:'Bandish',4:'Nirmit'}
print(data)
print(data[1])
print(data.get(2))
print(data.get(1,'Not found'))
print(data.get(3,'Not found'))

keys=['Bandish','Nirmit','Deep']
values=['Python','Java','JS']
data=dict(zip(keys,values))
print(data)

data['Monika']='CS'
print(data)


prog={'JS':'Atom ','CS':'VS','Python':['Pycharm','Sublime'],'Java':{'JSE':'Netebans','JEE':'Eclipse'}}
print(prog['JS'])
print(prog['Java']['JEE'])
print(prog['Python'][0])