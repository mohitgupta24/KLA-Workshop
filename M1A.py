from datetime import datetime
import yaml

fl = open("Milestone1A.yaml", "r")
f = open("log.txt", "w")
dic = dict()

def Task(ts,cp):
    f.write(str(datetime.now())+";"+cp+" Entry\n")
    f.write(str(datetime.now())+";"+cp+" Executing "+ts['Function']+" ("+ts['Inputs']['FunctionInput']+", "+ts['Inputs']['ExecutionTime']+")\n")
    f.write(str(datetime.now())+";"+cp+" Exit\n")

def Flow(fl,cp):
    for data in fl:
        if type(fl[data]) == dict:
            print(fl[data])
            if(fl[data]['Type'] == 'Flow'):
                solve(fl[data],cp+"."+str(data))
            else:
                Task(fl[data],str(cp+"."+data))

def solve(dic, cp):
    for data in dic:
        if data == 'Type':
            if(dic[data] == 'Flow'):
                f.write(str(datetime.now())+";"+cp+" Entry\n")    
                Flow(dic['Activities'],str(cp))
                f.write(str(datetime.now())+";"+cp+" Exit\n")    
            elif(dic[data] == 'Task'):
                Flow(dic['Activities'],str(cp))

if __name__=='__main__':
    content = yaml.load(fl,Loader=yaml.FullLoader)
    dic = content
    for data in dic:
        if type(dic[data]) == dict:
            solve(dic[data],str(data))