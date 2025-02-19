#task2lesson27.py

import requests
from bs4 import BeautifulSoup, Tag

class TreeNode:
    def __init__(self, tag, text):
        self.tag = tag
        self.text = text.strip() if text else ""
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self, indent=0):
        result = " " * indent + f"Tag: {self.tag}, Text: {self.text}\n"
        for child in self.children:
            result += child.__str__(indent + 4)
        return result

class DOMTree:
    def __init__(self):
        self.root = None

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        if soup and soup.find():
            self.root = self._build_tree(soup.find())

    def _build_tree(self, element):
        node = TreeNode(tag=element.name, text=element.get_text())
        for child in element.children:
            if isinstance(child, Tag):  
                child_node = self._build_tree(child)
                node.add_child(child_node)
        return node

    def search_by_tag(self, tag):
        results = []
        if self.root:
            self._search_tree(self.root, tag, results)
        return results

    def _search_tree(self, node, tag, results):
        if node.tag == tag:
            results.append(node.text)
        for child in node.children:
            self._search_tree(child, tag, results)

    def __str__(self):
        return str(self.root) if self.root else "DOM-дерево порожнє"

if __name__ == '__main__':
    url = 'https://example.com/blog/'
    response = requests.get(url)
    dom_tree = DOMTree()
    dom_tree.parse_html(response.text)

    print("DOM-дерево:")
    print(dom_tree)

    tag_to_search = 'p'
    texts = dom_tree.search_by_tag(tag_to_search)

    print(f"Texts found for tag '{tag_to_search}':")
    for text in texts:
        print(text)
