f = open('base.txt', 'r')
content = f.read()
content_list = content.split(' ')
for x in content_list:
    if x == '':
        content_list.remove(x)
    else:
        pass
f.close()
for x in range(0,len(content_list)-2):
    if x != len(content_list)-1:
        
        if (content_list[x] == '</h1>') and (content_list[x+1] == '<h1>'):
            poped = content_list.pop(x)
            poped1 = content_list.pop(x)
        else:
            pass
for x in range(0,len(content_list)-2):
    if x != len(content_list)-1:
        if (content_list[x] == '</b>') and (content_list[x+1] == '<b>'):
            poped = content_list.pop(x)
            poped1 = content_list.pop(x)
        else:
            pass
for x in range(0,len(content_list)-2):
    if x != len(content_list)-1:
        if (content_list[x] == '</i>') and (content_list[x+1] == '<i>'):
            poped = content_list.pop(x)
            poped1 = content_list.pop(x)
        else:
            pass

f = open('base.txt', 'w')
for x in content_list:
    f.write(x + ' ')