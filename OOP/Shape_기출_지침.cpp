/*
문제 지침
1. 
<iostream> <castdio> <string> <cmath>를 사용할 수 있다.


2. Shape의 Subclass인 Rectangle을 구현하라.

- class 이름은 Rectangle이다.
- 멤버 변수로 width w와 height h를 가진다.
- 2개의 double을 argument로 갖는 생성자를 정의하라.
- calc_area 실행 시, 면적값 w * h을 return 하라.
- get_name() 실행 시, "Rectangle"을 return하라.


3. Rectangle의 Subclass Square를 구현하라.

- class 이름은 Square이다.
- 멤버 변수는 따로 선언하지 마라.
- 1개의 double을 argument로 갖는 생성자를 정의하되, parent class의 생성자를 활용하라.
- calc_area()는 구현할 필요 없으며, parent의 function을 사용하라.
- get_name() 실행 시, "Square"을 return하라.



4. Shape의 Subclass Triangle을 구현하라.

- class 이름은 Triangle이다.
- a, b, c 3개의 double 멤버 변수를 가진다.
- 3개의 double을 argument로 갖는 생성자를 정의하라.
- calc_area()실행 시, 면적값을 return 하라. cmath의 sqrt를 사용할 수 있다.
    - 면적값은 다음과 같이 계산된다. 
        s : (a+b+c) / 2       , area = sqrt(s*(s-a)*(s-b)*(s-c))
- get_name() 실행 시, "Triangle"을 return하라.


5.Triangle의 Subclass인 RightTriangle을 구현하라.

- class 이름은 RightTriangle이다.
- 멤버 변수는 따로 선언하지 마라.
- 2개의 double을 argument로 갖는 생성자를 정의하되, parent class의 생성자를 활용하라.
    - 이 때, c의 값은 sqrt(a^2 + b^2)이다. 
- calc_area()실행 시, 면적값 (a * b)  / 2를  return 하라. 
- get_name() 실행 시, "RightTriangle"을 return하라.


6.
모든 non-abstract class를 생성하고 그들의 함수를 실행하라.
입력값은 임의로 설정하여도 되며, 출력 결과 또는 return 포맷은 자유롭다.
제출 코드의 상단에 컴파일 명령어와 실행 명령어, 그리고 예상되는 출력 결과를 작성하라.

*/