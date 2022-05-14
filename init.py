from utils.testapi import *
from utils.languageprocessor import *

coinname=str(input("Enter Stock Name"))
for i in range(5):
    title = [informationgather(coinname)[0][i]]
    desc = informationgather(coinname)[1][i]
    sentimentanalysis(title, desc)


