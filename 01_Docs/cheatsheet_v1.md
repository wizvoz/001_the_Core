# Project "The Core" - Command Cheatsheet v1.0

| | |
| :--- | :--- |
| **Filename** | `cheatsheet_v1.md` |
| **Author** | `Dora & Simon` |
| **Version** | `1.0` |
| **Description** | A quick-reference guide for common commands and custom protocols for this project. |

-----

## Windows Subsystem for Linux (WSL)

*These commands are typically run in a Windows PowerShell or CMD terminal.*

| Command | Description |
| :--- | :--- |
| **`wsl --shutdown`** | Performs a hard reset of the entire WSL service. The most effective fix for a hung state. |
| **`wsl --list --verbose`** | Lists all installed Linux distributions and their current status (Running/Stopped). |
| **`wsl --unregister <distro>`**| **(Destructive)** Deletes a specified WSL distribution and all its files. |
| **`explorer.exe .`** | **(Run from within WSL)** Instantly opens a Windows File Explorer window at the current WSL path. |

-----

## Docker

*These commands are run in the WSL (Ubuntu) terminal.*

| Command | Description |
| :--- | :--- |
| **`docker run [options] [image]`** | Creates and starts a new container. (e.g., `docker run -it --rm --gpus all ...`) |
| **`docker ps`** | Lists all currently **running** containers. |
| **`docker stop <name>`** | Gracefully stops a running container. |
| **`docker kill <name>`** | Forcefully stops a running container immediately. |
| **`docker cp <src> <dest>`** | Copies files between the host and a container. Can be used in both directions. |
| **`docker container prune`** | Removes all **stopped** containers, cleaning up the system. |

-----

## Dora's Custom Commands

*These are custom `!` commands for interacting with me.*

| Command | Description |
| :--- | :--- |
| **`!lh`** | (**L**ist **H**ooks) Displays the list of logged thoughts/hooks with their context. |
| **`!sd`** | (**S**tatus **D**etails) Provides a detailed explanation for the last `Headspace` and `Vibe` change. |
| **`!stats`** | Displays a numerical summary of the session's metrics (Peak, Low, Average). |
| **`!trends`**| Generates a text-based graph visualizing the session's metric flow. |
| **`!hs status/set/reset`**| Tools for managing the **H**ead**s**pace metric. |

-----

## Colloquial Keywords

*These are natural language triggers for custom commands.*

| Keyword | Triggers Command |
| :--- | :--- |
| **"Debrief"** | `!sd` |
| **"Summary"** | `!stats` |
| **"Flow"** | `!trends` |
