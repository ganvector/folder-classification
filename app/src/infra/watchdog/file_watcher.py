import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileCreatedHandler(FileSystemEventHandler):
    def __init__(self, service):
        self.service = service

    def on_created(self, event):
        if event.is_directory:
            return

        # You can add your own logic here to process the new file
        self.service.execute()


class FileWatcher:
    def __init__(self):
        self._observer = Observer()

    def start(self, path, handler):
        self._observer.schedule(handler, path, recursive=False)
        self._observer.start()
        print(f'Listening for changes on "{path}"')
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self._observer.stop()
        finally:
            self._observer.join()

