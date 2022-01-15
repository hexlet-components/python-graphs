from hexlet.graphs import make_joints


TREE = ['A', [
    ['C', [
        ['F', [
            ['J', [
                ['O'],
                ['N'],
            ]],
            ['I', [
                ['M'],
            ]],
        ]],
        ['G', [
            ['K'],
            ['L'],
        ]],
    ]],
    ['B', [
        ['E'],
        ['D', [
            ['H'],
        ]],
    ]],
]]

JOINTS = {
        'A': ['C', 'B'],
        'B': ['E', 'D', 'A'],
        'C': ['F', 'G', 'A'],
        'D': ['H', 'B'],
        'E': ['B'],
        'F': ['J', 'I', 'C'],
        'G': ['K', 'L', 'C'],
        'H': ['D'],
        'I': ['M', 'F'],
        'J': ['O', 'N', 'F'],
        'K': ['G'],
        'L': ['G'],
        'M': ['I'],
        'N': ['J'],
        'O': ['J'],
    }


def test_make_joints():
    joints = make_joints(TREE)
    assert joints == JOINTS
