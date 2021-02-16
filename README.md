# Web Project

This is a introduction to web development using Python and webpy.org.

web.py is a web framework for Python that is as simple as it is powerful. web.py is in the public domain, you can use it for whatever purpose with absolutely no restrictions.


### Install web.py

```py
pip3 install web.py
```


### Sample Code from webpy.org

```py
import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run(
```
