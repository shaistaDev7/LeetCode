class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_box = {}
        no_of_jewels = 0
        for s in stones:
            if s not in stone_box:
                stone_box[s] = 1
            else:
                stone_box[s] += 1
        for j in jewels: 
            if j in stone_box:
                no_of_jewels += stone_box[j]
        return no_of_jewels