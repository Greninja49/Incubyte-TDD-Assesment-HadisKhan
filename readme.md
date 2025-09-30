# String Calculator TDD Kata

Implement a String Calculator with a method:

`int add(string numbers)`

Rules (summary):

- "" -> 0
- "1" -> 1
- "1,5" -> 6
- Allow new lines between numbers ("1\n2,3" -> 6)
- Support custom delimiter syntax: `//[delimiter]\n[numbers...]` e.g. `//;\n1;2` -> 3
- Negative numbers: raise exception with message `negative numbers not allowed <n>`; if multiple, list them separated by commas.
- pytest command for terminal in root folder: `python -m pytest tests -q`
