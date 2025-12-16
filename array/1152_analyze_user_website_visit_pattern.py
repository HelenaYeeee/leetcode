# sol 1 
class Node: 
    def __init__(self, name, timestamp, website):
        self.name = name
        self.timestamp = timestamp
        self.website = website 

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        from collections import defaultdict
        from itertools import combinations
        nodes = [Node(name, ts, site) for name, ts, site in zip(username, timestamp, website)]
        # the use of zip() here is great
        nodes.sort(key=lambda x: x.timestamp)
        user_visits = defaultdict(list)

        for node in nodes: 
            user_visits[node.name].append(node) # key = username, value = (username, timestamp, website)
        
        route = defaultdict(int) # key = path, value = score
        
        for visits in user_visits.values():
            tmp = set()
            for i,j,k in combinations(range(len(visits)), 3):
                # generate length=3 combinations from the visits of a user
                # note that range(len(visits)) is sorted, so the output will also be sorted 
                # ref: https://docs.python.org/3/library/itertools.html#itertools.combinations  
                path = (visits[i].website, visits[j].website, visits[k].website)
                tmp.add(path)
            for path in tmp: 
                route[path] += 1 

        max_count = -1
        result = ()
        for path, count in route.items():
            if count > max_count or (count == max_count and path < result):
                max_count = count
                result = path
        return list(result) # converts tuple to list


# sol 2, essentially the same thing, but much shorter 
# focus on sol 1, use sol 2 for extended study
# ref: https://leetcode.com/problems/analyze-user-website-visit-pattern/solutions/899805/detailed-easy-to-follow-python-solution-afhy9 
