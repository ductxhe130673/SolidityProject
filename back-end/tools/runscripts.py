import json
import requests
import subprocess
from subprocess import Popen, PIPE, STDOUT


# for Windows
# path = r"D:\Document\CapStone\CapstoneProject\SolidityProject\tools"
# for Ubuntu
path = r"G:\CapstoneProject\SolidityProject\tools"


# ---save file to temporary----
# data = {'name':'', '':'', ...}
def savetotemporary(data):
    for k in data.keys():
        if k == 'name':
            continue
        with open(f'{path}/temporary/{k}', 'w') as f:
            f.write(data[k])



def unfolding():
    # get from temporary
    # context_PATH = './test/test.xml'
    #ltl_PATH = './test/ltl.json'
    # initialMarking_PATH  = './test/test.im.json'
    context_PATH = path + '/temporary/context_PATH.xml'
    ltl_PATH = path + '/temporary/ltl_PATH.json'
    initialMarking_PATH  = path + '/temporary/initialMarkingInfor.json'

    # wait tools
    lna_PATH = './test/EtherGame.lna'
    sol_ast_PATH = './test/blindAuction.ast'
    lna_json_PATH = './test/etherGame.json'

    # output
    output_PATH = './output/'
    output_NAME = 'test'

    commandUnf = "./unfolding --lna " + lna_PATH + " --context " + \
        context_PATH + " --context-type " + "DCR" + " --ltl "+ltl_PATH+" --sol-ast " + \
        sol_ast_PATH+" --lna-json "+lna_json_PATH+ " --im-json " +initialMarking_PATH + \
         " --output_path " + output_PATH+" --output_name "+output_NAME
    # print (commandUnf)
    pathUnf = path + r"/unfolding"
    unfolding = subprocess.run(
        commandUnf, cwd=pathUnf, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"err" : unfolding.stderr.decode(), "file_path" : path +r"/unfolding/output/", "file_name":output_NAME}
#unfolding()

def runHelena():
    helenaPath = path + r"/unfolding/output"
    helenaFile = "test.lna"
    propfile = helenaPath + "/" + helenaFile[0:-4]+".prop.lna"
    f = open(propfile, 'r')
    propLna = str(f.read())
    begin = propLna.find("property ")+9
    end = propLna.find(":")
    property = propLna[begin:end]
    # print(property)
    helena = "helena -N=CHECK -p=" + property + " " + helenaFile
    pro4 = subprocess.run(helena, cwd=helenaPath, shell=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = str(pro4.stdout.decode("cp932"))
    start = output.find("Helena report")
    report = output[start:]
    #print(repr(report))
    f.close()
    return report

#runHelena()