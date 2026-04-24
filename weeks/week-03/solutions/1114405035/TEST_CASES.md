# Week 03 Test Cases

## UVA 100：Collatz 序列

1. 輸入：`1 10`
   - 輸出：`1 10 20`

2. 輸入：`100 200`
   - 輸出：`100 200 125`

3. 輸入：`201 210`
   - 輸出：`201 210 89`

## UVA 118：機器人模擬

1. 輸入：
   ```
   5 3
   1 1 E
   RFRFRF
   ```
   - 輸出：`3 1 S`

2. 輸入：
   ```
   5 3
   3 2 N
   FRRFLLFFRRFLL
   ```
   - 輸出：`3 3 N LOST`

3. 輸入：
   ```
   5 3
   0 3 W
   LLFFFLFLFL
   ```
   - 輸出：`2 3 S`

## UVA 272：TeX 引號

1. 輸入：`"To be or not to be," said Hamlet.`
   - 輸出：``"To be or not to be," said Hamlet.``

2. 輸入：`He said, "I am not a number!"`
   - 輸出：`He said, ``I am not a number!''`

## UVA 299：火車排序

1. 輸入：
   ```
   3
   3
   1 3 2
   4
   4 3 2 1
   2
   2 1
   ```
   - 輸出：
     ```
     Optimal train swapping takes 1 swaps.
     Optimal train swapping takes 6 swaps.
     Optimal train swapping takes 1 swaps.
     ```

## UVA 490：文字旋轉

1. 輸入：
   ```
   Hello
   World
   ```
   - 輸出：
     ```
     HW
     eo
     lr
     ll
     od
     ```

## Robot Core 測試

1. 機器人旋轉測試
   - 初始：N → 左轉 → W → 左轉 → S

2. 正常移動測試
   - (0,0,N) + F → (0,1,N)

3. LOST 與 scent 測試
   - (5,5,N) + F → LOST, scent 添加 (5,5,N)

4. scent 保護測試
   - 相同位置方向的 F 指令被忽略