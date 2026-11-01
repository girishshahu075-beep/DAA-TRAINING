class Solution:
    def getSkyline(self, buildings):
        events=[]
        for left,right,height in buildings:
            events.append((left,-height,right))
            events.append((right,0,0))
        events.sort()
        active=[(0,float('inf'))]
        result=[]
        prev_height=0
        for x,neg_height,right in events:
            active=[item for item in active if item[1]>x]
            if neg_height !=0:
                active.append((neg_height,right))
            curr_height=-min(active)[0]
            if curr_height!=prev_height:
                result.append([x,curr_height])
                prev_height=curr_height
        return result