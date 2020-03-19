#Mampir cok
#https://github.com/JustAHackers
#youtube : JustA Hackers
import requests,re,os
from difflib import get_close_matches as caris
G0 = "\033[0;32m"
G1 = "\033[1;32m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
Y1 = "\033[1;33m"
Y0 = "\033[0;33m"
os.system('clear')
a=requests.get("https://api.kawalcorona.com/").text
namanegara=re.findall('"Country_Region":"(.*?)"',a)
print("""
%s ____ _____ __ __   ____ _____ _____ _____ __  __  ___
((    ||==  ||<<   ((   ((   ))||_//((   ))||\\ || ||=||
 \\_ _ ||___ || \\    \\__   \\_// ||\\    \\_// || \|| || ||

"""%(G1))
ask=raw_input("%s[%s#%s] %sCountry : "%(G1,Y1,G1,W1))
cari="".join(caris(ask,namanegara,n=1,cutoff=0))
pat= r'{"OBJECTID":.*?,"Country_Region":"'+cari+'","Last_Update":.*?,"Lat":.*?,"Long_":.*?,"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),"Active":(.*?)}}'
b=re.search(pat,a)
print ("\n{}[{}#{}] {}{} Status").format(G1,Y1,G1,W1,cari)
print ("""\n{}[{}#{}] {}Infected  : {}
{}[{}#{}] {}Died      : {}
{}[{}#{}] {}Recovered : {}
{}[{}#{}] {}Active    : {}
""".format(G1,Y1,G1,W1,b.group(1),G1,Y1,G1,W1,b.group(2),G1,Y1,G1,W1,b.group(3),G1,Y1,G1,W1,b.group(4)))




