from html.parser import HTMLParser

class Node:
    def __init__(self, tag, text=''):
        self.tag = tag
        self.text = text
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def find_text_by_tag(self, tag):
        results = []
        if self.tag == tag and self.text:
            results.append(self.text)
        for child in self.children:
            results.extend(child.find_text_by_tag(tag))
        return results

    def __str__(self, level=0):
        ret = "\t" * level + f"<{self.tag}>: {self.text}\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = None
        self.current_node = None
        self.stack = []

    def handle_starttag(self, tag, attrs):
        new_node = Node(tag)
        if self.current_node:
            self.current_node.add_child(new_node)
        else:
            self.root = new_node
        self.stack.append(new_node)
        self.current_node = new_node

    def handle_endtag(self, tag):
        if self.stack:
            self.stack.pop()
            if self.stack:
                self.current_node = self.stack[-1]
            else:
                self.current_node = None

    def handle_data(self, data):
        if self.current_node:
            self.current_node.text += data.strip()

def parse_html_to_dom(html):
    parser = MyHTMLParser()
    parser.feed(html)
    return parser.root

if __name__ == '__main__':
    html_doc = """
    <html>
        <head>
            <title>Test Page</title>
        </head>
        <body>
            <p>This is a paragraph.</p>
            <div>
                <p>This is another paragraph.</p>
            </div>
        </body>
    </html>
    """

    # Парсимо HTML-документ і будуємо DOM-дерево
    dom_tree = parse_html_to_dom(html_doc)

    # Виводимо DOM-дерево
    print("DOM-дерево:")
    print(dom_tree)

    # Пошук тексту за тегом
    tag_to_find = "title"
    texts = dom_tree.find_text_by_tag(tag_to_find)
    print(f"\nТекст за тегом '{tag_to_find}': {texts}")

    tag_to_find = "p"
    texts = dom_tree.find_text_by_tag(tag_to_find)
    print(f"Текст за тегом '{tag_to_find}': {texts}")
