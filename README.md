# Jetbrains Pycharm fail debugger

This project show a way to see the debugger of pycharm not behaving correctly from 2019.2 versions.

Simply put some breakpoints in the `apps.py` file on the `print` calls.
And launch the server in debug mode.

Debugger will work correctly with versions before 2019.2, but with above it will fail.

The main reason is about this line:  
`manager.start()`

A `multiprocessing.managers` is started, making the debugger failing :/

I'm so stuck with pycharm 1.4...

#### Install:

```bash
$> pip install -r requirements.txt
```
