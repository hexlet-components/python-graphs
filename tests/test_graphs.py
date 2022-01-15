from hexlet.graphs import (
    build_tree_from_leaf,
    make_joints,
    sort_joints,
    sort_tree
)


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


def test_sort_joints():
    expected = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B', 'H'],
        'E': ['B'],
        'F': ['C', 'I', 'J'],
        'G': ['C', 'K', 'L'],
        'H': ['D'],
        'I': ['F', 'M'],
        'J': ['F', 'N', 'O'],
        'K': ['G'],
        'L': ['G'],
        'M': ['I'],
        'N': ['J'],
        'O': ['J'],
    }
    actual = sort_joints(JOINTS)
    assert actual == expected


def test_sort_tree():
    expected = ['A', [
        ['B', [
            ['D', [
                ['H'],
            ]],
            ['E'],
        ]],
        ['C', [
            ['F', [
                ['I', [
                    ['M'],
                ]],
                ['J', [
                    ['N'],
                    ['O'],
                ]],
            ]],
            ['G', [
                ['K'],
                ['L'],
            ]],
        ]],
    ]]
    actual = sort_tree(TREE)
    assert actual == expected


def test_sort_tree_with_duplicate_leafs():
    tree_with_duplicate_leafs = ['B', [
        ['D'],
        ['A', [
            ['C', [
                ['F'],
                ['E'],
            ]],
            ['B', [
                ['D'],
            ]],
        ]],
    ]]
    expected = ['B', [
        ['A', [
            ['B', [
                ['D'],
            ]],
            ['C', [
                ['E'],
                ['F'],
            ]],
        ]],
        ['D'],
    ]]
    actual = sort_tree(tree_with_duplicate_leafs)
    assert actual == expected
