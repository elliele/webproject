import web


#set up certain set of routes(list of two item per row which route and name of class('index') which route need to connect to
urls = (
    '/(.*)/(.*)', 'index'
)

#tell where python to look for our html into "resources/" directory
render = web.template.render("resources/")

#instantiate web application
app = web.application(urls, globals())

class index:
    def GET(self, name, age):
        return render.main(name, age)

if __name__ == "__main__":
    app.run()

#HTML Templates
#create a directory(resources)

#<h1>Name: $name</h1> , pass variable with $
# $def with (name,age), how to pass it into variable and also to return render.main(name, age)

