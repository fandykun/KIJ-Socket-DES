
pc1 = [[57, 49, 41, 33, 25, 17, 9],
       [1, 58, 50, 42, 34, 26, 18],
       [10, 2, 59, 51, 43, 35, 27],
       [19, 11, 3, 60, 52, 44, 36],
       [63, 55, 47, 39, 31, 23, 15],
       [7, 62, 54, 46, 38, 30, 22],
       [14, 6, 61, 53, 45, 37, 29],
       [21, 13, 5, 28, 20, 12, 4]]

pc2 = [[14, 17, 11, 24, 1, 5],
       [3, 28, 15, 6, 21, 10],
       [23, 19, 12, 4, 26, 8],
       [16, 7, 27, 20, 13, 2],
       [41, 52, 31, 37, 47, 55],
       [30, 40, 51, 45, 33, 48],
       [44, 49, 39, 56, 34, 53],
       [46, 42, 50, 36, 29, 32]]

ip = [[58, 50, 42, 34, 26, 18, 10, 2],
      [60, 52, 44, 36, 28, 20, 12, 4],
      [62, 54, 46, 38, 30, 22, 14, 6],
      [64, 56, 48, 40, 32, 24, 16, 8],
      [57, 49, 41, 33, 25, 17, 9 ,1],
      [59, 51, 43, 35, 27, 19, 11, 3],
      [61, 53, 45, 37, 29, 21, 13, 5],
      [63, 55, 47, 39, 31, 23, 15, 7]]

invIp = [[40, 8, 48, 16, 56, 24, 64, 32],
         [39, 7, 47, 15, 55, 23, 63, 31],
         [38, 6, 46, 14, 54, 22, 62, 30],
         [37, 5, 45, 13, 53, 21, 61, 29],
         [36, 4, 44, 12, 52, 20, 60, 28],
         [35, 3, 43, 11, 51, 19, 59, 27],
         [34, 2, 42, 10, 50, 18, 58, 26],
         [33, 1, 41, 9, 49, 17, 57, 25]]

eBitSelection = [[32, 1, 2, 3, 4, 5],
                 [4, 5, 6, 7 , 8 ,9 ],
                 [8, 9 , 10, 11, 12, 13],
                 [12, 13, 14, 15, 16, 17],
                 [16, 17, 18, 19, 20, 21],
                 [20, 21, 22, 23, 24, 25],
                 [24, 25, 26, 27 ,28, 29],
                 [28, 29, 30, 31, 32, 1]]

s_box = [[
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7], 
         [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
         [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
         [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
        ], 
    
        [
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10], 
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5], 
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15], 
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
        ],
       
        [
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7], 
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
        ], 
      
        [
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
        ], 
        
        [
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9], 
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6], 
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14], 
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
        ],

        [
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6], 
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
        ], 

        [
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2], 
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
        ], 
       
        [
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7], 
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2], 
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8], 
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
        ]]
        
pBox =  [[16, 7, 20, 21],
         [29, 12, 28, 17],
         [1, 15, 23, 26],
         [5, 18, 31, 10],
         [2, 8, 24, 14],
         [32, 27, 3, 9],
         [19, 13, 30, 6],
         [22, 11, 4, 25]]

class DES:
    def __init__(self):
        pass

    def shiftTwo (self, keys) :
        key0 = keys[0]
        key1 = keys[1]
        for x in list(range(26)) :
            if keys[x] != keys[x + 2]:
                keys = keys[:x] + keys[x + 2] + keys[(x + 1):]
        if(keys[26] != key0) :
            keys = keys[:26] + key0 + keys[(27):]
        if keys[27] != key1 :
            keys = keys[:-1]
            keys = keys + key1
        return keys

    def shiftOne (self, keys) :
        key0 = keys[0]
        for x in list(range(27)):
            if keys[x] != keys[x + 1]:
                keys = keys[:x] + keys[x+1] + keys[(x + 1):]
        if keys[27] != key0 :
            keys = keys[:27] + key0 + keys[(28):]
        return keys

    def subkeys (self, keys) :
        for x in range(1, 17):
            if x == 1 or x == 2 or x == 9 or x == 16 :
                keys.append((self.shiftOne(keys[x-1])))
            else:
                keys.append((self.shiftTwo(keys[x-1])))

    def changeToTable(self, column, row, table, source) :
        result=""
        for x in list(range(row)):
            for y in list(range(column)):
                index = table[x][y]
                result += (source[index-1])
        return result

    def encrypt(self, m, key):
        #print(key)

        #key = "133457799BBCDFF1"

        #ubah key ke pc1 table 56 bit
        keyInBin= bin(int(key, 16))[2:].zfill(64)
        # print("key in bin : ", keyInBin)
        kPlus = self.changeToTable(7, 8, pc1, keyInBin)

        #pisah key jadi 2 bagian
        c = []
        d = []
        c.append(kPlus[:28])
        d.append(kPlus[28:])

        #geser-geser key
        self.subkeys(c)
        self.subkeys(d)

        cd = []
        k = []

        #gabung lagi key
        for x in list(range(17)) :
            cd.append(c[x]+d[x])

        #ubah key ke pc2 table 48 bit
        for w in range(1, 17):
            temp = self.changeToTable(6, 8, pc2, cd[w])
            k.append(temp)
            temp = ""

        #print(k)

        #m = "0123456789ABCDEF"
        mInBin = bin(int(m, 16))[2:].zfill(64)
        # print("message in bin : ", mInBin)
        #ubah message ke ip table 64 bit
        mIP = self.changeToTable(8, 8, ip, mInBin)

        #pisahkan message menjadi l0 dan r0
        l = []
        r = []
        l.append(mIP[:32])
        r.append(mIP[32:])

        for y in list(range(16)) :
            sb = ""
            pSb= ""
            #ubah r ke e table 48 bit
            eR = self.changeToTable(6, 8, eBitSelection, r[y])
            k_XOR_eR =bin(int(k[y], 2) ^ int(eR, 2))[2:].zfill(48)
            awal = 0
            akhir = 6
            #ubah hasil xor ke s-box table 32 bit
            for x in list(range(8)) :
                b = k_XOR_eR[awal:akhir]    
                ySTable = int((b[0]+b[-1]), 2)
                xSTable = int(b[1:5], 2)
                sb += str(bin(s_box[x][ySTable][xSTable])[2:].zfill(4))
                awal += 6
                akhir += 6
            #ubah hasil s-box ke p table 32 bit
            pSb= self.changeToTable(4, 8, pBox, sb)
            #r = hasil xor pSb dengan l
            r.append(bin(int(l[y], 2) ^ int(pSb, 2))[2:].zfill(32))
            l.append(r[y])
            
        #gabung r16 dan l16
        rl = r[16] + l[16]
        #ubah ke ip-1 table
        chiper = self.changeToTable(8, 8, invIp, rl)
        # print("Chiper in bin : " , chiper)
        return hex(int(chiper, 2))[2:]
        



