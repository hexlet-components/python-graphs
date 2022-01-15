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
