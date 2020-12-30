from blog.blog import Blog

MENU_PROMPT = ("Enter 'c' to create a blog, 'l' to list blogs, "
               "'r' to read one, 'p' to create a post, or 'q' to quit: ")
POST_TEMPLATE = """
---{}---

{}

"""

blogs = dict()  # blog_name: Blog object


def menu():
    # Show the user the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit

    selection = input(MENU_PROMPT)
    print_blogs()
    while selection != "q":
        if selection == "c":
            ask_create_blog()
        elif selection == "l":
            print_blogs()
        elif selection == "r":
            ask_read_blog()
        elif selection == "p":
            ask_create_post()

        selection = input(MENU_PROMPT)


def print_blogs():
    # Print the available blogs
    for key, blog in blogs.items():
        print("- {}".format(blog))


def ask_create_blog():
    title = input("What's the title of the blog: ")
    author = input("Please, what's the author's name: ")
    blog = Blog(title, author)
    blogs[title] = blog


def ask_read_blog():
    title = input("Enter the blog title you want to read: ")

    print_posts(blogs[title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    blog_name = input("Enter the blog title you want to write a post in: ")
    title = input("Enter your post title: ")
    content = input("Enter your post content: ")

    blogs[blog_name].create_post(title, content)