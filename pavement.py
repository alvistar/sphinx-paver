# <== include('started/newway/pavement.py', 'imports')==>
from paver.easy import *
from paver.virtual import virtualenv
import paver.doctools
import tornado.ioloop
import tornado.web
import os
from  watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from paver.setuputils import setup
# <==end==>

options(
    sphinx=Bunch(
        docroot=".",
        builddir="build",
        sourcedir="source"
    ),
    virtualenv=Bunch(
        dest_dir="virtualenv",
        no_site_packages=True,
        packages_to_install= ["sphinx","tornado","watchdog"]
    )
)

@task
def server (options, info):
	""" Run server and monitor for changes """
	
	class MyEventHandler(FileSystemEventHandler):
		def on_any_event(self, event):
			print "Changes detected"
			print "Building html"
			paver.doctools.html()

	settings = {
	    "debug":True
	}

	event_handler = MyEventHandler()

	application = tornado.web.Application( 	
		[(r"/", tornado.web.RedirectHandler,dict(url="/index.html")),
		(r"/(.*)",tornado.web.StaticFileHandler, {"path": "build/html"})],
		**settings)

	print "Running server on port 8888"

	observer= Observer()

	observer.schedule(event_handler, "source", recursive=True)
	observer.start()

	application.listen(8888)
	
	while True: 
		print "Starting the server"
		tornado.ioloop.IOLoop.instance().start()

