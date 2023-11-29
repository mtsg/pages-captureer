# Pages-Captureer

Pages-Captureer is a script of Windows RPA, whereby you can capture pages automatically.

## Prerequisite

- OS:
  - **Windows**
- Environment:
  - **Python3** or more
    - See `Pipfile` for more details

## Installation

```bash
pipenv install
```

## Usage
1. Modify `FILE_NAME_PREFIX`, `TURNING_PAGE_POINT` and/or `CAPTURE_REGION` in `./main.py` as you like
    - To take the coordinates, `python -c "import pyautogui;print(pyautogui.position())"` would be helpful
1. `python ./main.py`

## Contributing

Anything welcome. No rule needed.

## License

[MIT](/LICENSE)