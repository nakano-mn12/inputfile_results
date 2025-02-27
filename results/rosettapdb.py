import sys
args=sys.argv

with open(args[1], mode='r') as f:
    data_lines = f.readlines()

for line in data_lines:
    if "H1" in line:
        line = line.replace(" H1", "1H ")
    if "H2" in line:
        line = line.replace(" H2", "2H ")       
    if "H3" in line:
        line = line.replace(" H3", "3H ")
    #GLYの変換
    if "GLY" in line:
        if "HA2" in line:
            line = line.replace(" HA2", "1HA ")
        if "HA3" in line:
            line = line.replace(" HA3", "2HA ")       
    #ALAの変換
    if "ALA" in line:
        if "HB1" in line:
            line = line.replace(" HB1", "1HB ")
        if "HB2" in line:
            line = line.replace(" HB2", "2HB ")       
        if "HB3" in line:
            line = line.replace(" HB3", "3HB ") 
    #VALの変換      
    if "VAL" in line:
        if "HG11" in line:
            line = line.replace("HG11", "1HG1")
        if "HG12" in line:
            line = line.replace("HG12", "2HG1")       
        if "HG13" in line:
            line = line.replace("HG13", "3HG1")       
        if "HG21" in line:
            line = line.replace("HG21", "1HG2")
        if "HG22" in line:
            line = line.replace("HG22", "2HG2")       
        if "HG23" in line:
            line = line.replace("HG23", "3HG2")
    #LEUの変換
    if "LEU" in line:
        if "HB2" in line:
            line = line.replace(" HB2", "1HB ")
        if "HB3" in line:
            line = line.replace(" HB3", "2HB ")    
        if "HD11" in line:
            line = line.replace("HD11", "1HD1")
        if "HD12" in line:
            line = line.replace("HD12", "2HD1")       
        if "HD13" in line:
            line = line.replace("HD13", "3HD1")       
        if "HD21" in line:
            line = line.replace("HD21", "1HD2")
        if "HD22" in line:
            line = line.replace("HD22", "2HD2")       
        if "HD23" in line:
            line = line.replace("HD23", "3HD2")
    #ILEの変換
    if "ILE" in line:
        if "HD11" in line:
            line = line.replace("HD11", "1HD1")
        if "HD12" in line:
            line = line.replace("HD12", "2HD1")       
        if "HD13" in line:
            line = line.replace("HD13", "3HD1")       
        if "HG21" in line:
            line = line.replace("HG21", "1HG2")
        if "HG22" in line:
            line = line.replace("HG22", "2HG2")       
        if "HG23" in line:
            line = line.replace("HG23", "3HG2")
        if "HG12" in line:
            line = line.replace("HG12", "1HG1")       
        if "HG13" in line:
            line = line.replace("HG13", "2HG1")
    #SERの変換           
    if "SER" in line:
        if "HB2" in line:
            line = line.replace(" HB2", "1HB ")
        if "HB3" in line:
            line = line.replace(" HB3", "2HB ")
    #THRの変換
    if "THR" in line:
        if "HG21" in line:
            line = line.replace("HG21", "1HG2")
        if "HG22" in line:
            line = line.replace("HG22", "2HG2")       
        if "HG23" in line:
            line = line.replace("HG23", "3HG2")
    #CYSの変換
    if "CYS" in line:
        if "HB2" in line:
            line = line.replace(" HB2", "1HB ")
        if "HB3" in line:
            line = line.replace(" HB3", "2HB ")
    #METの変換
    if "MET" in line:
        if "HB2" in line:
            line = line.replace(" HB2", "1HB ")
        if "HB3" in line:
            line = line.replace(" HB3", "2HB ")
        if "HG2" in line:
            line = line.replace(" HG2", "1HG ")
        if "HG3" in line:
            line = line.replace(" HG3", "2HG ")
        if "HE1" in line:
            line = line.replace(" HE1", "1HE ")
        if "HE2" in line:
            line = line.replace(" HE2", "2HE ")       
        if "HE3" in line:
            line = line.replace(" HE3", "3HE ")
    #ASPの変換
    if "ASP" in line:
        if "HB2" in line:
            line = line.replace(" HB2", "1HB ")
        if "HB3" in line:
            line = line.replace(" HB3", "2HB ")
    #GLUの変換
    if "GLU" in line:
        if "HB2" in line:
            line = line.replace(" HB2", "1HB ")
        if "HB3" in line:
            line = line.replace(" HB3", "2HB ")
        if "HG2" in line:
            line = line.replace(" HG2", "1HG ")
        if "HG3" in line:
            line = line.replace(" HG3", "2HG ")
    #LYSの変換
    if "LYS" in line:
        if "HB2" in line:
            line = line.replace(" HB2", "1HB ")
        if "HB3" in line:
            line = line.replace(" HB3", "2HB ")
        if "HG2" in line:
            line = line.replace(" HG2", "1HG ")
        if "HG3" in line:
            line = line.replace(" HG3", "2HG ")
        if "HD2" in line:
            line = line.replace(" HD2", "1HD ")
        if "HD3" in line:
            line = line.replace(" HD3", "2HD ")
        if "HE2" in line:
            line = line.replace(" HE2", "1HE ")       
        if "HE3" in line:
            line = line.replace(" HE3", "1HE ")                  
        if "HZ1" in line:
            line = line.replace(" HZ1", "1HZ ")
        if "HZ2" in line:
            line = line.replace(" HZ2", "2HZ ")       
        if "HZ3" in line:
            line = line.replace(" HZ3", "3HZ ")
    #ARGの変換
    if "ARG" in line:
        if "HB2" in line:
            line = line.replace(" HB2", "1HB ")
        if "HB3" in line:
            line = line.replace(" HB3", "2HB ")
        if "HG2" in line:
            line = line.replace(" HG2", "1HG ")
        if "HG3" in line:
            line = line.replace(" HG3", "2HG ")
        if "HD2" in line:
            line = line.replace(" HD2", "1HD ")
        if "HD3" in line:
            line = line.replace(" HD3", "2HD ")
        if "HH11" in line:
            line = line.replace("HH11", "1HH1")
        if "HH12" in line:
            line = line.replace("HH12", "2HH1")       
        if "HH21" in line:
            line = line.replace("HH21", "1HH2")
        if "HH22" in line:
            line = line.replace("HH22", "2HH2") 
    #ASNの変換          
    if "ASN" in line:
        if "HB2" in line:
            line = line.replace(" HB2", "1HB ")
        if "HB3" in line:
            line = line.replace(" HB3", "2HB ")
        if "HD21" in line:
            line = line.replace("HD21", "1HD2")
        if "HD22" in line:
            line = line.replace("HD22", "2HD2") 
    #GLNの変換      
    if "GLN" in line:
        if "HB2" in line:
            line = line.replace(" HB2", "1HB ")
        if "HB3" in line:
            line = line.replace(" HB3", "2HB ")
        if "HE21" in line:
            line = line.replace("HD21", "1HD2")
        if "HE22" in line:
            line = line.replace("HD22", "2HD2")
        if "HG2" in line:
            line = line.replace(" HG2", "1HG ")
        if "HG3" in line:
            line = line.replace(" HG3", "2HG ")
    #PHEの変換
    if "PHE" in line:
        if "HB2" in line:
            line = line.replace(" HB2", "1HB ")
        if "HB3" in line:
            line = line.replace(" HB3", "2HB ")
    #TYRの変換  
    if "TYR" in line:
        if "HB2" in line:
            line = line.replace(" HB2", "1HB ")
        if "HB3" in line:
            line = line.replace(" HB3", "2HB ")
    #HISの変換       
    if "HIE" in line:
        line = line.replace("HIE", "HIS")
        if "HB2" in line:
            line = line.replace(" HB2", "1HB ")
        if "HB3" in line:
            line = line.replace(" HB3", "2HB ")
    #TRPの変換 
    if "TRP" in line:
        if "HB2" in line:
            line = line.replace(" HB2", "1HB ")
        if "HB3" in line:
            line = line.replace(" HB3", "2HB ")
    #PROの変換
    if "PRO" in line:
        if "HB2" in line:
            line = line.replace(" HB2", "1HB ")
        if "HB3" in line:
            line = line.replace(" HB3", "2HB ")
        if "HG2" in line:
            line = line.replace(" HG2", "1HG ")
        if "HG3" in line:
            line = line.replace(" HG3", "2HG ")
        if "HD2" in line:
            line = line.replace(" HD2", "1HD ")
        if "HD3" in line:
            line = line.replace(" HD3", "2HD ")
    with open("re"+args[1], mode="a") as t:
        t.write(line)      