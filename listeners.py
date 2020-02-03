from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import logging
import handlers

_logger = logging.getLogger(__name__)

_REQUEST_FILE_PATTERNS = ['*.txt']


class _CommandFileCreationHandler(PatternMatchingEventHandler):

    def __init__(self):
        super().__init__(patterns=_REQUEST_FILE_PATTERNS)

    def on_created(self, event):
        super().on_created(event)

        # TODO: Filter on file size?
        with open(event.src_path) as f:
            handlers.handle(f.readline())


class FileListener(object):
    """Handle commands using the file system.

    This listener listens for files added in
    a directory (The request directory) and responds
    to them in another directory (The response directory).
    """

    def __init__(self, req_dir, res_dir):
        self.req_dir = req_dir
        self.res_dir = res_dir
        self._event_handler = _CommandFileCreationHandler()
        self._observer = Observer()
        self._observer.schedule(self._event_handler, self.req_dir)

    def start(self):
        """Starts the listener"""
        self._observer.start()

    def stop(self):
        """Stops the listener"""
        self._observer.stop()

# listener = FileListener('/Users/ali/Desktop', '/Users/ali/Desktop')
# listener.start()
#
# import time
# try:
#     while True:
#         time.sleep(1)
# except KeyboardInterrupt:
#     listener.stop()
