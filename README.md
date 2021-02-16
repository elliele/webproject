# Web Project

This is a introduction to web development using Python and webpy.org.


***Install web.py

---
pip3 install web.py
---

***Sample Code from webpy.org

---
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
    app.run()
 
 ---
