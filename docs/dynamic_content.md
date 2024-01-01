# Dynamic Content

You often want to display dynamic content in your widgets. For example, you might want to display the current time or the current volume.

In sora you can achieve this by binding a `Variable` or a `Service` to a property of a widget. Note that not all properties are bindable.

## Variable

A `Variable` is a object that holds a single value.

### Properties

- `value`: The value of the variable (Read, Write)

### Methods

- `stop_interval()`: Stops the interval of the variable if running.
- `stop_listener()`: Stops the listener of the variable if running.
- `bind()`: Returns a `Binding` which can be used to bind the variable to a property of a widget.

### Static Methods

- `interval(interval: int, func: Callable[[], Any])`: Creates a variable that changes its value every `interval` seconds.
- `listen(command: list[str] | str)`: Creates a variable that listens on the output of a command and updates its value on a new line.

```python
my_var = Variable("Hello World")
```

### Interval

An interval variable is a variable that changes its value every `x` seconds.

```python
my_var = Variable.interval(1, lambda: "Hello World")
```

### Listener

A listener variable listens on the output of a command and updates its value on a new line. You can create a listener variable by calling the `listen` method.

```python
my_var = Variable.listen(["bash", "-c", "my-command"])
```

### Updating the value

```python
my_var.value = "Hello World"
```

### Retrieving the value

```python
print(my_var.value)
```

### Bind

The `bind` method returns a `Binding` which can be used to bind the variable to a property of a widget.

```python
my_var = Variable("Hello World")

my_label = Label(
    LabelProps(
        label=my_var.bind(),
    ),
)
```

You can also provide a mapper function that maps the value of the variable to a different value.

```python
my_var = Variable("Hello World")

my_label = Label(
    LabelProps(
        label=my_var.bind().map(lambda value: value.upper()),
    ),
)
```

## Service

A `Service` is object that can contain multiple values and can be used to provide values from an external service. There are some built-in services that you can use.

It is provided as a Singleton, so it only runs once for all widgets.

### Usage

The usage of a service is similar to a variable. But you can specify which property of the service you want to bind to.

```python
my_label = Label(
    LabelProps(
        label=SomeService().bind("some_value").map(lambda value: value.upper()),
    ),
)
```

### Built-in Services

- [`i3`](services/i3.md): Provides information about the i3 window manager.
