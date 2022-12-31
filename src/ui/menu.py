"""General terminal menu"""
from simple_term_menu import TerminalMenu


class Menu:
    """General menu class to choose between supplied options"""

    def __init__(self):
        """Constructor for the class"""

    def show(self, commands, title=None, cancel=True):
        """
        Show a terminal menu with the supplied choices

        Parameters:
            commands: List of choices to show.
            title: Optional, default None. A title to be shown. I left empty no title is shown.
            cancel: Whether to include a cancel option in the list.
        """

        options = commands.copy()

        if cancel:
            options.append({
                "action": self.no_op,
                "message": "Cancel",
                "shortcut": "c"
            })

        options_strings = [self.get_option(o) for o in options]

        terminal_menu = TerminalMenu(
            options_strings,
            title=title,
            shortcut_key_highlight_style=(
                "fg_yellow",
            ))

        menu_entry_index = terminal_menu.show()

        return options[menu_entry_index]["action"]

    def no_op(self, *args):
        """No-op function for the cancel option"""

    def get_option(self, command):
        """
        Return string representation of a supplied menu choice.

        Parameters:
            command: Collection containing the menu choice message and shortcut.
        """
        if command["shortcut"]:
            return f"[{command['shortcut']}] {command['message']}"
        return command["message"]
