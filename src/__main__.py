"""
Application can be started by calling this module.
Application for playing and viewing and testing algorithms for the game 2048.
"""

from ui.app import App


def main():
    """Starts the application."""
    app = App()
    app.run()


if __name__ == '__main__':
    main()
