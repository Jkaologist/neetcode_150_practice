class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False
    def __repr__(self):  
        return "TrieNode children are:% s isWord:% s" % (self.children, self.isWord)  
    def __str__(self):  
        return "From str method of TrieNode: children are % s, " \
              "isWord is % s" % (self.children, self.isWord)
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            i = ord(char) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]

        curr.isWord = True
    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            i = ord(char) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            i = ord(char) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]

        return True

# Driver Code          
root = TrieNode()
  
# This calls __str__()  
print(root)  
  
# This calls __repr__()
print([root]) 