class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.terminal = False

class Trie:
    def __init__(self, root):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.terminal = True

    def search(self, word):
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.terminal
    
    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True
    
    def display(self):
        def helper(node, word):
            if node.terminal:
                print(word)
            for i, c in enumerate(node.children):
                if c:
                    helper(c, word + chr(i + ord('a')))
        helper(self.root, "")
    
    def display_prefix(self, prefix):
        node = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                return
            node = node.children[idx]
        def helper(node, word):
            if node.terminal:
                print(prefix + word)
            for i, c in enumerate(node.children):
                if c:
                    helper(c, word + chr(i + ord('a')))
        helper(node, "")

t = Trie(TrieNode())
t.insert("apple")
t.insert("app")
t.insert("ap")
t.insert("apricot")
t.insert("banana")
t.insert("b")
t.insert("c")

print(t.search("apple"))
print(t.search("app"))
print(t.search("bananaz"))
print(t.search("bananaz"))

print(t.startsWith("ap"))
print(t.startsWith("b"))
print(t.startsWith("c"))
print(t.startsWith("ban"))

t.display()
t.display_prefix("ap")
t.display_prefix("b")