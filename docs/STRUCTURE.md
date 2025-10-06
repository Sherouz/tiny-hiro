# 🏗️ Project Structure: Tiny Hero

This document explains the folder and file structure of the **Tiny Hero** project. It’s designed to help you understand how the code is organized and where to find each component.

---

## 📂 Root Directory

| File/Folder        | Description                                                                     |
| ------------------ | ------------------------------------------------------------------------------- |
| `.gitignore`       | Specifies files and folders to be ignored by Git.                               |
| `cli.py`           | Main game controller; handles the flow of the game (intro, setup, battle loop). |
| `main.py`          | Entry point of the game; runs the CLI.                                          |
| `README.md`        | Project documentation and instructions.                                         |
| `LICENSE`          | MIT License for the project.                                                    |
| `requirements.txt` | List of Python dependencies (e.g., `rich`).                                     |
| `docs/`            | Documentation folder; contains `STRUCTURE.md`.                                  |
| `src/`             | Source code for the game.                                                       |

---

## 📂 src Directory

| File            | Responsibility                                                                   |
| --------------- | -------------------------------------------------------------------------------- |
| `actions.py`    | Defines hero actions like Attack, Strong Attack, and Heal.                       |
| `battle.py`     | Manages turn-based combat and initiative logic.                                  |
| `character.py`  | Base classes for characters (`Character`, `Hero`, `Enemy`) using OOP principles. |
| `health_bar.py` | Logic for displaying and updating colored health bars.                           |
| `setup.py`      | Game setup and initialization (creating hero, enemies, and starting state).      |
| `weapon.py`     | Weapon classes and stats; manage weapon creation and inventory.                  |
| `__init__.py`   | Marks `src` as a Python package.                                                 |

---

## 📂 src/ui Directory

| File            | Responsibility                                                                     |
| --------------- | ---------------------------------------------------------------------------------- |
| `animations.py` | ASCII animations for attacks, critical hits, and battle events.                    |
| `ascii_arts.py` | Stores ASCII art banners and visual assets.                                        |
| `display.py`    | Handles printing panels, messages, and other UI elements.                          |
| `fancy_ui.py`   | **Facade Pattern:** combines menu, display, and animation managers for unified UI. |
| `menu.py`       | Handles interactive menu selection for actions and equipment.                      |
| `ui.py`         | General UI utilities, helper functions, and screen clearing.                       |
| `__init__.py`   | Marks `src/ui` as a Python package.                                                |

---

## 📝 Notes

* The project is structured using **OOP principles** and **modular design**, so each file has a clear responsibility.
* The **UI folder** is separated to isolate display logic from game logic.
* Any new features (weapons, enemies, UI components) should follow this structure to maintain consistency.

---

*Last updated: Oct 06, 2025*

```
```