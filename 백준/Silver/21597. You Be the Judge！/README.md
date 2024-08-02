# [Silver IV] You Be the Judge! - 21597 

[문제 링크](https://www.acmicpc.net/problem/21597) 

### 성능 요약

메모리: 31120 KB, 시간: 44 ms

### 분류

많은 조건 분기, 구현, 수학, 정수론, 소수 판정, 문자열

### 제출 일자

2024년 8월 2일 09:36:34

### 문제 설명

<p>Congratulations! You are now the judge of a programming contest! You’ve been put in charge of a problem, and since your problem may not have unique correct output, you’ve got to write an output checker for it.</p>

<p>Your problem is called “Good as Goldbach”, and it’s based on the Goldbach Conjecture (that any positive even integer greater than 3 can be expressed as the sum of two primes). A solving program’s output should have three numbers separated by whitespace: First, a positive even integer greater than 3 and less than or equal to 10<sup>9</sup>, and then two (positive) prime numbers which sum to the even number.</p>

<p>You must write a checker for this problem. Your checker should take the output of a contestant’s program, and determine whether or not it could possibly be correct. That is, determine if the contestant’s output consists only of three tokens separated by whitespace, the first of which is a positive even integer greater than 3 and less than or equal to 10<sup>9</sup>, and the next two are positive prime integers which sum to the first. The integers should be in base ten, with no signs or leading zeros. Any amount of white space anywhere except within an integer, including blank lines, is OK. Any other output, extra characters, missing numbers, etc. should be considered incorrect.</p>

### 입력 

 <p>The input will consist of from 0 to 1,000 lines. Each line consists of from 0 to 100 printable ASCII characters (with codes 32 through 126), or tabs.</p>

### 출력 

 <p>Output a single integer, which is 1 if the input could possibly be a correct output for the “Good as Goldbach” problem, or 0 if the input could not possibly be a correct output for the “Good as Goldbach” problem.</p>

