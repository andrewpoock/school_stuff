# Project 3
# Andrew Poock

from statistics import stdev as sd
from statistics import mean
from math import sqrt
from functools import reduce

aml = open('ALL_AML_gr.thr.train.csv', 'r')

foldratios = {}
ALLstdev = {}
AMLstdev = {}
ALLmean = {}
AMLmean = {}
ALLs2n = {}
ALLtvalue = {}
AMLs2n = {}
AMLtvalue = {}
lines = []
for line in aml:
    cleanline = line.strip('\n')
    splitline = cleanline.split(',')
    if splitline[0] == 'id':
        continue
    vals = splitline[1:]
    vals = [eval(i) for i in vals]
    foldratios[splitline[0]] = max(vals) - min(vals)
    ALLstdev[splitline[0]] = sd(vals[0:27])
    ALLmean[splitline[0]] = mean(vals[0:27])
    AMLstdev[splitline[0]] = sd(vals[27:39])
    AMLmean[splitline[0]] = mean(vals[27:39])
    try:
        ALLs2n[splitline[0]] = (ALLmean[splitline[0]] - AMLmean[splitline[0]])/(ALLstdev[splitline[0]] + AMLstdev[splitline[0]])
        ALLtvalue[splitline[0]] = (ALLmean[splitline[0]] - AMLmean[splitline[0]])/(sqrt(((ALLstdev[splitline[0]]**2)/27)+((AMLstdev[splitline[0]]**2)/11)))
        AMLs2n[splitline[0]] = (AMLmean[splitline[0]] - ALLmean[splitline[0]])/(AMLstdev[splitline[0]] + ALLstdev[splitline[0]])
        AMLtvalue[splitline[0]] = (AMLmean[splitline[0]] - ALLmean[splitline[0]])/(sqrt(((AMLstdev[splitline[0]]**2)/11)+((ALLstdev[splitline[0]]**2)/27)))
    except ZeroDivisionError:
        ALLs2n[splitline[0]] = 0
        ALLtvalue[splitline[0]] = 0
        AMLs2n[splitline[0]] = 0
        AMLtvalue[splitline[0]] = 0

aml.close()

keymaxes = []
valmax = None
for key in foldratios:
    if valmax == None:
        valmax = foldratios[key]
        keymaxes = [key]
    if valmax is not None:
        if foldratios[key] > valmax:
            valmax = foldratios[key]
            keymaxes = [key]
        if foldratios[key] == valmax:
            keymaxes.append(key)

keymins = []
valmin = None
for key in foldratios:
    if valmin == None:
        valmin = foldratios[key]
        keymins = [key]
    if valmin is not None:
        if foldratios[key] < valmin:
            valmin = foldratios[key]
            keymins = [key]
        if foldratios[key] == valmin:
            keymins.append(key)

print('\nS2N comparison:')
for key in ALLs2n:
    if key == 'U22376_cds2_s_at':
        print(ALLs2n[key])
for key in AMLs2n:
    if key == 'U22376_cds2_s_at':
        print(AMLs2n[key])
print('\nTval comparison:')
for key in ALLtvalue:
    if key == 'U22376_cds2_s_at':
        print(ALLtvalue[key])
for key in AMLtvalue:
    if key == 'U22376_cds2_s_at':
        print(AMLtvalue[key])

ALLs2nkeymaxes = []
ALLs2nmaxes = []
for key in ALLs2n:
    if len(ALLs2nkeymaxes) < 50:
        ALLs2nmaxes.append(ALLs2n[key])
        ALLs2nkeymaxes.append(key)
    else:
        minvalue = min(ALLs2nmaxes)
        mindex = ALLs2nmaxes.index(minvalue)
        if ALLs2n[key] > minvalue:
            ALLs2nmaxes[mindex] = ALLs2n[key]
            ALLs2nkeymaxes[mindex] = key

ALLtvalkeymaxes = []
ALLtvalmaxes = []
for key in ALLtvalue:
    if len(ALLtvalkeymaxes) < 50:
        ALLtvalmaxes.append(ALLtvalue[key])
        ALLtvalkeymaxes.append(key)
    else:
        minvalue = min(ALLtvalmaxes)
        mindex = ALLtvalmaxes.index(minvalue)
        if ALLtvalue[key] > minvalue:
            ALLtvalmaxes[mindex] = ALLtvalue[key]
            ALLtvalkeymaxes[mindex] = key

AMLs2nkeymaxes = []
AMLs2nmaxes = []
for key in AMLs2n:
    if len(AMLs2nkeymaxes) < 50:
        AMLs2nmaxes.append(AMLs2n[key])
        AMLs2nkeymaxes.append(key)
    else:
        minvalue = min(AMLs2nmaxes)
        mindex = AMLs2nmaxes.index(minvalue)
        if AMLs2n[key] > minvalue:
            AMLs2nmaxes[mindex] = AMLs2n[key]
            AMLs2nkeymaxes[mindex] = key

AMLtvalkeymaxes = []
AMLtvalmaxes = []
for key in AMLtvalue:
    if len(AMLtvalkeymaxes) < 50:
        AMLtvalmaxes.append(AMLtvalue[key])
        AMLtvalkeymaxes.append(key)
    else:
        minvalue = min(AMLtvalmaxes)
        mindex = AMLtvalmaxes.index(minvalue)
        if AMLtvalue[key] > minvalue:
            AMLtvalmaxes[mindex] = AMLtvalue[key]
            AMLtvalkeymaxes[mindex] = key

ALLcombined = []
for i in ALLs2nkeymaxes:
    if i in ALLtvalkeymaxes:
        ALLcombined.append(i)
AMLcombined = []
for j in AMLs2nkeymaxes:
    if j in AMLtvalkeymaxes:
        AMLcombined.append(j)

ALLs2ntop3num = []
ALLs2ntop3key = []
for i in range(len(ALLs2nmaxes)):
    if len(ALLs2ntop3num) < 3:
        ALLs2ntop3num.append(ALLs2nmaxes[i])
        ALLs2ntop3key.append(ALLs2nkeymaxes[i])
    else:
        minvalue = min(ALLs2ntop3num)
        mindex = ALLs2ntop3num.index(minvalue)
        if ALLs2nmaxes[i] > minvalue:
            ALLs2ntop3num[mindex] = ALLs2nmaxes[i]
            ALLs2ntop3key[mindex] = ALLs2nkeymaxes[i]

ALLtvaltop3num = []
ALLtvaltop3key = []
for i in range(len(ALLtvalmaxes)):
    if len(ALLtvaltop3num) < 3:
        ALLtvaltop3num.append(ALLtvalmaxes[i])
        ALLtvaltop3key.append(ALLtvalkeymaxes[i])
    else:
        minvalue = min(ALLtvaltop3num)
        mindex = ALLtvaltop3num.index(minvalue)
        if ALLtvalmaxes[i] > minvalue:
            ALLtvaltop3num[mindex] = ALLtvalmaxes[i]
            ALLtvaltop3key[mindex] = ALLtvalkeymaxes[i]

AMLs2ntop3num = []
AMLs2ntop3key = []
for i in range(len(AMLs2nmaxes)):
    if len(AMLs2ntop3num) < 3:
        AMLs2ntop3num.append(AMLs2nmaxes[i])
        AMLs2ntop3key.append(AMLs2nkeymaxes[i])
    else:
        minvalue = min(AMLs2ntop3num)
        mindex = AMLs2ntop3num.index(minvalue)
        if AMLs2nmaxes[i] > minvalue:
            AMLs2ntop3num[mindex] = AMLs2nmaxes[i]
            AMLs2ntop3key[mindex] = AMLs2nkeymaxes[i]

AMLtvaltop3num = []
AMLtvaltop3key = []
for i in range(len(AMLtvalmaxes)):
    if len(AMLtvaltop3num) < 3:
        AMLtvaltop3num.append(AMLtvalmaxes[i])
        AMLtvaltop3key.append(AMLtvalkeymaxes[i])
    else:
        minvalue = min(AMLtvaltop3num)
        mindex = AMLtvaltop3num.index(minvalue)
        if AMLtvalmaxes[i] > minvalue:
            AMLtvaltop3num[mindex] = AMLtvalmaxes[i]
            AMLtvaltop3key[mindex] = AMLtvalkeymaxes[i]

lte2 = []
b2and4 = []
b4and8 = []
b8and16 = []
b16and32 = []
b32and64 = []
b64and128 = []
b128and256 = []
b256and512 = []
gt512 = []

for key in foldratios:
    if foldratios[key] <= 2:
        lte2.append(key)
    if 2 < foldratios[key] <= 4:
        b2and4.append(key)
    if 4 < foldratios[key] <= 8:
        b4and8.append(key)
    if 8 < foldratios[key] <= 16:
        b8and16.append(key)
    if 16 < foldratios[key] <= 32:
        b16and32.append(key)
    if 32 < foldratios[key] <= 64:
        b32and64.append(key)
    if 64 < foldratios[key] <= 128:
        b64and128.append(key)
    if 128 < foldratios[key] <= 256:
        b128and256.append(key)
    if 256 < foldratios[key] <= 512:
        b256and512.append(key)
    if foldratios[key] > 512:
        gt512.append(key)

print('\nRESULTS: \n')
print('Largest fold ratio: ', valmax)
print('Keys with max fold ratio: ', len(keymaxes), '\n')
print('Smallest fold ratio: ', valmin)
print('Keys with min fold ratio: ', len(keymins), '\n')
print('Number of items in each fold ratio: ')
print('FR <= 2: ', len(lte2))
print('2 < FR <= 4: ', len(b2and4))
print('4 < FR <= 8: ', len(b4and8))
print('8 < FR <= 16: ', len(b8and16))
print('16 < FR <= 32: ', len(b16and32))
print('32 < FR <= 64: ', len(b32and64))
print('64 < FR <= 128: ', len(b64and128))
print('128 < FR <= 256: ', len(b128and256))
print('256 < FR <= 512: ', len(b256and512))
print('512 < FR: ', len(gt512), '\n')
print('\nGreatest 50 ALL s2n values and gene names. Each list is is order so the first corresponds to the first in the other list and so on:\n')
print(ALLs2nmaxes)
print(ALLs2nkeymaxes)
print('\n1st value:', ALLs2nkeymaxes[ALLs2nmaxes.index(max(ALLs2nmaxes))], '---', max(ALLs2nmaxes))
print('50th value:', ALLs2nkeymaxes[ALLs2nmaxes.index(min(ALLs2nmaxes))], '---', min(ALLs2nmaxes))
print('\nAML values --------------------')
print(AMLs2nmaxes)
print(AMLs2nkeymaxes)
print('\n1st value:', AMLs2nkeymaxes[AMLs2nmaxes.index(max(AMLs2nmaxes))], '---', max(AMLs2nmaxes))
print('50th value:', AMLs2nkeymaxes[AMLs2nmaxes.index(min(AMLs2nmaxes))], '---', min(AMLs2nmaxes))
print('\n\nGreatest 50 ALL t values and gene names. Same order:\n')
print(ALLtvalmaxes)
print(ALLtvalkeymaxes)
print('\n1st value:', ALLtvalkeymaxes[ALLtvalmaxes.index(max(ALLtvalmaxes))], '---', max(ALLtvalmaxes))
print('50th value:', ALLtvalkeymaxes[ALLtvalmaxes.index(min(ALLtvalmaxes))], '---', min(ALLtvalmaxes))
print('\nAML ---------------------------')
print(AMLtvalmaxes)
print(AMLtvalkeymaxes)
print('\n1st value:', AMLtvalkeymaxes[AMLtvalmaxes.index(max(AMLtvalmaxes))], '---', max(AMLtvalmaxes))
print('50th value:', AMLtvalkeymaxes[AMLtvalmaxes.index(min(AMLtvalmaxes))], '---', min(AMLtvalmaxes))
print('\n# of top 50 ALL genes in s2n and t value:', len(ALLcombined))
print('# of top 50 AML genes in s2n and t value:', len(AMLcombined))
print('\nTop 3 ALL s2n:', ALLs2ntop3num, ALLs2ntop3key)
print('\nTop 3 ALL tval:', ALLtvaltop3num, ALLtvaltop3key)
print('\nTop 3 AML s2n:', AMLs2ntop3num, AMLs2ntop3key)
print('\nTop 3 AML tval:', AMLtvaltop3num, AMLtvaltop3key)