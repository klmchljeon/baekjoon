# [Platinum III] Cow Lineup - 5851 

[문제 링크](https://www.acmicpc.net/problem/5851) 

### 성능 요약

메모리: 6248 KB, 시간: 204 ms

### 분류

자료 구조, 트리를 사용한 집합과 맵, 두 포인터

### 문제 설명

<p>Farmer John's N cows (1 <= N <= 100,000) are lined up in a row.  Each cow is identified by an integer "breed ID" in the range 0...1,000,000,000; the breed ID of the ith cow in the lineup is B(i).  Multiple cows can share the same breed ID.</p><p>FJ thinks that his line of cows will look much more impressive if there is a large contiguous block of cows that all have the same breed ID.  In order to create such a block, FJ chooses up to K breed IDs and removes from his lineup all the cows having those IDs.  Please help FJ figure out the length of the largest consecutive block of cows with the same breed ID that he can create by doing this.</p>

### 입력 

 <ul><li>Line 1: Two space-separated integers: N and K.</li><li>Lines 2..1+N: Line i+1 contains the breed ID B(i).</li></ul>

### 출력 

 <ul><li>Line 1: The largest size of a contiguous block of cows with identical breed IDs that FJ can create.</li></ul>

