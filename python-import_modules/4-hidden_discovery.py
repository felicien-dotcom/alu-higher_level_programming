#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
             print(name)
```
### How it Works
* **`import hidden_4`**: Imports the compiled module (ensure `hidden_4.pyc` is in the same directory).
* **`dir(hidden_4)`**: Returns a list of all attributes and method names defined in the module.
* **`sorted(names)`**: Sorts the names in alphabetical (alpha) order.
* **`not name.startswith("__")`**: Filters out any special built-in names starting with a double underscore.
* **`if __name__ == "__main__":`**: Ensures the script does not run automatically when imported elsewhere.
<FollowUp>
If you need help with the next task or another script from this project, let me know!
</FollowUp>
