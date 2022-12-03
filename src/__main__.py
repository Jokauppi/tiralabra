from ui.app import App
from ui.io.console_io import ConsoleIO


def main():
    io = ConsoleIO()
    app = App(io)
    app.run()


if __name__ == '__main__':
    main()
