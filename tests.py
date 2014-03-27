import os
import unittest
from jinja2 import Environment, Template, FileSystemLoader
from jinja2_markdown import MarkdownExtension


class Jinja2MarkdownTestCase(unittest.TestCase):

    def setUp(self):
        loader = FileSystemLoader(os.path.dirname(__file__))
        self.env = Environment(loader=loader, extensions=[MarkdownExtension])

    def test_parsing(self):
        input = ("{% markdown %}"
                 "Regular text"
                 "# Heading"
                 "{% endmarkdown %}")

        output = ("<p>Regular text</p>\n"
                  "<h1>Heading</h1>")

        template = self.env.get_template('test_input.html')
        self.assertEqual(template.render(), output)


if __name__ == '__main__':
    unittest.main()
