import os

directories = ['api','core','crud','database','models','schemas','tests']

for dir in directories:
    path = f'./{dir}'
    os.mkdir(dir)

    file = f'{dir}.py'
    file2 = '__init__.py'

    open(os.path.join(path, file),'w')
    open(os.path.join(path, file2),'w')