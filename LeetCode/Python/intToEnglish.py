# https://leetcode.com/problems/integer-to-english-words/
# Reprak11
class Solution:
    def numberToWords(self, num: int) -> str:
        numberDict = {
            0:'Zero',
            1:'One',
            2:'Two',
            3:'Three',
            4:'Four',
            5:'Five',
            6:'Six',
            7:'Seven',
            8:'Eight',
            9:'Nine',
            10:'Ten',
            11:'Eleven',
            12:'Twelve',
            13:'Thirteen',
            14:'Fourteen',
            15:'Fifteen',
            16:'Sixteen',
            17:'Seventeen',
            18:'Eighteen',
            19:'Nineteen',
            20:'Twenty',
            30:'Thirty',
            40:'Forty',
            50:'Fifty',
            60:'Sixty',
            70:'Seventy',
            80:'Eighty',
            90:'Ninety'
        }

        thousand = 1000
        million = thousand * 1000
        billion = million * 1000
        trillion = billion * 1000

        if num < 20:
            return numberDict[num]
        if num < 100:
            if num % 10 == 0:
                return numberDict[num]
            else:
                return numberDict[(num//10)*10] +' '+numberDict[num%10]
        if num < thousand:
            temp = numberDict[num//100] +' Hundred'
            if num%100 == 0:
                return temp
            else:
                return temp +' '+self.numberToWords(num%100)
        if num < million:
            temp = self.numberToWords(num//thousand) +' Thousand'
            if num%thousand == 0:
                return temp
            else:
                return temp +' '+self.numberToWords(num%1000)
        if num < billion:
            temp = self.numberToWords(num//million) +' Million'
            if num%million == 0:
                return temp
            else:
                return temp +' '+self.numberToWords(num%million)
        if num < trillion:
            temp = self.numberToWords(num//billion) +' Billion'
            if num%billion == 0:
                return temp
            else:
                return temp +' '+self.numberToWords(num%billion)

print(Solution().numberToWords(1001000000))