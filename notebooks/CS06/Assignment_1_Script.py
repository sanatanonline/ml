import numpy as np
import matplotlib.pyplot as plt
from pandas import ExcelWriter, ExcelFile, read_excel, DataFrame, concat
from openpyxl import load_workbook

gcloud_tokeninfo = requests.get('https://www.googleapis.com/oauth2/v3/tokeninfo?access_token=' + gcloud_token[0]).json()
user_email = gcloud_tokeninfo['email']


def readExcelSheet1(excelfile):
    return (read_excel(excelfile)).values

def readExcelRange(excelfile,sheetname="Sheet1",startrow=1,endrow=1,startcol=1,endcol=1):
    values=(read_excel(excelfile, sheetname,header=None)).values
    return values[startrow-1:endrow,startcol-1:endcol]

def readExcel(excelfile,**args):
    if args:
        data=readExcelRange(excelfile,**args)
    else:
        data=readExcelSheet1(excelfile)
    [nr,nc]=data.shape
    if [nr,nc]==[1,1]:
        return data[0,0]
    elif min([nr,nc])==1:
        return np.squeeze(data)
    else:
        return data

def writeExcelData(x,excelfile,sheetname,startrow,startcol):
    df=DataFrame(x)
    book = load_workbook(excelfile)
    writer = ExcelWriter(excelfile, engine='openpyxl') 
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    df.to_excel(writer, sheet_name=sheetname,startrow=startrow-1, startcol=startcol-1, header=False, index=False)
    writer.save()
    writer.close()

def getSheetNames(excelfile):
    return (ExcelFile(excelfile)).sheet_names

def showHistograms(HF, HM, xmin, xmax):
    B=len(HF)
    plt.figure(figsize=(10,5))
    opacity = 0.5
    [bincenters,binwidth]=np.linspace(xmin, xmax, num=B, retstep=True)
    rects1 = plt.bar(bincenters, HF, binwidth,
                    alpha=opacity,
                    color='pink',
                    edgecolor='black',
                    label='Female')
    rects2 = plt.bar(bincenters, HM, binwidth,
                    alpha=opacity,
                    color='b',
                    edgecolor='black',
                    label='Male')
    plt.xlabel('Height')
    plt.ylabel('Count')
    plt.xticks(bincenters, bincenters.astype(int), fontsize=10)
    plt.legend()
    plt.show()

def showResult(query, label, probability):
    print(DataFrame({'Query':query, 'Gender':label, 'Probability':probability}))

def showAllResults(query, resultHlabel, resultHprob, resultH50label, resultH50prob, resultBlabel, resultBprob, resultB50label, resultB50prob):
    return DataFrame({'Query':query, 'GH':resultHlabel, 'PH':resultHprob, 'GH50':resultH50label, 'PH50':resultH50prob, 'GB':resultBlabel, 'PB':resultBprob, 'GB50':resultB50label, 'PB50':resultB50prob})

all_vars = [\
            'minheight',\
            'maxheight',\
            'HF',\
            'HM',\
            'muF',\
            'muM',\
            'sigmaF',\
            'sigmaM',\
            'NF',\
            'NM',\
            'HF50',\
            'HM50',\
            'muF50',\
            'muM50',\
            'sigmaF50',\
            'sigmaM50',\
            'NF50',\
            'NM50',\
            'GH',\
            'PH',\
            'GB',\
            'PB',\
            'GH50',\
            'PH50',\
            'GB50',\
            'PB50'\
           ]

def check_one_var(varstring):
  try: exec(varstring)
  except NameError: print('***** Error! ' + varstring + ' is not defined. *****')
  else: print(varstring + ' exists.')

def check_all_vars(all_vars):
  list(map(check_one_var, all_vars))

def closeExcelFile(excelfile):
  try: user_email
  except NameError: None
  else: writeExcelData([user_email], excelfile, 'ID', 2, 1)


