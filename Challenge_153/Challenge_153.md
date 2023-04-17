# Challenge 153: Tim, Avib, and Sushi

**Difficulty: 3/10  
Labels: Searching, Implementation**

Tim invited Avib for a dinner to a sushi restaurant. The restaurant is a bit unusual: it offers `n` pieces of sushi aligned in a row, and a customer has to choose a continuous subsegment of this sushi to buy.

The pieces of sushi are of two types: either with tuna or with eel. Let's denote the type of the `i`<sup>`th`</sup> from the left sushi as `t[i]`, where `t[i] = T` means it is with tuna, and `t[i] = E` means it is with eel.

Tim does not like tuna, Avib does not like eel. Tim wants to choose such a continuous subsegment of sushi that it has equal number of sushi of each type and each half of the subsegment has only sushi of one type. For example, subsegments `EEETTT` and `TTEE` are valid, but subsegment `TETETE` is not, because both halves contain both types of sushi.

Find the length of the longest continuous subsegment of sushi Tim can buy.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The only line contains a string `t` of length `n`, where `t[i]` denotes the type of sushi at the `i`th position.

Output a single integer, the length of the longest valid substring of `t`.

### Examples

#### Input

```rust
5
EEETTEE
TETETE
EETTTEEEE
TTTT
E
```

#### Output

```rust
‌4
2
6
0
0
```

- For test case 1, Tim can choose `EETT` or `TTEE`.
- For test case 4 and 5, there is no valid segment of sushi that satisfies the conditions.

### Note

- `1 <= n <= 50,000`
- `t[i]` is either `T` or `E`.

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C` (gnu17) / `C++` (c++20) - GCC 11.2
- `Ruby` 3.1
- `Golang` 1.19
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.68.2
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.10)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_153)
