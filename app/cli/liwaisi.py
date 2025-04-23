#!/usr/bin/env python3

import curses
import time
import threading
from datetime import datetime


def draw_chat_ui(stdscr):
    curses.curs_set(1)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_MAGENTA)

    stdscr.clear()
    stdscr.refresh()

    h, w = stdscr.getmaxyx()
    header_height = 3
    footer_height = 3
    content_height = h - header_height - footer_height

    # WINDOWS
    header_win = curses.newwin(header_height, w, 0, 0)
    content_win = curses.newwin(content_height, w, header_height, 0)
    footer_win = curses.newwin(footer_height, w, header_height + content_height, 0)

    # DATA
    messages = [
        ("User", "Hola preséntate a ti mismo:"),
        ("AI", "Hola, Soy tu asistente personal de inteligencia artificial."),
    ]

    def append_message(origin, text):
        messages.append((origin, text))
        content_win.clear()
        content_win.bkgd(" ", curses.color_pair(2))
        max_lines = content_height - 2
        recent_msgs = messages[-max_lines:]  # Show only what fits
        for i, (who, msg) in enumerate(recent_msgs):
            content_win.addstr(i + 1, 2, f"{who}: {msg}")
        content_win.refresh()

    def update_header():
        while True:
            now = datetime.now()
            date_str = now.strftime("%a %d %B %Y")  # e.g. Fri 18 April 2025
            time_str = now.strftime("%H:%M:%S")  # e.g. 14:30:45
            header_text = f" AI Personal Assistant - {date_str} {time_str} "
            header_win.clear()
            header_win.bkgd(" ", curses.color_pair(1))
            header_win.addstr(1, max(2, (w - len(header_text)) // 2), header_text)
            header_win.refresh()
            # Move cursor back to footer
            footer_win.move(1, 2 + len(user_input))
            footer_win.refresh()
            time.sleep(1)

    # Start the header update thread
    threading.Thread(target=update_header, daemon=True).start()

    # Initial content render
    append_message("", "")  # Just to render messages initially

    # Enable wide char input
    footer_win.keypad(True)

    user_input = ""
    while True:
        # Render footer
        footer_win.bkgd(" ", curses.color_pair(3))
        footer_win.clear()
        footer_win.addstr(1, 2, user_input)
        # Move cursor to end of input
        footer_win.move(1, 2 + len(user_input))
        footer_win.refresh()

        try:
            key = footer_win.get_wch()
        except curses.error:
            continue

        if isinstance(key, str):
            if key == "\n":
                if user_input.strip():
                    append_message("User", user_input.strip())
                user_input = ""
            elif key == "\x7f":  # Backspace
                user_input = user_input[:-1]
            else:
                user_input += key
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            user_input = user_input[:-1]


def main():
    curses.wrapper(draw_chat_ui)


if __name__ == "__main__":
    main()
