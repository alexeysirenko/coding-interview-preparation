class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2 ** 31 - 1
        
        acc = 0
        number = abs(x)
        while number != 0:
            n = number % 10
            number = number // 10
            
            if x >= 0 and acc > max_int // 10 or (acc == max_int // 10 and n >= 7):
                return 0
            if x < 0 and acc > (max_int + 1) // 10 or (acc == (max_int + 1) // 10 and n >= 8):
                return 0
            
            acc = acc * 10 + n
            
        return acc if x > 0 else -acc
        