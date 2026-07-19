def solution(todo_list, finished):
    unfinished = []
    for i, v in enumerate(finished):
        if not v:
            unfinished.append(todo_list[i])
    return unfinished
            