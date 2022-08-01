# Challenge 114: Matching

**Difficulty: 4/10**  
You are given two arrays of **distinct** integers `a` and `b`. You can cyclically shift the array `a` to the right any number of times. Let this shifted array be `c`. Your task is to find the maximum number of positions `i` for which `c[i] == b[i]` for any cyclic shift of the array `a`

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- an integer `n` in first line
- `n` integers that represent the array `a` in second line
- `n` integers that represent the array `b` in third line

### Examples

#### Input

```rs
2
4
1 2 3 4
2 3 1 4
5
1 2 3 4 5
3 4 5 2 1
```

#### Output

```rs
2
3
```

#### Explanation

1. For this case, shifting the array to the right `3` times gives the optimal answer
    [1, 2, 3, 4] shifted to the right 3 times will be [2, 3, 4, 1]
    there are two indices 0-indexed (`0`, `1`) where `c`<sup>`th`</sup> element is equal to the `b`<sup>`th`</sup> element
    `c[0] == b[0] = 2`, `c[1] == b[1] = 3`

    ```rs
    c = [2, 3, 4, 1]
         ↕  ↕
    b = [2, 3, 1, 4]
    ```

2. For second case:

    ```rs
    c = [3, 4, 5, 1, 2]
         ↕  ↕  ↕
    b = [3, 4, 5, 2, 1]
    ```

### Constraints

`1 <= n <= 10`<sup>`6`</sup>
`1 <= a[i], b[i] <= 10`<sup>`10`</sup>
All elements within array `a` and `b` are **unique**

### Note

`n`<sup>`th`</sup> Cyclic shift of an array is rotating the array by `n` times circularly

Challenge written by @KK1729

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.18
- `Java` 18 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.62
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.2)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_114)
