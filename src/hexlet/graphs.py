import functools
import itertools


def make_joints(tree, parent=None):
    iterable = iter(tree)
    leaf = next(iterable)
    children = next(iterable, None)

    if children is None:
        return {leaf: [parent]}

    flatChildren = list(itertools.chain(*children))
    neighbors = list(filter(
        lambda neighbor: neighbor is not None and
        not isinstance(neighbor, list),
        [*flatChildren, parent],
    ))
    joints = functools.reduce(
        lambda acc, child: {**acc, **make_joints(child, leaf)},
        children,
        {},
    )

    return {leaf: neighbors, **joints}


def build_tree_from_leaf(joints, leaf):
    def iter(current, acc):
        checked = [*acc, current]
        neighbors = joints[current]

        filtered = filter(
            lambda neighbor: neighbor not in checked,
            neighbors,
        )
        maped = list(map(
            lambda neighbor: iter(neighbor, checked),
            filtered,
        ))

        return [current, maped] if maped else [current]

    return iter(leaf, [])


def sort_joints(joints):
    return functools.reduce(
        lambda acc, leaf: {**acc, leaf: sorted(joints[leaf])},
        joints,
        {},
    )
