import os
import urllib

def rename(name):
    if len(name) == 2:
        name = '0' + name + '.jpg'
    elif len(name) == 1:
        name = '00' + name + '.jpg'
    else:
        name = name + '.jpg'
    return name
   
os.chdir("D:\\download")
os.getcwd()
count = 1
name=str(count)
name = rename(name)
print(name)
while count < 15:
    url = "http://jandan.net/ooxx/page-" + str(1744+count)+ '#comments'
    a = urllib.urlopen(url)
    f = open(name, "wb")
    f.write(a.read())
    f.close()
    print(url + ' Saved!')   
    count = count + 1
    name=str(count)
    name = rename(name)
    print(name)
    url = 'http://bgimg1.meimei22.com/list/2012-5-24/2/sa' + name
    try:
        a = urllib.urlopen(url)
        pass
    except (Exception) as e:
        print(e) 
    else:
        pass
else:
    print(url + ' not found')
#github
#ssh12