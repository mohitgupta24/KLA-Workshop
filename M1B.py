from datetime import datetime
from time import sleep
import threading
import yaml

fl = open("Milestone1B.yaml", "r")
f = open("log2.txt", "w")
dic = dict()

def Task(ts,cp):
    f.write(str(datetime.now())+";"+cp+" Entry\n")
    f.write(str(datetime.now())+";"+cp+" Executing "+ts['Function']+" ("+ts['Inputs']['FunctionInput']+", "+ts['Inputs']['ExecutionTime']+")\n")
    sleep(int(ts['Inputs']['ExecutionTime']))
    f.write(str(datetime.now())+";"+cp+" Exit\n")


def Flow_seq(fl,cp):
    for data in fl:
        if type(fl[data]) == dict:
            if(fl[data]['Type'] == 'Flow'):
                solve(fl[data],cp+"."+str(data))
            else:
                Task(fl[data],str(cp+"."+data))
                
def Flow_con(fl,cp):
    for data in fl:
        if type(fl[data]) == dict:
            if(fl[data]['Type'] == 'Flow'):
                solve(fl[data],cp+"."+str(data))
            else:
                t1 = threading.Thread(target=Task, args=(fl[data],str(cp+"."+data),))
                t1.start()

def solve(dic, cp):
    for data in dic:
        if data == 'Type':
            if(dic[data] == 'Flow'):
                f.write(str(datetime.now())+";"+cp+" Entry\n")
                if(dic['Type'] =='Sequential'):    
                    Flow_seq(dic['Activities'],str(cp))
                else:
                    Flow_con(dic['Activities'],str(cp))
                f.write(str(datetime.now())+";"+cp+" Exit\n")    
            elif(dic[data] == 'Task'):
                Flow(dic['Activities'],str(cp))

if __name__=='__main__':
    content = yaml.load(fl,Loader=yaml.FullLoader)
    dic = content
    for data in dic:
        if type(dic[data]) == dict:
            solve(dic[data],str(data))