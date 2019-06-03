# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:16:28 2019

@author: Meed Ubarab
"""

#importing panda for csv and excel data reading
import pandas as pd

#importing datetime module for retrieving date of submission
from datetime import datetime

#report information
reportName = 'ABMS104'
reportDescription = 'FI and MMO RETURN ON AGENT ACTIVITY'

#getting current date of submission
todaysDate = datetime.today().strftime('%d-%m-%Y')

#saving information for Contec Global
institutionName = 'Contec Global'
FICode = 100032


#checking if file exists
while True:
    try:
        #geting the data file
        fileName = input('Enter filename>>  ')
        
        
        #creating link to csv file on folder
        csvFile = fileName.upper()+'.csv'
        
        #setting for xml file creation
        newFilename = "%s.xml" % fileName
        
        
        #creating an empty xml file
        xmlFile = open(newFilename, 'w')
        df = pd.read_csv(csvFile, sep=',')
        break
    except:
        print("It looks like the file doesn't exist. Check and Try again")
        continue



#header script
header="""<?xml version="1.0" encoding="utf-8"?>
    <CALLREPORT>
      <HEADER>
        <CALLREPORT_ID>%s</CALLREPORT_ID>
        <CALLREPORT_DESC>%s</CALLREPORT_DESC>
        <INST_CODE>%s</INST_CODE>
        <INST_NAME>%s</INST_NAME>
        <AS_AT>%s</AS_AT>
      </HEADER>
      <BODY>""" % (reportName, reportDescription, FICode, institutionName, todaysDate)
      

#footer script
footer ="""\n</BODY>
</CALLREPORT>"""


#body xml tag converter function
def getLGACode(row):
    lga = row.LGA
    lgaCode = 0
    try:
        if lga == "Ibiono-Ibom":
            lgaCode = 48
        if lga == "Ika":
            lgaCode = 49
        if lga == "Ikono":
            lgaCode = 50
        if lga == "Ikot Abasi":
            lgaCode = 51
        if lga == "Ikot Ekpene":
            lgaCode = 52
        if lga == "Ini":
            lgaCode = 53
        if lga == "Itu":
            lgaCode = 54
        if lga == "Mbo":
            lgaCode = 55
        if lga == "Mkpat-Enin":
            lgaCode = 56
        if lga == "Nsit-Atai":
            lgaCode = 57
        if lga == "Nsit-Ibom":
            lgaCode = 58
        if lga == "Nsit-Ubium":
            lgaCode = 59
        if lga == "Obot Akara":
            lgaCode = 60
        if lga == "Okobo":
            lgaCode = 61
        if lga == "Onna":
            lgaCode = 62
        if lga == "Oron":
            lgaCode = 63
        if lga == "Oruk Anam":
            lgaCode = 64
        if lga == "Udung-Uko":
            lgaCode = 65
        if lga == "Ukanafun":
            lgaCode = 66
        if lga == "Uruan":
            lgaCode = 67
        if lga == "Urue-Offong/Oruko":
            lgaCode = 68
        if lga == "Uyo":
            lgaCode = 69
        if lga == "Aguata":
            lgaCode = 70
        if lga == "Anambra East":
            lgaCode = 71
        if lga == "Anambra West":
            lgaCode = 72
        if lga == "Anaocha":
            lgaCode = 73
        if lga == "Awka North":
            lgaCode = 74
        if lga == "Awka South":
            lgaCode = 75
        if lga == "Ayamelum":
            lgaCode = 76
        if lga == "Dunukofia":
            lgaCode = 77
        if lga == "Ekwusigo":
            lgaCode = 78
        if lga == "Idemili North":
            lgaCode = 79
        if lga == "Idemili South":
            lgaCode = 80
        if lga == "Ihiala":
            lgaCode = 81
        if lga == "Njikoka":
            lgaCode = 82
        if lga == "Nnewi North":
            lgaCode = 83
        if lga == "Nnewi South":
            lgaCode = 84
        if lga == "Ogbaru":
            lgaCode = 85
        if lga == "Onitsha North":
            lgaCode = 86
        if lga == "Onitsha South":
            lgaCode = 87
        if lga == "Orumba North":
            lgaCode = 88
        if lga == "Orumba South":
            lgaCode = 89
        if lga == "Oyi":
            lgaCode = 90
        if lga == "Alkaleri":
            lgaCode = 91
        if lga == "Bauchi":
            lgaCode = 92
        if lga == "Bogoro":
            lgaCode = 93
        if lga == "Damban":
            lgaCode = 94
        if lga == "Darazo":
            lgaCode = 95
        if lga == "Dass":
            lgaCode = 96
        if lga == "Gamawa":
            lgaCode = 97
        if lga == "Ganjuwa":
            lgaCode = 98
        if lga == "Giade":
            lgaCode = 99
        if lga == "Itas/Gadau":
            lgaCode = 100
        if lga == "Jama'are":
            lgaCode = 101
        if lga == "Katagum":
            lgaCode = 102
        if lga == "Kirfi":
            lgaCode = 103
        if lga == "Misau":
            lgaCode = 104
        if lga == "Ningi":
            lgaCode = 105
        if lga == "Shira":
            lgaCode = 106
        if lga == "Tafawa Balewa":
            lgaCode = 107
        if lga == "Toro":
            lgaCode = 108
        if lga == "Warji":
            lgaCode = 109
        if lga == "Zaki":
            lgaCode = 110
        if lga == "Brass":
            lgaCode = 111
        if lga == "Ekeremor":
            lgaCode = 112
        if lga == "Kolokuma/Opokuma":
            lgaCode = 113
        if lga == "Nembe":
            lgaCode = 114
        if lga == "Ogbia":
            lgaCode = 115
        if lga == "Sagbama":
            lgaCode = 116
        if lga == "Southern Ijaw":
            lgaCode = 117
        if lga == "Yenagoa":
            lgaCode = 118
        if lga == "Ado":
            lgaCode = 119
        if lga == "Agatu":
            lgaCode = 120
        if lga == "Apa":
            lgaCode = 121
        if lga == "Buruku":
            lgaCode = 122
        if lga == "Gboko":
            lgaCode = 123
        if lga == "Guma":
            lgaCode = 124
        if lga == "Gwer East":
            lgaCode = 125
        if lga == "Gwer West":
            lgaCode = 126
        if lga == "Katsina-Ala":
            lgaCode = 127
        if lga == "Konshisha":
            lgaCode = 128
        if lga == "Kwande":
            lgaCode = 129
        if lga == "Logo":
            lgaCode = 130
        if lga == "Makurdi":
            lgaCode = 131
        if lga == "Obi":
            lgaCode = 132
        if lga == "Ogbadibo":
            lgaCode = 133
        if lga == "Ohimini":
            lgaCode = 134
        if lga == "Oju":
            lgaCode = 135
        if lga == "Okpokwu":
            lgaCode = 136
        if lga == "Oturkpo":
            lgaCode = 137
        if lga == "Tarka":
            lgaCode = 138
        if lga == "Ukum":
            lgaCode = 139
        if lga == "Ushongo":
            lgaCode = 140
        if lga == "Vandeikya":
            lgaCode = 141
        if lga == "Abadam":
            lgaCode = 142
        if lga == "Askira/Uba":
            lgaCode = 143
        if lga == "Bama":
            lgaCode = 144
        if lga == "Bayo":
            lgaCode = 145
        if lga == "Biu":
            lgaCode = 146
        if lga == "Chibok":
            lgaCode = 147
        if lga == "Damboa":
            lgaCode = 148
        if lga == "Dikwa":
            lgaCode = 149
        if lga == "Gubio":
            lgaCode = 150
        if lga == "Guzamala":
            lgaCode = 151
        if lga == "Gwoza":
            lgaCode = 152
        if lga == "Hawul":
            lgaCode = 153
        if lga == "Jere":
            lgaCode = 154
        if lga == "Kaga":
            lgaCode = 155
        if lga == "Kala/Balge":
            lgaCode = 156
        if lga == "Konduga":
            lgaCode = 157
        if lga == "Kukawa":
            lgaCode = 158
        if lga == "Kwaya Kusar":
            lgaCode = 159
        if lga == "Mafa":
            lgaCode = 160
        if lga == "Magumeri":
            lgaCode = 161
        if lga == "Maiduguri":
            lgaCode = 162
        if lga == "Marte":
            lgaCode = 163
        if lga == "Mobbar":
            lgaCode = 164
        if lga == "Monguno":
            lgaCode = 165
        if lga == "Ngala":
            lgaCode = 166
        if lga == "Nganzai":
            lgaCode = 167
        if lga == "Shani":
            lgaCode = 168
        if lga == "Abi":
            lgaCode = 169
        if lga == "Akamkpa":
            lgaCode = 170
        if lga == "Akpabuyo":
            lgaCode = 171
        if lga == "Bakassi":
            lgaCode = 172
        if lga == "Bekwarra":
            lgaCode = 173
        if lga == "Biase":
            lgaCode = 174
        if lga == "Boki":
            lgaCode = 175
        if lga == "Calabar Municipal":
            lgaCode = 176
        if lga == "Calabar South":
            lgaCode = 177
        if lga == "Etung":
            lgaCode = 178
        if lga == "Ikom":
            lgaCode = 179
        if lga == "Obanliku":
            lgaCode = 180
        if lga == "Obubra":
            lgaCode = 181
        if lga == "Obudu":
            lgaCode = 182
        if lga == "Odukpani":
            lgaCode = 183
        if lga == "Ogoja":
            lgaCode = 184
        if lga == "Yakuur":
            lgaCode = 185
        if lga == "Yala":
            lgaCode = 186
        if lga == "Aniocha North":
            lgaCode = 187
        if lga == "Aniocha South":
            lgaCode = 188
        if lga == "Bomadi":
            lgaCode = 189
        if lga == "Burutu":
            lgaCode = 190
        if lga == "Ethiope East":
            lgaCode = 191
        if lga == "Ethiope West":
            lgaCode = 192
        if lga == "Ika North East":
            lgaCode = 193
        if lga == "Ika South":
            lgaCode = 194
        if lga == "Isoko North":
            lgaCode = 195
        if lga == "Isoko South":
            lgaCode = 196
        if lga == "Ndokwa East":
            lgaCode = 197
        if lga == "Ndokwa West":
            lgaCode = 198
        if lga == "Okpe":
            lgaCode = 199
        if lga == "Oshimili North":
            lgaCode = 200
        if lga == "Oshimili South":
            lgaCode = 201
        if lga == "Patani":
            lgaCode = 202
        if lga == "Sapele":
            lgaCode = 203
        if lga == "Udu":
            lgaCode = 204
        if lga == "Ughelli North":
            lgaCode = 205
        if lga == "Ughelli South":
            lgaCode = 206
        if lga == "Ukwuani":
            lgaCode = 207
        if lga == "Uvwie":
            lgaCode = 208
        if lga == "Warri North":
            lgaCode = 209
        if lga == "Warri South":
            lgaCode = 210
        if lga == "Warri South West":
            lgaCode = 211
        if lga == "Abakaliki":
            lgaCode = 212
        if lga == "Afikpo North":
            lgaCode = 213
        if lga == "Afikpo South (Edda)":
            lgaCode = 214
        if lga == "Ebonyi":
            lgaCode = 215
        if lga == "Ezza North":
            lgaCode = 216
        if lga == "Ezza South":
            lgaCode = 217
        if lga == "Ikwo":
            lgaCode = 218
        if lga == "Ishielu":
            lgaCode = 219
        if lga == "Ivo":
            lgaCode = 220
        if lga == "Izzi":
            lgaCode = 221
        if lga == "Ohaozara":
            lgaCode = 222
        if lga == "Ohaukwu":
            lgaCode = 223
        if lga == "Onicha":
            lgaCode = 224
        if lga == "Akoko-Edo":
            lgaCode = 225
        if lga == "Egor":
            lgaCode = 226
        if lga == "Esan Central":
            lgaCode = 227
        if lga == "Esan North-East":
            lgaCode = 228
        if lga == "Esan South-East":
            lgaCode = 229
        if lga == "Esan West":
            lgaCode = 230
        if lga == "Etsako Central":
            lgaCode = 231
        if lga == "Etsako East":
            lgaCode = 232
        if lga == "Etsako West":
            lgaCode = 233
        if lga == "Igueben":
            lgaCode = 234
        if lga == "Ikpoba Okha":
            lgaCode = 235
        if lga == "Oredo":
            lgaCode = 236
        if lga == "Orhionmwon":
            lgaCode = 237
        if lga == "Ovia North-East":
            lgaCode = 238
        if lga == "Ovia South-West":
            lgaCode = 239
        if lga == "Owan East":
            lgaCode = 240
        if lga == "Owan West":
            lgaCode = 241
        if lga == "Uhunmwonde":
            lgaCode = 242
        if lga == "Ado Ekiti":
            lgaCode = 243
        if lga == "Efon":
            lgaCode = 244
        if lga == "Ekiti East":
            lgaCode = 245
        if lga == "Ekiti South-West":
            lgaCode = 246
        if lga == "Ekiti West":
            lgaCode = 247
        if lga == "Emure":
            lgaCode = 248
        if lga == "Gbonyin":
            lgaCode = 249
        if lga == "Ido Osi":
            lgaCode = 250
        if lga == "Ijero":
            lgaCode = 251
        if lga == "Ikere":
            lgaCode = 252
        if lga == "Ikole":
            lgaCode = 253
        if lga == "Ilejemeje":
            lgaCode = 254
        if lga == "Irepodun/Ifelodun":
            lgaCode = 255
        if lga == "Ise/Orun":
            lgaCode = 256
        if lga == "Moba":
            lgaCode = 257
        if lga == "Oye":
            lgaCode = 258
        if lga == "Aninri":
            lgaCode = 259
        if lga == "Awgu":
            lgaCode = 260
        if lga == "Enugu East":
            lgaCode = 261
        if lga == "Enugu North":
            lgaCode = 262
        if lga == "Enugu South":
            lgaCode = 263
        if lga == "Ezeagu":
            lgaCode = 264
        if lga == "Igbo Etiti":
            lgaCode = 265
        if lga == "Igbo Eze North":
            lgaCode = 266
        if lga == "Igbo Eze South":
            lgaCode = 267
        if lga == "Isi Uzo":
            lgaCode = 268
        if lga == "Nkanu East":
            lgaCode = 269
        if lga == "Nkanu West":
            lgaCode = 270
        if lga == "Nsukka":
            lgaCode = 271
        if lga == "Oji River":
            lgaCode = 272
        if lga == "Udenu":
            lgaCode = 273
        if lga == "Udi":
            lgaCode = 274
        if lga == "Uzo-Uwani":
            lgaCode = 275
        if lga == "Abaji":
            lgaCode = 276
        if lga == "Bwari":
            lgaCode = 277
        if lga == "Gwagwalada":
            lgaCode = 278
        if lga == "Kuje":
            lgaCode = 279
        if lga == "Kwali":
            lgaCode = 280
        if lga == "ABUJA Municipal Area Council":
            lgaCode = 281
        if lga == "Akko":
            lgaCode = 282
        if lga == "Balanga":
            lgaCode = 283
        if lga == "Billiri":
            lgaCode = 284
        if lga == "Dukku":
            lgaCode = 285
        if lga == "Funakaye":
            lgaCode = 286
        if lga == "Gombe":
            lgaCode = 287
        if lga == "Kaltungo":
            lgaCode = 288
        if lga == "Kwami":
            lgaCode = 289
        if lga == "Nafada":
            lgaCode = 290
        if lga == "Shongom":
            lgaCode = 291
        if lga == "Yamaltu/Deba":
            lgaCode = 292
        if lga == "Aboh Mbaise":
            lgaCode = 293
        if lga == "Ahiazu Mbaise":
            lgaCode = 294
        if lga == "Ehime Mbano":
            lgaCode = 295
        if lga == "Ezinihitte":
            lgaCode = 296
        if lga == "Ideato North":
            lgaCode = 297
        if lga == "Ideato South":
            lgaCode = 298
        if lga == "Ihitte/Uboma":
            lgaCode = 299
        if lga == "Ikeduru":
            lgaCode = 300
        if lga == "Isiala Mbano":
            lgaCode = 301
        if lga == "Isu":
            lgaCode = 302
        if lga == "Mbaitoli":
            lgaCode = 303
        if lga == "Ngor Okpala":
            lgaCode = 304
        if lga == "Njaba":
            lgaCode = 305
        if lga == "Nkwerre":
            lgaCode = 306
        if lga == "Nwangele":
            lgaCode = 307
        if lga == "Obowo":
            lgaCode = 308
        if lga == "Oguta":
            lgaCode = 309
        if lga == "Ohaji/Egbema":
            lgaCode = 310
        if lga == "Okigwe":
            lgaCode = 311
        if lga == "Orlu":
            lgaCode = 312
        if lga == "Orsu":
            lgaCode = 313
        if lga == "Oru East":
            lgaCode = 314
        if lga == "Oru West":
            lgaCode = 315
        if lga == "Owerri Municipal":
            lgaCode = 316
        if lga == "Owerri North":
            lgaCode = 317
        if lga == "Owerri West":
            lgaCode = 318
        if lga == "Unuimo":
            lgaCode = 319
        if lga == "Auyo":
            lgaCode = 320
        if lga == "Babura":
            lgaCode = 321
        if lga == "Biriniwa":
            lgaCode = 322
        if lga == "Birnin Kudu":
            lgaCode = 323
        if lga == "Buji":
            lgaCode = 324
        if lga == "Dutse":
            lgaCode = 325
        if lga == "Gagarawa":
            lgaCode = 326
        if lga == "Garki":
            lgaCode = 327
        if lga == "Gumel":
            lgaCode = 328
        if lga == "Guri":
            lgaCode = 329
        if lga == "Gwaram":
            lgaCode = 330
        if lga == "Gwiwa":
            lgaCode = 331
        if lga == "Hadejia":
            lgaCode = 332
        if lga == "Jahun":
            lgaCode = 333
        if lga == "Kafin Hausa":
            lgaCode = 334
        if lga == "Kaugama":
            lgaCode = 335
        if lga == "Kazaure":
            lgaCode = 336
        if lga == "Kiri Kasama":
            lgaCode = 337
        if lga == "Kiyawa":
            lgaCode = 338
        if lga == "Maigatari":
            lgaCode = 339
        if lga == "Malam Madori":
            lgaCode = 340
        if lga == "Miga":
            lgaCode = 341
        if lga == "Ringim":
            lgaCode = 342
        if lga == "Roni":
            lgaCode = 343
        if lga == "Sule Tankarkar":
            lgaCode = 344
        if lga == "Taura":
            lgaCode = 345
        if lga == "Yankwashi":
            lgaCode = 346
        if lga == "Birnin Gwari":
            lgaCode = 347
        if lga == "Chikun":
            lgaCode = 348
        if lga == "Giwa":
            lgaCode = 349
        if lga == "Igabi":
            lgaCode = 350
        if lga == "Ikara":
            lgaCode = 351
        if lga == "Jaba":
            lgaCode = 352
        if lga == "Jema'a":
            lgaCode = 353
        if lga == "Kachia":
            lgaCode = 354
        if lga == "Kaduna North":
            lgaCode = 355
        if lga == "Kaduna South":
            lgaCode = 356
        if lga == "Kagarko":
            lgaCode = 357
        if lga == "Kajuru":
            lgaCode = 358
        if lga == "Kaura":
            lgaCode = 359
        if lga == "Kauru":
            lgaCode = 360
        if lga == "Kubau":
            lgaCode = 361
        if lga == "Kudan":
            lgaCode = 362
        if lga == "Lere":
            lgaCode = 363
        if lga == "Makarfi":
            lgaCode = 364
        if lga == "Sabon Gari":
            lgaCode = 365
        if lga == "Sanga":
            lgaCode = 366
        if lga == "Soba":
            lgaCode = 367
        if lga == "Zangon Kataf":
            lgaCode = 368
        if lga == "Zaria":
            lgaCode = 369
        if lga == "Ajingi":
            lgaCode = 370
        if lga == "Albasu":
            lgaCode = 371
        if lga == "Bagwai":
            lgaCode = 372
        if lga == "Bebeji":
            lgaCode = 373
        if lga == "Bichi":
            lgaCode = 374
        if lga == "Bunkure":
            lgaCode = 375
        if lga == "Dala":
            lgaCode = 376
        if lga == "Dambatta":
            lgaCode = 377
        if lga == "Dawakin Kudu":
            lgaCode = 378
        if lga == "Dawakin Tofa":
            lgaCode = 379
        if lga == "Doguwa":
            lgaCode = 380
        if lga == "Fagge":
            lgaCode = 381
        if lga == "Gabasawa":
            lgaCode = 382
        if lga == "Garko":
            lgaCode = 383
        if lga == "Garun Mallam":
            lgaCode = 384
        if lga == "Gaya":
            lgaCode = 385
        if lga == "Gezawa":
            lgaCode = 386
        if lga == "Gwale":
            lgaCode = 387
        if lga == "Gwarzo":
            lgaCode = 388
        if lga == "Kabo":
            lgaCode = 389
        if lga == "Kano Municipal":
            lgaCode = 390
        if lga == "Karaye":
            lgaCode = 391
        if lga == "Kibiya":
            lgaCode = 392
        if lga == "Kiru":
            lgaCode = 393
        if lga == "Kumbotso":
            lgaCode = 394
        if lga == "Kunchi":
            lgaCode = 395
        if lga == "Kura":
            lgaCode = 396
        if lga == "Madobi":
            lgaCode = 397
        if lga == "Makoda":
            lgaCode = 398
        if lga == "Minjibir":
            lgaCode = 399
        if lga == "Nasarawa":
            lgaCode = 400
        if lga == "Rano":
            lgaCode = 401
        if lga == "Rimin Gado":
            lgaCode = 402
        if lga == "Rogo":
            lgaCode = 403
        if lga == "Shanono":
            lgaCode = 404
        if lga == "Sumaila":
            lgaCode = 405
        if lga == "Takai":
            lgaCode = 406
        if lga == "Tarauni":
            lgaCode = 407
        if lga == "Tofa":
            lgaCode = 408
        if lga == "Tsanyawa":
            lgaCode = 409
        if lga == "Tudun Wada":
            lgaCode = 410
        if lga == "Ungogo":
            lgaCode = 411
        if lga == "Warawa":
            lgaCode = 412
        if lga == "Wudil":
            lgaCode = 413
        if lga == "Bakori":
            lgaCode = 414
        if lga == "Batagarawa":
            lgaCode = 415
        if lga == "Batsari":
            lgaCode = 416
        if lga == "Baure":
            lgaCode = 417
        if lga == "Bindawa":
            lgaCode = 418
        if lga == "Charanchi":
            lgaCode = 419
        if lga == "Dan Musa":
            lgaCode = 420
        if lga == "Dandume":
            lgaCode = 421
        if lga == "Danja":
            lgaCode = 422
        if lga == "Daura":
            lgaCode = 423
        if lga == "Dutsi":
            lgaCode = 424
        if lga == "Dutsin Ma":
            lgaCode = 425
        if lga == "Faskari":
            lgaCode = 426
        if lga == "Funtua":
            lgaCode = 427
        if lga == "Ingawa":
            lgaCode = 428
        if lga == "Jibia":
            lgaCode = 429
        if lga == "Kafur":
            lgaCode = 430
        if lga == "Kaita":
            lgaCode = 431
        if lga == "Kankara":
            lgaCode = 432
        if lga == "Kankia":
            lgaCode = 433
        if lga == "Katsina":
            lgaCode = 434
        if lga == "Kurfi":
            lgaCode = 435
        if lga == "Kusada":
            lgaCode = 436
        if lga == "Mai'Adua":
            lgaCode = 437
        if lga == "Malumfashi":
            lgaCode = 438
        if lga == "Mani":
            lgaCode = 439
        if lga == "Mashi":
            lgaCode = 440
        if lga == "Matazu":
            lgaCode = 441
        if lga == "Musawa":
            lgaCode = 442
        if lga == "Rimi":
            lgaCode = 443
        if lga == "Sabuwa":
            lgaCode = 444
        if lga == "Safana":
            lgaCode = 445
        if lga == "Sandamu":
            lgaCode = 446
        if lga == "Zango":
            lgaCode = 447
        if lga == "Aleiro":
            lgaCode = 448
        if lga == "Arewa Dandi":
            lgaCode = 449
        if lga == "Argungu":
            lgaCode = 450
        if lga == "Augie":
            lgaCode = 451
        if lga == "Bagudo":
            lgaCode = 452
        if lga == "Birnin Kebbi":
            lgaCode = 453
        if lga == "Bunza":
            lgaCode = 454
        if lga == "Dandi":
            lgaCode = 455
        if lga == "Fakai":
            lgaCode = 456
        if lga == "Gwandu":
            lgaCode = 457
        if lga == "Jega":
            lgaCode = 458
        if lga == "Kalgo":
            lgaCode = 459
        if lga == "Koko/Besse":
            lgaCode = 460
        if lga == "Maiyama":
            lgaCode = 461
        if lga == "Ngaski":
            lgaCode = 462
        if lga == "Sakaba":
            lgaCode = 463
        if lga == "Shanga":
            lgaCode = 464
        if lga == "Suru":
            lgaCode = 465
        if lga == "Wasagu/Danko":
            lgaCode = 466
        if lga == "Yauri":
            lgaCode = 467
        if lga == "Zuru":
            lgaCode = 468
        if lga == "Adavi":
            lgaCode = 469
        if lga == "Ajaokuta":
            lgaCode = 470
        if lga == "Ankpa":
            lgaCode = 471
        if lga == "Bassa":
            lgaCode = 472
        if lga == "Dekina":
            lgaCode = 473
        if lga == "Ibaji":
            lgaCode = 474
        if lga == "Idah":
            lgaCode = 475
        if lga == "Igalamela Odolu":
            lgaCode = 476
        if lga == "Ijumu":
            lgaCode = 477
        if lga == "Kabba/Bunu":
            lgaCode = 478
        if lga == "Kogi":
            lgaCode = 479
        if lga == "Lokoja":
            lgaCode = 480
        if lga == "Mopa Muro":
            lgaCode = 481
        if lga == "Ofu":
            lgaCode = 482
        if lga == "Ogori/Magongo":
            lgaCode = 483
        if lga == "Okehi":
            lgaCode = 484
        if lga == "Okene":
            lgaCode = 485
        if lga == "Olamaboro":
            lgaCode = 486
        if lga == "Omala":
            lgaCode = 487
        if lga == "Yagba East":
            lgaCode = 488
        if lga == "Yagba West":
            lgaCode = 489
        if lga == "Asa":
            lgaCode = 490
        if lga == "Baruten":
            lgaCode = 491
        if lga == "Edu":
            lgaCode = 492
        if lga == "Ekiti":
            lgaCode = 493
        if lga == "Ifelodun":
            lgaCode = 494
        if lga == "Ilorin East":
            lgaCode = 495
        if lga == "Ilorin South":
            lgaCode = 496
        if lga == "Ilorin West":
            lgaCode = 497
        if lga == "Irepodun":
            lgaCode = 498
        if lga == "Isin":
            lgaCode = 499
        if lga == "Kaiama":
            lgaCode = 500
        if lga == "Moro":
            lgaCode = 501
        if lga == "Offa":
            lgaCode = 502
        if lga == "Oke Ero":
            lgaCode = 503
        if lga == "Oyun":
            lgaCode = 504
        if lga == "Pategi":
            lgaCode = 505
        if lga == "Agege":
            lgaCode = 506
        if lga == "Ajeromi-Ifelodun":
            lgaCode = 507
        if lga == "Alimosho":
            lgaCode = 508
        if lga == "Amuwo-Odofin":
            lgaCode = 509
        if lga == "Apapa":
            lgaCode = 510
        if lga == "Badagry":
            lgaCode = 511
        if lga == "Epe":
            lgaCode = 512
        if lga == "Eti Osa":
            lgaCode = 513
        if lga == "Ibeju-Lekki":
            lgaCode = 514
        if lga == "Ifako-Ijaiye":
            lgaCode = 515
        if lga == "Ikeja":
            lgaCode = 516
        if lga == "Ikorodu":
            lgaCode = 517
        if lga == "Kosofe":
            lgaCode = 518
        if lga == "Lagos Island":
            lgaCode = 519
        if lga == "Lagos Mainland":
            lgaCode = 520
        if lga == "Mushin":
            lgaCode = 521
        if lga == "Ojo":
            lgaCode = 522
        if lga == "Oshodi-Isolo":
            lgaCode = 523
        if lga == "Shomolu":
            lgaCode = 524
        if lga == "Surulere":
            lgaCode = 525
        if lga == "Akwanga":
            lgaCode = 526
        if lga == "Awe":
            lgaCode = 527
        if lga == "Doma":
            lgaCode = 528
        if lga == "Karu":
            lgaCode = 529
        if lga == "Keana":
            lgaCode = 530
        if lga == "Keffi":
            lgaCode = 531
        if lga == "Kokona":
            lgaCode = 532
        if lga == "Lafia":
            lgaCode = 533
        if lga == "Nasarawa":
            lgaCode = 534
        if lga == "Nasarawa Egon":
            lgaCode = 535
        if lga == "Obi":
            lgaCode = 536
        if lga == "Toto":
            lgaCode = 537
        if lga == "Wamba":
            lgaCode = 538
        if lga == "Agaie":
            lgaCode = 539
        if lga == "Agwara":
            lgaCode = 540
        if lga == "Bida":
            lgaCode = 541
        if lga == "Borgu":
            lgaCode = 542
        if lga == "Bosso":
            lgaCode = 543
        if lga == "Chanchaga":
            lgaCode = 544
        if lga == "Edati":
            lgaCode = 545
        if lga == "Gbako":
            lgaCode = 546
        if lga == "Gurara":
            lgaCode = 547
        if lga == "Katcha":
            lgaCode = 548
        if lga == "Kontagora":
            lgaCode = 549
        if lga == "Lapai":
            lgaCode = 550
        if lga == "Lavun":
            lgaCode = 551
        if lga == "Magama":
            lgaCode = 552
        if lga == "Mariga":
            lgaCode = 553
        if lga == "Mashegu":
            lgaCode = 554
        if lga == "Mokwa":
            lgaCode = 555
        if lga == "Moya":
            lgaCode = 556
        if lga == "Paikoro":
            lgaCode = 557
        if lga == "Rafi":
            lgaCode = 558
        if lga == "Rijau":
            lgaCode = 559
        if lga == "Shiroro":
            lgaCode = 560
        if lga == "Suleja":
            lgaCode = 561
        if lga == "Tafa":
            lgaCode = 562
        if lga == "Wushishi":
            lgaCode = 563
        if lga == "Abeokuta North":
            lgaCode = 564
        if lga == "Abeokuta South":
            lgaCode = 565
        if lga == "Ado-Odo/Ota":
            lgaCode = 566
        if lga == "Ewekoro":
            lgaCode = 567
        if lga == "Ifo":
            lgaCode = 568
        if lga == "Ijebu East":
            lgaCode = 569
        if lga == "Ijebu North":
            lgaCode = 570
        if lga == "Ijebu North East":
            lgaCode = 571
        if lga == "Ijebu Ode":
            lgaCode = 572
        if lga == "Ikenne":
            lgaCode = 573
        if lga == "Imeko Afon":
            lgaCode = 574
        if lga == "Ipokia":
            lgaCode = 575
        if lga == "Obafemi Owode":
            lgaCode = 576
        if lga == "Odeda":
            lgaCode = 577
        if lga == "Odogbolu":
            lgaCode = 578
        if lga == "Ogun Waterside":
            lgaCode = 579
        if lga == "Remo North":
            lgaCode = 580
        if lga == "Shagamu":
            lgaCode = 581
        if lga == "Yewa North":
            lgaCode = 582
        if lga == "Yewa South":
            lgaCode = 583
        if lga == "Akoko North-East":
            lgaCode = 584
        if lga == "Akoko North-West":
            lgaCode = 585
        if lga == "Akoko South-East":
            lgaCode = 586
        if lga == "Akoko South-West":
            lgaCode = 587
        if lga == "Akure North":
            lgaCode = 588
        if lga == "Akure South":
            lgaCode = 589
        if lga == "Ese Odo":
            lgaCode = 590
        if lga == "Idanre":
            lgaCode = 591
        if lga == "Ifedore":
            lgaCode = 592
        if lga == "Ilaje":
            lgaCode = 593
        if lga == "Ile Oluji/Okeigbo":
            lgaCode = 594
        if lga == "Irele":
            lgaCode = 595
        if lga == "Odigbo":
            lgaCode = 596
        if lga == "Okitipupa":
            lgaCode = 597
        if lga == "Ondo East":
            lgaCode = 598
        if lga == "Ondo West":
            lgaCode = 599
        if lga == "Ose":
            lgaCode = 600
        if lga == "Owo":
            lgaCode = 601
        if lga == "Aiyedaade":
            lgaCode = 602
        if lga == "Aiyedire":
            lgaCode = 603
        if lga == "Atakunmosa East":
            lgaCode = 604
        if lga == "Atakunmosa West":
            lgaCode = 605
        if lga == "Boluwaduro":
            lgaCode = 606
        if lga == "Boripe":
            lgaCode = 607
        if lga == "Ede North":
            lgaCode = 608
        if lga == "Ede South":
            lgaCode = 609
        if lga == "Egbedore":
            lgaCode = 610
        if lga == "Ejigbo":
            lgaCode = 611
        if lga == "Ife Central":
            lgaCode = 612
        if lga == "Ife East":
            lgaCode = 613
        if lga == "Ife North":
            lgaCode = 614
        if lga == "Ife South":
            lgaCode = 615
        if lga == "Ifedayo":
            lgaCode = 616
        if lga == "Ifelodun":
            lgaCode = 617
        if lga == "Ila":
            lgaCode = 618
        if lga == "Ilesa East":
            lgaCode = 619
        if lga == "Ilesa West":
            lgaCode = 620
        if lga == "Irepodun":
            lgaCode = 621
        if lga == "Irewole":
            lgaCode = 622
        if lga == "Isokan":
            lgaCode = 623
        if lga == "Iwo":
            lgaCode = 624
        if lga == "Obokun":
            lgaCode = 625
        if lga == "Odo Otin":
            lgaCode = 626
        if lga == "Ola Oluwa":
            lgaCode = 627
        if lga == "Olorunda":
            lgaCode = 628
        if lga == "Oriade":
            lgaCode = 629
        if lga == "Orolu":
            lgaCode = 630
        if lga == "Osogbo":
            lgaCode = 631
        if lga == "Afijio":
            lgaCode = 632
        if lga == "Akinyele":
            lgaCode = 633
        if lga == "Atiba":
            lgaCode = 634
        if lga == "Atisbo":
            lgaCode = 635
        if lga == "Egbeda":
            lgaCode = 636
        if lga == "Ibadan North":
            lgaCode = 637
        if lga == "Ibadan North-East":
            lgaCode = 638
        if lga == "Ibadan North-West":
            lgaCode = 639
        if lga == "Ibadan South-East":
            lgaCode = 640
        if lga == "Ibadan South-West":
            lgaCode = 641
        if lga == "Ibarapa Central":
            lgaCode = 642
        if lga == "Ibarapa East":
            lgaCode = 643
        if lga == "Ibarapa North":
            lgaCode = 644
        if lga == "Ido":
            lgaCode = 645
        if lga == "Irepo":
            lgaCode = 646
        if lga == "Iseyin":
            lgaCode = 647
        if lga == "Itesiwaju":
            lgaCode = 648
        if lga == "Iwajowa":
            lgaCode = 649
        if lga == "Kajola":
            lgaCode = 650
        if lga == "Lagelu":
            lgaCode = 651
        if lga == "Ogbomosho North":
            lgaCode = 652
        if lga == "Ogbomosho South":
            lgaCode = 653
        if lga == "Ogo Oluwa":
            lgaCode = 654
        if lga == "Olorunsogo":
            lgaCode = 655
        if lga == "Oluyole":
            lgaCode = 656
        if lga == "Ona Ara":
            lgaCode = 657
        if lga == "Orelope":
            lgaCode = 658
        if lga == "Ori Ire":
            lgaCode = 659
        if lga == "Oyo East":
            lgaCode = 660
        if lga == "Oyo West":
            lgaCode = 661
        if lga == "Saki East":
            lgaCode = 662
        if lga == "Saki West":
            lgaCode = 663
        if lga == "Surulere":
            lgaCode = 664
        if lga == "Barkin Ladi":
            lgaCode = 665
        if lga == "Bassa":
            lgaCode = 666
        if lga == "Bokkos":
            lgaCode = 667
        if lga == "Jos East":
            lgaCode = 668
        if lga == "Jos North":
            lgaCode = 669
        if lga == "Jos South":
            lgaCode = 670
        if lga == "Kanam":
            lgaCode = 671
        if lga == "Kanke":
            lgaCode = 672
        if lga == "Langtang North":
            lgaCode = 673
        if lga == "Langtang South":
            lgaCode = 674
        if lga == "Mangu":
            lgaCode = 675
        if lga == "Mikang":
            lgaCode = 676
        if lga == "Pankshin":
            lgaCode = 677
        if lga == "Qua'an Pan":
            lgaCode = 678
        if lga == "Riyom":
            lgaCode = 679
        if lga == "Shendam":
            lgaCode = 680
        if lga == "Wase":
            lgaCode = 681
        if lga == "Abua/Odual":
            lgaCode = 682
        if lga == "Ahoada East":
            lgaCode = 683
        if lga == "Ahoada West":
            lgaCode = 684
        if lga == "Akuku-Toru":
            lgaCode = 685
        if lga == "Andoni":
            lgaCode = 686
        if lga == "Asari-Toru":
            lgaCode = 687
        if lga == "Bonny":
            lgaCode = 688
        if lga == "Degema":
            lgaCode = 689
        if lga == "Eleme":
            lgaCode = 690
        if lga == "Emuoha":
            lgaCode = 691
        if lga == "Etche":
            lgaCode = 692
        if lga == "Gokana":
            lgaCode = 693
        if lga == "Ikwerre":
            lgaCode = 694
        if lga == "Khana":
            lgaCode = 695
        if lga == "Obio/Akpor":
            lgaCode = 696
        if lga == "Ogba/Egbema/Ndoni":
            lgaCode = 697
        if lga == "Ogu/Bolo":
            lgaCode = 698
        if lga == "Okrika":
            lgaCode = 699
        if lga == "Omuma":
            lgaCode = 700
        if lga == "Opobo/Nkoro":
            lgaCode = 701
        if lga == "Oyigbo":
            lgaCode = 702
        if lga == "Port Harcourt":
            lgaCode = 703
        if lga == "Tai":
            lgaCode = 704
        if lga == "Binji":
            lgaCode = 705
        if lga == "Bodinga":
            lgaCode = 706
        if lga == "Dange Shuni":
            lgaCode = 707
        if lga == "Gada":
            lgaCode = 708
        if lga == "Goronyo":
            lgaCode = 709
        if lga == "Gudu":
            lgaCode = 710
        if lga == "Gwadabawa":
            lgaCode = 711
        if lga == "Illela":
            lgaCode = 712
        if lga == "Isa":
            lgaCode = 713
        if lga == "Kebbe":
            lgaCode = 714
        if lga == "Kware":
            lgaCode = 715
        if lga == "Rabah":
            lgaCode = 716
        if lga == "Sabon Birni":
            lgaCode = 717
        if lga == "Shagari":
            lgaCode = 718
        if lga == "Silame":
            lgaCode = 719
        if lga == "Sokoto North":
            lgaCode = 720
        if lga == "Sokoto South":
            lgaCode = 721
        if lga == "Tambuwal":
            lgaCode = 722
        if lga == "Tangaza":
            lgaCode = 723
        if lga == "Tureta":
            lgaCode = 724
        if lga == "Wamako":
            lgaCode = 725
        if lga == "Wurno":
            lgaCode = 726
        if lga == "Yabo":
            lgaCode = 727
        if lga == "Ardo Kola":
            lgaCode = 728
        if lga == "Bali":
            lgaCode = 729
        if lga == "Donga":
            lgaCode = 730
        if lga == "Gashaka":
            lgaCode = 731
        if lga == "Gassol":
            lgaCode = 732
        if lga == "Ibi":
            lgaCode = 733
        if lga == "Jalingo":
            lgaCode = 734
        if lga == "Karim Lamido":
            lgaCode = 735
        if lga == "Kumi":
            lgaCode = 736
        if lga == "Lau":
            lgaCode = 737
        if lga == "Sardauna":
            lgaCode = 738
        if lga == "Takum":
            lgaCode = 739
        if lga == "Ussa":
            lgaCode = 740
        if lga == "Wukari":
            lgaCode = 741
        if lga == "Yorro":
            lgaCode = 742
        if lga == "Zing":
            lgaCode = 743
        if lga == "Bade":
            lgaCode = 744
        if lga == "Bursari":
            lgaCode = 745
        if lga == "Damaturu":
            lgaCode = 746
        if lga == "Fika":
            lgaCode = 747
        if lga == "Fune":
            lgaCode = 748
        if lga == "Geidam":
            lgaCode = 749
        if lga == "Gujba":
            lgaCode = 750
        if lga == "Gulani":
            lgaCode = 751
        if lga == "Jakusko":
            lgaCode = 752
        if lga == "Karasuwa":
            lgaCode = 753
        if lga == "Machina":
            lgaCode = 754
        if lga == "Nangere":
            lgaCode = 755
        if lga == "Nguru":
            lgaCode = 756
        if lga == "Potiskum":
            lgaCode = 757
        if lga == "Tarmuwa":
            lgaCode = 758
        if lga == "Yunusari":
            lgaCode = 759
        if lga == "Yusufari":
            lgaCode = 760
        if lga == "Anka":
            lgaCode = 761
        if lga == "Bakura":
            lgaCode = 762
        if lga == "Birnin Magaji/Kiyaw":
            lgaCode = 763
        if lga == "Bukkuyum":
            lgaCode = 764
        if lga == "Bungudu":
            lgaCode = 765
        if lga == "Chafe":
            lgaCode = 766
        if lga == "Gummi":
            lgaCode = 767
        if lga == "Gusau":
            lgaCode = 768
        if lga == "Kaura Namoda":
            lgaCode = 769
        if lga == "Maradun":
            lgaCode = 770
        if lga == "Maru":
            lgaCode = 771
        if lga == "Shinkafi":
            lgaCode = 772
        if lga == "Talata Mafara":
            lgaCode = 773
        if lga == "Zurmi":
            lgaCode = 774
    except:
        print("""It seems one of the LGAs doesn't match the predefined""")
        
    return lgaCode
        


#body xml tag converter function
def getServiceCode(row):
    service = row.ServiceType
    serviceCode = 0
    try:
        if service == "Cash-in":
            serviceCode = 1
        if service == "Cash-out":
            serviceCode = 2
        if service == "Bills payment":
            serviceCode = 3
        if service == "Payment of salaries":
            serviceCode = 4
        if service == "Funds transfer services":
            serviceCode = 5
        if service == "Airtime top-up":
            serviceCode = 6
        if service == "P2P":
            serviceCode = 7
        if service == "Agent mobile payments/banking services":
            serviceCode = 8
        if service == "Cash disbursement of loans":
            serviceCode = 9
        if service == "Cash repayment of loans":
            serviceCode = 10
        if service == "Cash payment of retirement benefits":
            serviceCode = 11
    except:
        print("It seems the service type doesn't exist")
    return serviceCode



def convert_row(row):   
    return"""\n<RETURNITEM>
      <FICode>%s</FICode>
      <AgentCode>%s</AgentCode>
      <NoOfCustomers>%s</NoOfCustomers>
      <ServiceType>%s</ServiceType>
      <LGA>%s</LGA>
      <VolumeByServiceType>%s</VolumeByServiceType>
      <ValueByServiceType>%s</ValueByServiceType>      
      <DateRegistered>%s</DateRegistered>
    </RETURNITEM>""" % (FICode, row.AgentCode, row.NoOfCustomers, getServiceCode(row), getLGACode(row), row.VolumeByServiceType, row.ValueByServiceType, row.DateRegistered)


#Body xml script
body = '\n'.join(df.apply(convert_row, axis=1))

#combining all parts together
xmlLines = header+body+footer


#creating the xml file
xmlFile.write(xmlLines)


print("File converted successfully")