# Computer History

A simple Python program that tells you which stage of computer history a given year belongs to.

根据年份查询计算机发展阶段的小工具。

## Stages / 阶段划分

| End Year | Stage |
|---------|-------|
| 1945 | 没有计算机 (No computers) |
| 1957 | 电子管计算机 (Vacuum tube computers) |
| 1964 | 晶体管计算机 (Transistor computers) |
| 1970 | 集成电路计算机 (Integrated circuit computers) |
| 1980 | 大规模集成电路计算机 (Large-scale integration computers) |
| ∞ | 超大规模集成电路与智能计算机 (VLSI & intelligent computers) |

> Note: the year in each row is the **last year** of that stage.

## Usage / 使用

Run the script:

```bash
python computer_history.py
```

Then type a year and press Enter:

```
Please input the year:  1950
电子管计算机
```

Type `end` to quit:

```
Please input the year:  end
```

Non-numeric input will show a red hint and ask again.

## Requirements

- Python 3.x
- No third-party dependencies

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
