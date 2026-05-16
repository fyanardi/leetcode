class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def add_child(self, key):
        if key not in self.children:
            self.children[key] = TrieNode()

    def has_child(self, key):
        return key in self.children

    def get_child(self, key):
        return self.children[key] if key in self.children else None

    def set_end_of_word(self, end_of_word):
        self.end_of_word = end_of_word

    def is_end_of_word(self):
        return self.end_of_word

class Trie:

    def __init__(self):
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        node: TrieNode = self.root

        for c in word:
            if not node.has_child(c):
                node.add_child(c)
            node = node.get_child(c)

        node.set_end_of_word(True)

    def search(self, word: str) -> bool:
        node: TrieNode = self.root

        for c in word:
            if not node.has_child(c):
                return False
            node = node.get_child(c)

        return node.is_end_of_word()

    def startsWith(self, prefix: str) -> bool:
        node: TrieNode = self.root

        for c in prefix:
            if not node.has_child(c):
                return False
            node = node.get_child(c)

        return True


def execute_test_case(actions: list[str], params: list[list[str]], output: list[bool | None]):
    trie = None
    for i in range(len(actions)):
        action = actions[i]
        if action == "Trie":
            trie = Trie()
        elif action == "insert":
            assert trie is not None
            trie.insert(params[i][0])
        elif action == "search":
            assert trie is not None
            r = trie.search(params[i][0])
            assert r == output[i], f"Invalid search() output at i={i} expected={output[i]} actual={r}"
        elif action == "startsWith":
            assert trie is not None
            r = trie.startsWith(params[i][0])
            assert r == output[i], f"Invalid startsWith() output at i={i} expected={output[i]} actual={r}"


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == "__main__":
    execute_test_case(
        actions=[
            "Trie", "insert", "search", "search", "startsWith", "insert", "search"
        ],
        params=[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
        output=[None, None, True, False, True, None, True]
    )
