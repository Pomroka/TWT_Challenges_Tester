# Challenge 189: Not-so-pro-log

**Difficulty: 3/10  
Labels: Logic, DFS**

In this logic puzzle of not-so-pro-log, you are to implement a simple variation of prolog.
A **feature** is either an indivisible object or a common description of objects. For example, "pizza" or "hungry" can be features.
A feature can be described by another feature. For example, "blue" can be described using "color," as blue is indeed a color.
Feature descriptions can be nested and are transitive. For example, if "fruit" is a "food" and "apple" is a "fruit", then "apple" is indeed a "food."
You are given a list of feature-feature relationships. You are to answer a question: Does X describe Y?

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers `N`, the number of features, and `M`, the number of relationships.
- The next `M` lines each contain two distinct integers `a` and `b`. This means `a` can describe `b`, or `b` is a part of `a`. (For example, a=food and b=pizza)
- The final line starts with a `?` followed by two distinct integers `x` and `y`.

If `y` can definitely be described using `x`, output `Yes`. Otherwise, output `No`.

### Examples

#### Input

```rust
3
‌3 2
1 3
3 2
? 1 2
6 5
4 6
4 3
3 1
3 5
1 2
? 4 2
4 3
2 3
1 2
1 4
? 3 1
```

#### Output

```rust
‌Yes
Yes
No
```

- For test case 1, let's say 1=food, 2=apple, 3=fruit.  
    We are given that fruit is a food and apple is a fruit. We are asked if apple is food. Yes!
- For test case 3, although 1 describes 3, it does not imply that 3 describes 1, so the answer is No.

### Note

- `1 <= T`
- `1 <= N, M <= 10,000`
- `1 <= a, b, x, y <= N`
- `a != b, x != y`

## Submissions

Code can be written in any of these languages:

- `Python` 3.11
- `C` (gnu17) / `C++` (c++20) - GCC 12.2
- `Ruby` 3.2
- `Golang` 1.21
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.72
- `C#` 11 (.Net 7.0)
- `JavaScript` ES2023 (Node.js 20.6)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_189)
