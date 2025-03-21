# 🗼Catppuccin Factory 🏭

Forked from [catppuccin-factory](https://github.com/fxzzi/catppuccin-factory.git) by @fxzzi

A simple cli to convert any image to a catppuccin themed wallpaper

![example](./imgs/example.png)

## Installation

1. Clone the repo.
2. Install the required packages using pip as shown below:

    ```bash
    pip3 install rich image-go-nord argparse
    ```

3. Edit the file ```conv.py``` line 14 with your user name, DO NOT CHANGE THE DIR, IT WILL NOT WORK AS EXPECTED, IF YOU WANT TO EDIT IT THEN DO IT IN BOTH ```conv.py``` and ```cat.sh```.
4. Install it with:

    ```bash
    sudo make install
    ```

## Usage

from your terminal run:

```bash
catFactory
```

or

```bash
catFactory /path/to/image/
```

 All the outputs will be in ~/Pictures/cat

## UNINSTALL

 1. ```cd``` into the repo folder.
 2. Uninstall it with:

    ```bash
    sudo make uninstall
    ```

## Credits

- Credit to @fxzzi for the original repo, this is a fork of it.
- **Made** with [Schrodinger-Hat's ImageGoNord](https://github.com/Schrodinger-Hat), but with the Onedark palette
- **Text User Interface (TUI)** made with [rich](https://github.com/willmcgugan/rich)
