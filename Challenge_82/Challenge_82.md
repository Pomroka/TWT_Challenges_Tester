# Challenge 82: Keyboard

## Task

You are given an int `n`, `n` testcases follow. For each testcase you are given the `string` typed on one line and the `avg speed` (integer) for the finger to move on the keyboard (units/s) in the next line.

## Details

Given the a `qwerty` keyboard, a `string`, `avg speed` of the finger to move calculate the time taken to type the `string`.

### Keyboard layout:
```
1234567890
qwertyuiop
Casdfghjkl
  zxcvbnm
   |spc|
```

- You have treat this as a `2d` plane and calculate distance accordingly. The distance between the two keys is the [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry).

- The number `1` is at `(0,0)`
- The letter `w` is at `(1,1)`
- The `C` at `(2,0)` represents `Caps Lock`. If there is a capital char in the string, you have to move your finger over to the `C` located at `(2,0)` move to the char and move to `C` again only if the next letter isn't a capital too.

- If there is a `space` in the string, you have to reach the closest point of the `spacebar` from the previous character typed.
The `spacebar` points are `(4,3)`, `(4,4)`, `(4,5)`, `(4,6)`, `(4,7)`. Pressing any one of these will trigger the `space` key, but you have to choose the closest one from the previous char and use that position to move to the next non space char.  
If char start with `space` use closest position to first non space char.

## Example

### Input:
```
3
asdZ 12349
2
z  m
1
 x
1
```

### Output:
```
12
8
1
```

### Explanation

a-s = 1  
s-d = 1  
d-Z = d-CL + CL-z = 3 + 3 = 6  
z-spc = 2 (closest is (4,3))  
spc(4,3) - 1 = 7  
1-2 = 1  
2-3 = 1  
3-4 = 1  
4-9 = 5  

Total distance = 25 units  
Average speed = 2 units/s  
Time = 25 // 2 = 12s (use integer division)

Challenge suggested by @KK1729

## Submissions

Code can be written in either of these languages:

- `Python` 3.9
- `C++` (G++ 10.3)
- `Ruby` 3.0
- `Golang` 1.16