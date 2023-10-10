from tree_store import TreeStore


def tests(ts: TreeStore, items: list):
    assert ts.getAll() == items
    assert ts.getItem(7) == {"id": 7, "parent": 4, "type": None}
    assert ts.getChildren(4) == [{"id": 7, "parent": 4, "type": None}, {"id": 8, "parent": 4, "type": None}]
    assert ts.getChildren(5) == []
    assert ts.getAllParents(7) == [{"id": 4, "parent": 2, "type": "test"},
                                   {"id": 2, "parent": 1, "type": "test"},
                                   {"id": 1, "parent": "root"},
                                   ]
    print('All tests passed')


def main():
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]
    ts = TreeStore(items)
    tests(ts=ts, items=items)


if __name__ == '__main__':
    main()
