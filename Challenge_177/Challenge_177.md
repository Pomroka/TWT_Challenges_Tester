# Challenge 177: War

**Difficulty: 3/10  
Labels: Graphs, DFS, BFS, DSU**

You are the leader of Techindom, a country at war with another nation called Quantumania. Quantumania's resource supply is connected by many tunnels between crucial cities. Soldiers at Quantumania have incredible speed, so they can travel from one city to another instantly, as long as there is a path from one to another. Right now Quantumania cities are **all connected**.
Fortunately, you have the ability to destroy one city of your choice. When a city is destroyed, all tunnels connected to it disappears. Each city costs a different amount of money to destroy. You know Quantumania will surrender immediately when their kingdom is tore up into at least two parts, where there exists no path from any city in one part to any city of another.
Compute the minimum amount of money you need to spend to make Quantumania surrender. You may destroy **only one** city.

## Task

You are given a number `T` and `T` test cases follow, for each test case:

- The first line contains two integers, `n` and `m`, the number of cities (the cities are labelled 1, 2, ..., n) and the number of tunnels in Quantumania.
- The second line contains `n` integers, the cost of destroying each city.
- `m` lines follow. Each line contains two integers, `a` and `b`, indicating there is a two-way (undirected) tunnel between city `a` and `b`.

Output a single integer, the minimum cost to win by destroying one city. If it is impossible to win, output `-1`.

### Examples

#### Input

```rust
3
4 3
4 1 5 7
1 2
1 3
3 4
6 5
7 9 5 7 2 1
1 2
3 4
3 2
5 6
5 1
3 3
1 1 1
2 1
2 3
1 3
```

#### Output

```rust
4
‌2
-1
```

- For the first test case, you can disconnect the cities by destroying either city `1` or city `3`. City `1` has a lower cost, so we output `4`.
- For the third test case, it is impossible to disconnect the cities by destroying one.

## Note

- `1 <= T`
- `2 <= n <= 10`<sub>`4`</sub>
- `1 <= m <= 10`<sub>`4`</sub>
- `1 <= Cost[i] <= 10`<sub>`9`</sub>
- `1 <= a, b <= n`
- Each tunnel is distinct.
- It is the guaranteed that there exists a path from any city to any other city at the start.
This challenge does not promote war by any means.

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

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_177)
