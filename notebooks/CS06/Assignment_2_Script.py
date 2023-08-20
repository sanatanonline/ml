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

def show2DHistograms(HF, HM):
  plt.subplot(1, 2, 1);
  plt.imshow(HF,interpolation='None',cmap=plt.get_cmap('gray'));
  plt.subplot(1, 2, 2);
  plt.imshow(HM,interpolation='None',cmap=plt.get_cmap('gray'));
  plt.show()

def showResult(query, label, probability):
    print(DataFrame({'Query (Height)':query[:, 0], 'Query (Handspan)':query[:, 1], 'Gender':label, 'Probability':probability}))

def showAllResults(query, resultHlabel, resultHprob, resultBlabel, resultBprob):
    return DataFrame({'Query (Height)':query[:, 0], 'Query (Handspan)':query[:, 1], 'GH':resultHlabel, 'PH':resultHprob, 'GB':resultBlabel, 'PB':resultBprob})

all_vars = [\
            'xmin',\
            'xmax',\
            'HF',\
            'HM',\
            'muF',\
            'muM',\
            'sigmaF',\
            'sigmaM',\
            'NF',\
            'NM',\
            'GH',\
            'PH',\
            'GB',\
            'PB'\
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


