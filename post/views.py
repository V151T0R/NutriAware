from django.http import HttpResponse

posts = [
    {
        "id": 1,
        "title": "Introduction to Python",
        "content": "Python is a versatile programming language used for web development, data science, automation, and more."
    },
    {
        "id": 2,
        "title": "Understanding Lists",
        "content": "Lists are ordered collections in Python that can store multiple items."
    },
    {
        "id": 3,
        "title": "Working with Dictionaries",
        "content": "Dictionaries store data as key-value pairs and provide fast lookups."
    },
    {
        "id": 4,
        "title": "Getting Started with Flask",
        "content": "Flask is a lightweight Python web framework used to build web applications."
    },
    {
        "id": 5,
        "title": "REST API Basics",
        "content": "A REST API allows communication between clients and servers using HTTP methods."
    }
]

def static_view(request):
    html = ""

    for post in posts:
        html += f"""
        <div>
            <a href="posts/{post['id']}">
            <h1> {post["id"]}: {post['title']}</h1> </a>
        </div>
        """

    return HttpResponse(html)


def dynamic_view(request, id):
    for post in posts:
        if post["id"] == id:
            html = f"""
            <div>
                <h1>{post['title']}</h1>
                <p>{post['content']}</p>
            </div>
            """
            return HttpResponse(html)

    return HttpResponse("<h1>Page not found</h1>", status=404)