# [Platinum III] 근성아 일 좀 하자 - 34410 

[문제 링크](https://www.acmicpc.net/problem/34410) 

### 성능 요약

메모리: 144396 KB, 시간: 916 ms

### 분류

구현, 자료 구조, 시뮬레이션, 우선순위 큐, 연결 리스트

### 제출 일자

2025년 9월 21일 22:38:33

### 문제 설명

<blockquote>
<p><em>근성은 나무에 관심이 많다.</em></p>
</blockquote>

<p>평소 나무를 깨끗이 관리해 온 근성은 그 능력을 인정받아 북구청 청소행정과에 근무하게 되었다. 근성은 길거리에 버려진 쓰레기 더미를 수거하는 업무를 맡았는데, 어느 날 폭우로 인해 버려진 쓰레기 더미가 빗물을 떠다니게 되었다.</p>

<p>길은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>번 칸부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>번 칸까지의 일직선 모양이며, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>번 칸의 왼쪽 경계와 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>번 칸의 오른쪽 경계는 벽으로 막혀 있다.</p>

<p>처음에는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>개의 쓰레기 더미가 서로 <strong>한 칸 이상 떨어진 상태</strong>로 놓여있다. 각 쓰레기 더미는 위치와 무게, 이동 방향(오른쪽 또는 왼쪽)을 갖는다. 또한 쓰레기 더미는 정확히 한 칸의 길이를 차지한다.</p>

<p>움직이는 쓰레기 더미는 다른 쓰레기 더미 또는 벽에 충돌할 때까지 항상 이동 방향에 따라 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>의 속도로 이동한다. 이때 충돌은 칸의 경계가 아닌 곳에서 일어날 수도 있다.</p>

<p>쓰레기 더미가 움직이며 발생하는 충돌에 대한 규칙은 다음과 같다.</p>

<ul>
	<li>벽은 질량이 무한하며, 움직이는 쓰레기 더미가 벽에 부딪히면 그 자리에서 즉시 정지한다. 벽에 붙어있는 쓰레기 더미와 충돌하는 때도 동일하다.</li>
	<li>두 쓰레기 더미끼리 충돌하는 경우 하나의 쓰레기 더미로 합쳐진다.
	<ul>
		<li>합쳐진 쓰레기 더미의 길이와 무게는 두 쓰레기 더미의 합이 된다.</li>
		<li>이동 방향은 더 무거운 쓰레기 더미의 이동 방향을 따른다. 단, 두 쓰레기 더미의 무게가 같은 경우 그 자리에서 정지한다.</li>
	</ul>
	</li>
	<li>정지한 쓰레기 더미에 충돌하는 상황 또한 두 쓰레기 더미가 충돌하는 규칙을 따른다. 단, 양쪽에서 동시에 정지한 쓰레기 더미에 충돌하는 경우 아래와 같이 합쳐진다.
	<ul>
		<li>합쳐진 쓰레기 더미의 길이와 무게는 세 쓰레기 더미의 합이 된다.</li>
		<li>움직이는 두 쓰레기 더미의 무게가 같거나, 각 무게가 정지한 쓰레기 더미보다 가볍거나 같다면 그 자리에서 정지한다. 그렇지 않은 경우, 합쳐진 쓰레기 더미의 이동 방향은 더 무거운 쓰레기 더미의 이동 방향을 따른다.</li>
	</ul>
	</li>
	<li>합쳐진 쓰레기 더미는 하나의 쓰레기 더미로 이후 동일하게 규칙을 따른다.</li>
</ul>

<p>근성은 시간이 지나면 <strong>모든 쓰레기 더미가 결국 정지하게 된다</strong>는 사실을 알게 되었다. 근성을 도와 모든 쓰레기 더미가 멈춘 시점과 그때의 쓰레기 더미의 수를 계산하자.</p>

### 입력 

 <p>첫 번째 줄에 길의 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>과 초기 쓰레기 더미의 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>이 공백으로 구분되어 주어진다.</p>

<p>두 번째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>개의 줄에 걸쳐 각 쓰레기 더미의 위치 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x_i$</span></mjx-container>, 무게 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D464 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>w</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$w_i$</span></mjx-container>, 이동 방향 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$d_i$</span></mjx-container>(<span style="color:#e74c3c;"><code>L</code></span> 또는 <span style="color:#e74c3c;"><code>R</code></span>)이 공백으로 구분되어 주어진다. <span style="color:#e74c3c;"><code>L</code></span>과 <span style="color:#e74c3c;"><code>R</code></span>은 각각 왼쪽, 오른쪽 이동을 나타낸다.</p>

### 출력 

 <p>첫 번째 줄에 모든 쓰레기 더미가 멈춘 시간과 그때의 쓰레기 더미의 수를 공백으로 구분하여 출력한다. 이때 <strong>시간은 소수점 첫째 자리까지</strong> 출력해야 하며, 항상 답을 정확하게 출력할 수 있음을 증명할 수 있다.</p>

