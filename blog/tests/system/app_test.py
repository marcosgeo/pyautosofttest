from unittest import TestCase
from unittest.mock import patch, create_autospec

from blog import app
from blog.blog import Blog, Post


class AppTest(TestCase):
    def setUp(self):
        blog = Blog("New Blog", "Best Author")
        app.blogs = {"New Blog": blog}

    def test_menu_calls_create_blog(self):
        with patch("builtins.input") as mocked_input:
            with patch("blog.app.ask_create_blog") as mocked_ask_create_blog:
                mocked_input.side_effect = ("c", "Test Create Blog", "Test Author", "q")
                app.menu()
                mocked_ask_create_blog.assert_called()

    def test_app_prints_prompt(self):
        msg = ("Enter 'c' to create a blog, 'l' to list blogs, "
               "'r' to read one, 'p' to create a post, or 'q' to quit: ")

        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("l", "q")
            app.menu()
            mocked_input.assert_called_with(msg)

    def test_app_menu_calls_pring_blogs(self):
        with patch("blog.app.print_blogs") as mocked_print_blogs:
            with patch("builtins.input") as mocked_input:
                mocked_input.side_effect = ("l", "q")
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("- New Blog by Best Author (0 post)")

    def test_ask_create_blog(self):
        with patch("builtins.input") as mocked_input:
            # since input was called two times, two values are inputed
            mocked_input.side_effect = ("Test", "Test Author")
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get("Test"))

    def test_ask_read_blog(self):
        with patch("builtins.input", return_value="New Blog"):
            with patch("blog.app.print_posts") as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(app.blogs["New Blog"])

    def test_print_posts(self):
        blog = app.blogs["New Blog"]
        blog.create_post("Test Post", "Test Content")
        with patch("blog.app.print_post") as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post("Post title", "Post content")
        expected_print = """
---Post title---

Post content

"""
        with patch("builtins.print") as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("New Blog", "Blog Title", "Blog Content")

            app.ask_create_post()

            self.assertEqual(app.blogs["New Blog"].posts[0].title, "Blog Title")
            self.assertEqual(app.blogs["New Blog"].posts[0].content, "Blog Content")
