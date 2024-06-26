class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:

        clips.sort(key = lambda x: (x[0],-x[1]))
        t, cSet, ans = 0, set(), 0

        while clips:
            while clips and clips[0][1] <= t: clips.pop(0)
            while clips and clips[0][0] <= t: cSet.add(clips.pop(0)[1])

            if clips and not cSet: return -1
            t = max(cSet)
            ans+= 1
            if t >= time: return ans 
            cSet.clear()

        return -1