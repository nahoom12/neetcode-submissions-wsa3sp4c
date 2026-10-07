class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Value Pair to Hash map
        time = 0
        store = {}
        for i in range(len(tasks)):
            store[tasks[i]] = store.get(tasks[i], 0) + 1
        nums = list(store.values())
        for i in range(len(nums)):
            nums[i] = -1 * nums[i]
        heapq.heapify(nums)
        queue = deque()
        while nums or queue:
            if queue and queue[0][1] == time:
                x,y = queue.popleft()
                heapq.heappush(nums,x)
            if nums:
                num = heapq.heappop(nums)
                time += 1
                if num < -1:
                    queue.append([num + 1,time + n])
            else:
                time += 1
        return time

                


        