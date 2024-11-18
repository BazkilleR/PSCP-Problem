'''Bubble'''

def traverse(surface):
    '''Determines the number of jumps needed and possibility of traversal.'''
    jumps = 0
    pos = 0
    status = "POSSIBLE"

    while pos < len(surface):
        if surface[pos] in ('^', 'o'):

            if surface[pos + 1] != ' ':
                jumps += 1
                pos += 1
            else:
                status = 'IMPOSSIBLE'
                jumps = len(surface) - pos - 1
                break

        elif surface[pos] == 'O':
            max_jump = min(3, len(surface) - pos - 1)
            goal_idx = surface[pos + 1:pos + max_jump + 1].rfind('|')
            big_o_idx = surface[pos + 1:pos + max_jump + 1].rfind('O')
            o_idx = surface[pos + 1:pos + max_jump + 1].rfind('o')

            if goal_idx > -1:
                jumps += 1
                pos += goal_idx + 1
            elif big_o_idx > -1:
                jumps += 1
                pos += big_o_idx + 1
            elif o_idx > -1:
                jumps += 1
                pos += o_idx + 1
            else:
                status = 'IMPOSSIBLE'
                jumps = len(surface) - pos - 1
                break

        if surface[pos] == '|':
            break

    return jumps, status

j, result = traverse(input())
print(result)
print(j)
