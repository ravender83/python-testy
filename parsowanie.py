string = 'Kontrola MP {OK,NOK}'

def s_lst_parse_option(string):
        lista = []
        start = string.find('{')
        stop = string.find('}')
        if start != -1 and stop != -1:
            beg = start - 1
            end = stop + 1 
            txt_p = string[:beg]
            txt_k = string[end:]
            lista.append(txt_p + txt_k)

            beg = start+1
            end = stop         
            opcje = string[beg:end].split(',')
            for i in opcje:
                print(i)
                lista.append(f"{txt_p} {i.replace(' ','')}{txt_k}")
            return lista
        else:
            return string

s = s_lst_parse_option(string)
print(s)
