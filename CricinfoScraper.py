import json
import os
import csv
import re
import pandas as pd
import requests as req
import xlsxwriter
cwd = os.getcwd()
cric = os.path.join(cwd,'Cricinfo')
if not os.path.exists(cric):
    os.makedirs(cric)
teams = ['ind','pak','aus','rsa','sl','bd','uk','usa']
r = req.get("http://www.espncricinfo.com/netstorage/summary.json")
rson = r.json()
for i in range(len(rson['modules']['ind'])):    
    if rson['modules']['ind'][i]['title']=='International':
        for j in range(len(rson['modules']['ind'][i])):
            try:
                match_id = rson['modules']['ind'][i]['matches'][j]
                #print(match_id)
                info = rson['matches'][match_id]
                #print(info)
                df=pd.DataFrame({"Team1_Name":[info['team1_name']],
                                 "Team2_Name":[info['team2_name']],
                                 "Team1_Short":[info['team1_abbrev']],
                                 "Team2_Short":[info['team2_abbrev']],
                                 "Team1_Score":[info['team1_score']],
                                 "Team2_Score":[info['team2_score']],
                                 "URL":['http://www.espncricinfo.com'+str(info['url'])]
                                 })
                writer = pd.ExcelWriter(os.path.join(cric,'Cricinfo.xlsx'), engine='xlsxwriter')
                df.to_excel(writer, sheet_name='Sheet'+str(j+1))
                writer.save()
            except IndexError:
                pass
                

