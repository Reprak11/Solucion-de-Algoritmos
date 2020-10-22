# https://leetcode.com/problems/defanging-an-ip-address/
# Reprak11

class Solution:
    def defangIPaddr(self, address: str) -> str:
        address=address.split(".")
        address= "[.]".join(address)
        return address 
    
    def defangIPaddr2(self, address: str) -> str:
        return address.replace(".","[.]")
    
if __name__ == "__main__":
    address = input()
    x = Solution()
    print(x.defangIPaddr2(address))