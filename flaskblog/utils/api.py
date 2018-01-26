from flask import url_for

def make_public_blog(blog):
    """adds a public URI to blog

    :type blog: dict (blog.serialize)
    """
    new_blog = {}
    for field in blog.keys():
        if field == 'id':
            new_blog['URI'] = url_for('api.blog', blog_id = blog['id'], _external=True)
        else:
            new_blog[field] = blog[field]
    return new_blog
