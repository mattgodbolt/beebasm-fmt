# beebasm-fmt

An opinionated code formatter for [BeebAsm](https://github.com/stardot/beebasm)
6502/65C02 assembly source files.

## What it does

- Normalises indentation (4 spaces for instructions, 0 for labels)
- Aligns inline comments to a consistent column
- Normalises `:` statement separator spacing
- Double-indents inside `MACRO`/`FOR`/`IF` blocks
- Handles `{ }` scope braces (column 0, contents indented)
- Pads assignment (`=`) alignment

## Directives

Add these as comments in your source to control formatting:

| Directive | Effect |
|-----------|--------|
| `\ beebasm-fmt: off` | Stop formatting until `on` |
| `\ beebasm-fmt: on` | Resume formatting |
| `\ beebasm-fmt: align-cols` | Column-align `:` separators in following lines |

## Usage

### Standalone

```bash
python3 beebasm_fmt.py file.asm           # format in place
python3 beebasm_fmt.py --check file.asm   # check only (exit 1 if changes needed)
python3 beebasm_fmt.py --diff file.asm    # show diff without modifying
python3 beebasm_fmt.py *.asm              # format multiple files
```

### As a pre-commit hook

Add to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/mattgodbolt/beebasm-fmt
    rev: v0.1.0
    hooks:
      - id: beebasm-fmt
```

Then run:

```bash
pre-commit install
```

## Requirements

Python 3.6+. No external dependencies.

## License

MIT
