# Week 02 Test Cases

## Task 1：Sequence Clean

1. 輸入 `5 3 5 2 9 2 8 3 1`
   - `dedupe: 5 3 2 9 8 1`
   - `asc: 1 2 2 3 3 5 5 8 9`
   - `desc: 9 8 5 5 3 3 2 2 1`
   - `evens: 2 2 8`

2. 輸入 `4 4 2 2 1 1 3`
   - `dedupe: 4 2 1 3`
   - `asc: 1 1 2 2 3 4 4`
   - `desc: 4 4 3 2 2 1 1`
   - `evens: 4 4 2 2`

3. 輸入 `10 7 6 5 4`
   - `dedupe: 10 7 6 5 4`
   - `asc: 4 5 6 7 10`
   - `desc: 10 7 6 5 4`
   - `evens: 10 6 4`

## Task 2：Student Ranking

1. 輸入：
   ```text
   6 3
   amy 88 20
   bob 88 19
   zoe 92 21
   ian 88 19
   leo 75 20
   eva 92 20
   ``` 
   輸出：
   ```text
   eva 92 20
   zoe 92 21
   bob 88 19
   ```

2. 輸入：
   ```text
   4 2
   amy 90 21
   bob 90 20
   carl 85 22
   dora 90 20
   ```
   輸出：
   ```text
   bob 90 20
   dora 90 20
   ```

3. 輸入：
   ```text
   3 5
   amy 80 18
   bob 70 19
   cat 60 20
   ```
   輸出：
   ```text
   amy 80 18
   bob 70 19
   cat 60 20
   ```

## Task 3：Log Summary

1. 輸入：
   ```text
   8
   alice login
   bob login
   alice view
   alice logout
   bob view
   bob view
   chris login
   bob logout
   ```
   輸出：
   ```text
   bob 4
   alice 3
   chris 1
   top_action: login 3
   ```

2. 輸入：
   ```text
   5
   alice login
   alice login
   bob view
   bob view
   carl login
   ```
   輸出：
   ```text
   alice 2
   bob 2
   carl 1
   top_action: login 3
   ```

3. 輸入：
   ```text
   3
   alice logout
   bob login
   alice login
   ```
   輸出：
   ```text
   alice 2
   bob 1
   top_action: login 2
   ```
