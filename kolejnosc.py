from rav.files import otworz
from rav.zmien import string_na_clean_list
from rav.poka import liste

obecne = []
tagi = []
nowe = [''] * 10

obecne = string_na_clean_list(otworz('obecne.txt'))
tagi = string_na_clean_list(otworz('tagi.txt'))
nowe = [''] * len(obecne)
    
for k, i in enumerate(obecne):
   nowe[tagi.index(i)] = tagi[k] 

liste(nowe)
    
with open('nowe.txt', "w") as file:
    try:
        file.write('\n'.join(nowe))
    except:
        print('Wystąpił błąd zapisu')
