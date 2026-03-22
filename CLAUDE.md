This is a standalone code formatter for BeebAsm 6502/65C02 assembly.

The formatter is a single Python file (`beebasm_fmt.py`) with no external
dependencies. It's used both as a CLI tool and as a pre-commit hook.

## Testing

Run the formatter on itself (it should be a no-op on non-asm files):
```bash
python3 beebasm_fmt.py --check test_fixtures/*.asm
```

## Key design decisions

- The formatter is intentionally a single file for easy distribution
- It must be idempotent: running twice produces no changes
- Inline `FOR ... : NEXT` is treated as a single instruction, not a block
- `{ }` scope braces affect indentation depth (like C blocks)
- `beebasm-fmt: off/on` comments allow hand-formatted sections
- `beebasm-fmt: align-cols` column-aligns `:` separators in tabular data
