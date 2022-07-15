from flask import Flask
from index.index import index_bp
from blog.blog import blog_bp
from demos.demos import demos_bp

app = Flask(__name__)

app.register_blueprint(index_bp, url_prefix="/")
app.register_blueprint(blog_bp, url_prefix="/blog")
app.register_blueprint(demos_bp, url_prefix="/demos")
