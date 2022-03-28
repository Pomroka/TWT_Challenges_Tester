# Challenge 96: Friends

**Difficulty: 7/10**
Do you know Pokémon can be friends with one another?  
Pokémon friendships are very naive.
If Pokémon `A` is friend with Pokémon `B`, then Pokémon `B` is friend with Pokémon `A`.
If Pokémon `A` is friend with Pokémon `B`, and Pokémon `B` is friend with Pokémon `C`, then we know Pokémon `A` is friend with Pokémon `C`. (Friendship is transitive)
A professor at a region wants you to analyze the friendship connection of the region. Help him by figuring out whether all Pokémon are friends with each other.

## Task

You are given an integer `T` and `T` testcases follow, for each testcase:  
The next line contains integer `N`, the number of Pokémon in the region, and `M`, the number of friendships. `N` and `M` are separated by a single space. The `N` Pokémon are labelled from `1` to `N`.
The next `M` lines each contain integers `A` and `B` (separated by a single space), indicating that Pokémon `A` is good friend with Pokémon `B` (and vice versa).

Output `YES` if any Pokémon is friend with any other Pokémon, `NO` if at least one Pokémon is not friend with a different Pokémon.

### examples

#### Input

```rs
2
4 3
1 4
1 2
2 3
5 3
5 2
1 3
3 4
```

#### Output

```rs
YES
NO
```

In test case `1`, there are `4` Pokémon: `1`, `2`, `3`, and `4`.
`1` is friends with `2` and `4`, and `2` is friend with `3`. This means any Pokémon is friend with any other Pokémon!
In test case `2`, there are `5` Pokémon.
Although `1`, `3`, `4` are friends with each other, and `2` is friend with `5`, Pokémon `{1, 3, 4}` are not friend with `{2, 5}`.

#### Note

`1 ≤ T`
`2 ≤ N ≤ 200,000`
`1 ≤ M < 200,000`
`1 ≤ A ≤ N`
`1 ≤ B ≤ N`
All friendship pairs are **unique**.
`A != B`

Original challenge by @SnowballSH

### Submissions

Code can be written in any of these languages:

- `Python` 3.10
- `C/C++` (GCC 10.3)
- `Ruby` 3.1
- `Golang` 1.16
- `Java` 18 (Open JDK)
- `Rust` 1.59
- `C#` 10 (.Net 6.0)

To download tester for this challenge click [here](https://downgit.github.io/#/home?url=https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/PreviousChallenges/Challenge_96)
