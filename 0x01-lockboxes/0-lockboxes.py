#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes or not isinstance(boxes, list):
        return False
    
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    queue = [0]
    visited[0] = True
    
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not visited[key]:
                queue.append(key)
                visited[key] = True
                
    return all(visited)
