# Stepik QA automation course

## Adding custom command line options

1. `browser` fixture is defined in *conftest.py* file.
2. **--language** command line option is defined and processed in *conftest.py* file. <br>
Value specified with the option can be used in test through `language` fixture.
Default value is set to be *en-gb* (British English).
3. Testing is done within the `TestCart` class in *test_items.py* file:
- `test_add_button_present` does what is asked in the task.
- Other test are beyond the task and are skipped by default.