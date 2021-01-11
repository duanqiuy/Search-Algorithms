def get_node(name, heuristic=None):

    node = {}
    node['name'] = name
    node['children'] = []
    node['heuristic'] = heuristic
    node['path'] = []

    return node

def add_child(node, name, heuristic):
    node['children'].append(get_node(name, heuristic))

    return node['children'][-1]
#Building the tree
tree = get_node("Kitchener",130)
#children of kitchener:Guelph,New Hamburg
add_child(tree,"Guelph", 160)
add_child(tree,"New Hamburg", 110)
#children of Guelph:Drayton,Kitchener
add_child(tree['children'][0],"Drayton", 100)
add_child(tree['children'][0]['children'][0], "Listowel", 0)
#children of New Hamburg:Stratford,kitchener
add_child(tree['children'][1],"Stratford", 100)
#children of Stratford:St. Marys,Drayton,New Hamburg
add_child(tree['children'][1]['children'][0], "St. Marys", 130)
add_child(tree['children'][1]['children'][0], "Drayton", 100)
#children of St. Marys: Mitchell,Stratford
add_child(tree['children'][1]['children'][0]['children'][0],"Mitchell", 100)
#children of Mitchell:Listowel,St. Marys
add_child(tree['children'][1]['children'][0]['children'][0]['children'][0],"Listowel", 0)
#children of Drayton:Listowel,Guelph,Stratford
add_child(tree['children'][1]['children'][0]['children'][1],"Listowel", 0)
print ('tree',tree)

#Task 1 Implement Depth-First Search
def DFS(init_state, goal_name):
    frontier = [init_state]
    explored = []
    while len(frontier):
        state = frontier.pop() # dequeue
        explored.append(state['name'])
        if state['name'] == goal_name:
            return True
        for child in state['children']:
            if child['name'] not in explored:
                frontier.append(child)
    return False

print(DFS(tree, 'Listowel'))

# Greedy helper
def find_min_heuristic(frontier):
    min_h_i = 0
    if len(frontier) > 1:
        min_h = frontier[min_h_i]['heuristic']
        for i, state in enumerate(frontier):
            if state['heuristic'] < min_h:
                min_h_i = i
                min_h = state['heuristic']
    return min_h_i

def GreedySearch(init_state, goal_name):
    frontier = [init_state]
    explored = []
    while len(frontier):
        state = frontier.pop(find_min_heuristic(frontier))
        explored.extend(state['name'])
        tree['path'].append(state['name'])
        if state['name'] == goal_name:
            return True
        for child in state['children']:
            if child['name'] not in explored:
                frontier.append(child)

    return False

print(GreedySearch(tree, 'Listowel'))
print('path', tree['path'])