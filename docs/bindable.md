# Bindable

Most properties of a widget are bindable. This means that you can pass a `Variable` to this property.
A `Variable` can be used to update the value of the property.

## Variable

You can create a manual `Variable` that is mutable and updates the value of the property when it is changed:

```python
from sora.widgets.bind import Variable

my_variable = Variable("Hello World")

my_variable.value = "Hello World 2"
```

## Polling Variable

You can also create a `Variable` that polls a function and updates the value of the property when the function returns a new value:

```python
from sora.widgets.bind import Variable

my_variable = Variable.interval(1, lambda: "Hello World")
```

### Variable.interval

The `Variable.interval` method takes two arguments:

- `interval`: `float`: The interval in seconds between each poll.
- `func`: `Callable[[], T]`: The function that returns the value of the variable.

## Listening Variable

You can also create a `Variable` that runs a subprocess and updates the value of the property when the subprocess returns a new value:

```python
from sora.widgets.bind import Variable

my_variable = Variable.listen(["pactl", "subscribe"])
```

### Variable.listen

The `Variable.listen` method takes one argument:

- `command`: `list[str] | str`: The command to run.
