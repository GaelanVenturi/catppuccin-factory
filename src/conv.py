#!/usr/bin/env python3
"""
Catppuccin Factory: A script to manufacture Catppuccin-themed wallpapers.

This script processes images by applying a custom Catppuccin color palette
and saves the output images to a designated directory. It supports both
command-line arguments and interactive user input for specifying image paths.

Features:
- Dynamically sets the output directory based on the operating system.
- Handles user interruptions gracefully (Ctrl+C).
- Provides a CLI and TUI for user interaction.

"""

import signal
import argparse
import sys
import os
import platform

from ImageGoNord import GoNord
from rich.console import Console
from rich.panel import Panel

# Set the PATH dynamically based on the operating system
if platform.system() == "Windows":
    PATH = os.path.expanduser(r"~\Pictures\cat-factory-output")
else:
    PATH = os.path.expanduser("~/Pictures/cat-factory-output")

# Ensure the directory exists
os.makedirs(PATH, exist_ok=True)


def main():
    """
    Main entry point for the script.

    Sets up signal handling, initializes the console and GoNord instance,
    and processes images based on user input or command-line arguments.
    """
    signal.signal(signal.SIGINT, signal_handler)
    console = Console()

    cat_factory = GoNord()
    cat_factory.reset_palette()
    add_cat_palette(cat_factory)

    # Checks if there's an argument
    if len(sys.argv) > 1:
        image_paths = from_command_argument()
    else:
        image_paths = from_tui(console)

    for image_path in image_paths:
        if os.path.isfile(image_path):
            process_image(image_path, console, cat_factory)
        else:
            console.print(
                f"❌ [red]We had a problem in the pipeline! \nThe image at '{image_path}' "
                f"could not be found! \nSkipping... [/]"
            )
            continue


def from_command_argument():
    """
    Parses command-line arguments to get image paths.

    Args:
        console (Console): The Rich console instance for displaying messages.

    Returns:
        list: A list of image paths provided via the command line.
    """
    command_parser = argparse.ArgumentParser(
        description="A simple CLI to manufacture Catppuccin-themed wallpapers."
    )
    command_parser.add_argument(
        "Path", metavar="path", nargs="+", type=str, help="The path(s) to the image(s)."
    )
    args = command_parser.parse_args()

    return args.Path


def from_tui(console):
    """
    Prompts the user to input image paths interactively.

    Args:
        console (Console): The Rich console instance for displaying messages.

    Returns:
        list: A list of image paths provided by the user.
    """
    console.print(
        Panel(
            "🏭 [bold magenta] Catppuccin Factory [/] 🏭",
            expand=False,
            border_style="magenta",
        )
    )

    return [
        os.path.expanduser(path)
        for path in console.input(
            (
                "🖼️ [bold yellow]Which image(s) do you want to manufacture? "
                "(image paths separated by spaces):[/] "
            )
        ).split()
    ]


def process_image(image_path, console, cat_factory):
    """
    Processes a single image by applying the Catppuccin palette.

    Args:
        image_path (str): The path to the image to be processed.
        console (Console): The Rich console instance for displaying messages.
        cat_factory (GoNord): The GoNord instance for image processing.
    """
    image = cat_factory.open_image(image_path)

    console.print(f"🔨 [blue]manufacturing '{os.path.basename(image_path)}'...[/]")

    # Save the new image in the designated output directory
    save_path = os.path.join(PATH, "cat_" + os.path.basename(image_path))

    cat_factory.convert_image(image, save_path=save_path)
    console.print(f"✅ [bold green]Done![/] [green](saved at '{save_path}')[/]")


def add_cat_palette(cat_factory):
    """
    Adds the Catppuccin color palette to the GoNord instance.

    Args:
        cat_factory (GoNord): The GoNord instance to which the palette is added.
    """
    cat_palette = [
        "#F2CDCD",
        "#DDB6F2",
        "#F5C2E7",
        "#E8A2AF",
        "#F28FAD",
        "#F8BD96",
        "#FAE3B0",
        "#ABE9B3",
        "#B5E8E0",
        "#96CDFB",
        "#89DCEB",
        "#161320",
        "#1A1826",
        "#1E1E2E",
        "#302D41",
        "#575268",
        "#6E6C7E",
        "#988BA2",
        "#C3BAC6",
        "#D9E0EE",
        "#C9CBFF",
        "#F5E0DC",
    ]

    for color in cat_palette:
        cat_factory.add_color_to_palette(color)


def signal_handler():
    """
    Handles the SIGINT signal (Ctrl+C) to gracefully exit the program.

    Args:
        signal (int): The signal number.
        frame (FrameType): The current stack frame.
    """
    print()
    sys.exit(0)


if __name__ == "__main__":
    main()
