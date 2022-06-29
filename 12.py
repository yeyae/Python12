#문자열 포매팅 : 문자열을 정리하는 것
#'{인덱스0},{인덱스1}'.format(값0,값1)
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
f'나는 내년이면 {age+1}살이 된다.'
d = {'name' : '홍길동', 'age' : 30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
f'{"hi":<10}'

f'{"hi":>10}'

f'{"hi":^10}'

f'{"hi":=^10}'

f'{"hi":! 10}'

y = 3.42134234
f'{y:0.4f}'

#f문자열에서 {}문자를 표시하려면서 두개를 동시에 사용
f'{{ and }}'

#'!!!python!!!'
f'{"python":!^12}'

#문자열 관련 함수
#문자 개수 세기(count함수)
a = "hobby"
a.count('b')
#위치를 알려주기 1(find)
a = "Python is the best choice"
a.find('b')
a.find('k')
#위치를 알려주기 2(index)
a = "Life is too short"
a.index('t')
a.index('k')
#find 함수와 indx 함수의 다른 점 : 문자열 안에 존재하지 않는 문자를 찾으면 오류가 발생

#문자열 삽입(join)
",".join('abcd')

#소문자를 대문자로 바꾸기 (upper)
a = "hi"
a.upper()

#대문자를 소문자로 바꾸기(lower)
a="HI"
a.lower()
#왼쪽 공백 지우기(lstrip)
a="hi"
a.lstrip()
#오른쪽 공백 지우기(rstrip)
a="hi"
a.rstrip()
#양쪽 공백 지우기(strip)
a = "hi"
a.strip()
#문자열 바꾸기(replace)
a = "Life is too short"
a.replace("short", "long")
#문자열 나누기(split)
a = "Life is too short."
a.split()
 