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

    def get_children(self):
        return self.children


class Solution:
    def get_all_suffixes(self, node: TrieNode) -> list[str]:
        suffixes = []
        if node.is_end_of_word():
            suffixes.append("")

        for key, child in node.get_children().items():
            for suffix in self.get_all_suffixes(child):
                suffixes.append(key + suffix)

        return suffixes


    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        root: TrieNode = TrieNode()

        for product in products:
            node: TrieNode = root
            for c in product:
                if not node.has_child(c):
                    node.add_child(c)
                node = node.get_child(c)
            node.set_end_of_word(True)

        suggestions: list[list[str]] = [[] for _ in searchWord]

        # last common ancestor node
        node = root
        for i in range(len(searchWord)):
            c = searchWord[i]
            if not node.has_child(c):
                break

            prefix = searchWord[0:i+1]
            node = node.get_child(c)

            for suffix in self.get_all_suffixes(node):
                suggestions[i].append(prefix + suffix)

            suggestions[i] = sorted(suggestions[i])[0:3]

        return suggestions


if __name__ == "__main__":
    solution = Solution()
    assert solution.suggestedProducts(
        products=["mobile", "mouse", "moneypot", "monitor", "mousepad"],
        searchWord="mouse",
    ) == [
        ["mobile", "moneypot","monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
    ]

    assert solution.suggestedProducts(
        products=["havana"],
        searchWord="havana",
    ) == [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]
