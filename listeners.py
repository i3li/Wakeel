from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import logging
import handlers
from pathlib import Path

_logger = logging.getLogger(__name__)

_REQUEST_FILE_PATTERNS = ['*.txt']


class _CommandFileCreationHandler(PatternMatchingEventHandler):

    def __init__(self, res_dir, res_file_name=None):
        # res_file_name defaults to the same file name as the command file
        super().__init__(patterns=_REQUEST_FILE_PATTERNS)
        self.res_dir = Path(res_dir)
        self.res_file_name = res_file_name

    def on_created(self, event):
        super().on_created(event)
        # TODO: Filter on file size?
        with open(event.src_path) as f:
            src = Path(event.src_path)
            src_file_name = src.name
            if self.res_file_name is None:
                self.res_file_name = src_file_name
            res_path = self.res_dir.joinpath(self.res_file_name)
            handlers.handle(f.readline(), res_path)


class FileListener(object):
    """Handle commands using the file system.

    This listener listens for files added in
    a directory (The request directory) and responds
    to them in another directory (The response directory).
    """

    def __init__(self, req_dir, res_dir):
        self.req_dir = Path(req_dir)
        self.res_dir = Path(res_dir)
        self._event_handler = _CommandFileCreationHandler(self.res_dir)
        self._observer = Observer()
        self._observer.schedule(self._event_handler, str(self.req_dir))

    def start(self):
        """Starts the listener"""
        self._observer.start()

    def stop(self):
        """Stops the listener"""
        self._observer.stop()
