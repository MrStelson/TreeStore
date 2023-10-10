from typing import List


class TreeStore:
    def __init__(self, items: List[dict]):
        self._dict_items = {}
        self._children_items = {}

        for item in items:
            item_id = item.get("id")
            parent_id = item.get("parent")

            if parent_id not in self._children_items:
                self._children_items[parent_id] = []
            self._children_items.get(parent_id).append(item)

            self._dict_items[item_id] = item

    def getAll(self) -> List[dict]:
        return list(self._dict_items.values())

    def getItem(self, id: int) -> dict:
        return self._dict_items.get(id, f"Don't have id: {id}")

    def getChildren(self, id: int):
        return self._children_items.get(id, [])

    def getAllParents(self, id: int) -> list:
        parents = []
        node = self.getItem(id)
        while node["parent"] != "root":
            parent_id = node["parent"]
            node = self.getItem(parent_id)
            parents.append(self.getItem(parent_id))
        return parents


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

# На всякий случай запушил на гитхаб + тесты: https://github.com/MrStelson/TreeStore.git
