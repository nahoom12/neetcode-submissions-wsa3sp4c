class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.FollowMap = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count -= 1
    def getNewsFeed(self, userId: int) -> List[int]:
        self.FollowMap[userId].add(userId)
        res = []
        MinHeap = []
        for followeeId in self.FollowMap[userId]:
            index = len(self.tweetMap[followeeId]) - 1
            if index >= 0:
                count,tweetId = self.tweetMap[followeeId][index]
                MinHeap.append([count,tweetId,followeeId,index - 1])
                heapq.heapify(MinHeap)
        while MinHeap and len(res) < 10:
            count,tweetId,followeeId,index = heapq.heappop(MinHeap)
            res.append(tweetId)
            if index >= 0:
                count,tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(MinHeap,[count,tweetId,followeeId,index - 1])
        return res     
    def follow(self, followerId: int, followeeId: int) -> None:
        self.FollowMap[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.FollowMap[followerId]:
            self.FollowMap[followerId].remove(followeeId)  
        

        
