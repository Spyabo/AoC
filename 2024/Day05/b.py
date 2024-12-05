with open('./2024/Day05/input.txt', 'r') as f:
    lines: str = f.read().splitlines()

from collections import defaultdict, deque

rules = defaultdict(list)
i = 0

while lines[i] != '':
    left, right = lines[i].split('|')
    rules[left].append(right)
    
    i += 1
    
updates = lines[i + 1:]    
total = 0

print(rules)
print(updates)

def fix_update(update):
    in_degree = defaultdict(int)  
    queue = deque()
    graph = {x: list(filter(lambda y: y in update, rules[x])) for x in update}
    print("Graph: ", graph)
    result = []
  
    # Calculate in-degrees for each node  
    for node in graph:  
        for neighbor in graph[node]:  
            in_degree[neighbor] += 1  
  
    # Enqueue nodes with in-degree 0  
    for node in graph:  
        if in_degree[node] == 0:  
            queue.append(node)  
  
    while queue:  
        current_node = queue.popleft()  
        result.append(current_node)  
  
        # Update in-degrees for neighbours  
        for neighbor in graph[current_node]:  
            in_degree[neighbor] -= 1  
  
            # Enqueue nodes with in-degree 0  
            if in_degree[neighbor] == 0:  
                queue.append(neighbor)  
  
    # Check for cycles  
    if len(result) != len(graph):  
        raise Exception("The graph has a cycle!")
    
    return int(result[len(result) // 2])  

for update in updates:
    update = update.split(",")
    
    for index, page in enumerate(update):
        for rule in rules[page]:
            if rule in update and index > update.index(rule):
                print(f"Update: {update} Page: {page} Rule: {rule}, {int(update[len(update) // 2])}")
                total += fix_update(update)
                break
        else:
            continue
        break

print(total)