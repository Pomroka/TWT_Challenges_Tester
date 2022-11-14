# Challenge 132: Fruits

**Difficulty: 2/10
Labels: Hash Map (Dictionary)**

You are at a dinner with a few family members and friends. Each person at the table told you their favourite fruit. Each person has a different name and each person likes a different kind of fruit.

## Task

You are given a number `T` and `T` test cases follow, for each test`case:

- The first line contains two integers `M` and `Q`, separated by a single space.
- The next `M` lines each contain two words `N` and `F`. `N` is the name of the person and `F` is the fruit they like.
- The next `Q` lines each contain one query. Each query is either in the form `N <fruit name>` or `F <person name>`.

For the first case, output the name of the person that likes the given fruit. For the second case, output the fruit that the person given likes.

This may sound confusing, but see the following example for clarification.

### Example

#### Input

```rust
1
3 4
Tim Apple
Avib Pear
Pear Orange
N Pear
F Pear
N Apple
F Tim
```

#### Output

```rust
Avib
Orange
Tim
Apple
```

For the first (and only) test case, we have three people.

- Tim likes Apple.
- Avib likes Pear (fruit).
- Pear (name) likes Orange.

The next four queries ask us:

1. Who likes Pear (fruit)? (Avib)
2. What does Pear (name) like? (Orange)
3. Who likes Apple? (Tim)
4. What does Tim like? (Apple)

### Note

- `1 <= T`
- `1 <= M <= 2000`
- `1 <= Q <= 3000`
- `1 <= |N|, |F| <= 20`
- Each name is **unique**.
- Each fruit is only liked by **exactly one** person.
- Names and Fruit names **may conflict**.
- `N` and `F` only contain English alphabets (`A-Za-z`).
- You won't face an unknown person or an unknown fruit in queries.

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C` (gnu17) / `C++` (c++20) - GCC 11.2
- `Ruby` 3.1
- `Golang` 1.19
- `Java` 19 (Open JDK) - use **"class Main"!!!**
- `Rust` 1.64
- `C#` 10 (.Net 6.0)
- `JavaScript` ES2022 (Node.js 18.10)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_132)
