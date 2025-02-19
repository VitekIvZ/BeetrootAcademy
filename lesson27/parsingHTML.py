from bs4 import BeautifulSoup

class TreeNode:
    def __init__(self, tag, text):
        self.tag = tag
        self.text = text.strip() if text else ""
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class DOMTree:
    def __init__(self):
        self.root = None

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        self.root = self._build_tree(soup)

    def _build_tree(self, element):
        node = TreeNode(tag=element.name, text=element.get_text())
        for child in element.children:
            if child.name:  # Якщо це тег
                child_node = self._build_tree(child)
                node.add_child(child_node)
        return node

    def search_by_tag(self, tag):
        results = []
        self._search_tree(self.root, tag, results)
        return results

    def _search_tree(self, node, tag, results):
        if node.tag == tag:
            results.append(node.text)
        for child in node.children:
            self._search_tree(child, tag, results)

# Використання
html_doc = """
<html>
    <body>
        <div>
            <p>Hello World!</p>
            <p>This is a test.</p>
        </div>
        <span>Some text here.</span>
    </body>
</html>
"""

dom_tree = DOMTree()
dom_tree.parse_html(html_doc)

# Пошук тексту за тегом
tag_to_search = 'p'
texts = dom_tree.search_by_tag(tag_to_search)

print(f"Texts found for tag '{tag_to_search}':")
for text in texts:
    print(text)

