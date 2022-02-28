# Challenge 92: Triangle size

**Difficulty: 2/10**

**N007** suggested a challenge about printing triangles according to input. However, **SnowballSH's** computer doesn't have enough disk space to run the challenge because the stdout files will be too big for big input sizes like `32,000` rows!
Help **SnowballSH** by finding how large the output will be for printing the triangle.

## Task

You are given a number `T` and `T` testcases follow, for each testcase:
You are given a number `R`. Starting from one `*`, **SnowballSH** wants to print `R` rows of `*`, each with one more star than the previous one. For example if `R = 4`:

```rs
*
**
***
****
```

If each `*` takes `8` bits (1 byte), and there will be a newline (`\n`, also one byte) at the end of each line, output the amount bytes in the resulting output modulo by `4096`
Assume there is no EOF characters or any other characters besides `*` and `\n`.

## Examples

### Input

```rs
6
4
100
13
42
12345
0
```

### Output

```rs
14
1054
104
945
3758
0
```

### Explanation

For case `1`, refer to the triangle above. There are `10 *s` and `4 newlines`, of a total of `14` bytes.
For case `2`, the actual result would be `5150`, but since it is greater than `4096`, we modulo it by `4096`, getting `5150 ≅ 1054 (mod 4096)`.

## Note

`1 <= T < 20,000`
`0 <= R < 30,000`
If your output is not within `[0, 4096)`, it is probably wrong.
If you don't know modulo arithmetic yet, modulo basically means the `%` operator in Python for this challenge.

Challenge modified from suggestion by N007#2552

## Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.16
- `Java` 18 (Open JDK)
- `Rust` 1.58
- `C#` 10 (.Net 6.0)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_92)
