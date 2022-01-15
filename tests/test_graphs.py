from hexlet.graphs import build_tree_from_leaf, make_joints


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
    actual = make_joints(TREE)
    assert actual == JOINTS


def test_build_tree_from_leaf():
    expected = ['F', [
        ['J', [
            ['O'],
            ['N'],
        ]],
        ['I', [
            ['M'],
        ]],
        ['C', [
            ['G', [
                ['K'],
                ['L'],
            ]],
            ['A', [
                ['B', [
                    ['E'],
                    ['D', [
                        ['H'],
                    ]],
                ]],
            ]],
        ]],
    ]]
    actual = build_tree_from_leaf(JOINTS, 'F')
    print(actual)
    assert actual == expected
