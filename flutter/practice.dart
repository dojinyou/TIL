// dartpad.dartlang.org
4강 Strings
void main() {
  String name = "코드팩토리";
  
  print(name);
  
  String name2 = "슬기";
  String sentence = '는 레드벨벳 멤버입니다.';
  
  print(name2 + sentence);
  print('$name2$sentence');
  
  int count = 5;
  String sentence2 = '레드벨벳 멤버는 $count명 입니다.';
  
  print(sentence2);
}

5강 boolean
void main(){
  bool isTrue = true;
  bool isFalse = false;
}


6강 var, dynamic 타입
void main() {
  dynamic name = '코드팩토리';
  
  print(name);
  
  name = '슬기';
  
  print(name);
  
  name = 1;
  
  print(name);  
}

var 타입 = 선언과 동시에 타입을 정하면 바꿀수 없음
dynamic 타입 = 변수 타입을 바꾸어도 됨

7강 List 타입
void main(){
  List redVelvetList = [];
  
  print(redVelvetList);
  
  redVelvetList.add('아이린');
  redVelvetList.add('슬기');
  redVelvetList.add('조이');
  
  print(redVelvetList);
  
  redVelvetList.removeAt(1);
  
  print(redVelvetList);
  
  print(redVelvetList[0]);
  print(redVelvetList[1]);
  
  redVelvetList[0] = '코드팩토리';
  
  print(redVelvetList);
  
  print('-------------------------');
  
  List<String> redVelvetList2 = [];
  
  redVelvetList2.add('슬기');
  
  print(redVelvetList2);
  
  print('-------------------------');
  
  List redVelvetList3 = [
    '아이린',
    '슬기',
    '웬디',
    '조이',
    '예리',
  ];
  
  print(redVelvetList3);
  
  // List redVelvetList4 = new List.from([
  //   '아이린',
  //   '슬기',
  //   '웬디',
  //   '조이',
  //   '예리',
  // ]);
  List redVelvetList4 = new List.from(redVelvetList3);
  print(redVelvetList3);
  print(redVelvetList4);
	print('edited element 1 of list 4 ')
  print(redVelvetList3);
  redVelvetList4[0] = '삭제';
  print(redVelvetList4);
  
  print(redVelvetList4.length);
}

8강 Map 타입 (Key Value Pair)
void main(){
  Map dictionary = {
    'apple': '사과',
    'banana': '바나나',
    'watermelon': '수박',
  };
  
  print(dictionary);
  
  print(dictionary['apple']);
  print(dictionary['banana']);
  
  Map dictionary2 = {}; 
  print(dictionary2);
  
  dictionary2.addAll({
    'apple': '사과',
    'banana': '바나나',
    'watermelon': '수박',
  }); 
  print(dictionary2);
  
  dictionary2.remove('apple');
  print(dictionary2);
  
  dictionary2['banana'] = '코드팩토리';
  print(dictionary2);
  
  print('----------------------------------');
  
  Map dictionary3 = new Map();
  
  Map dictionary4 = new Map.from({
    'apple': '사과',
    'banana': '바나나',
  });
  
  print(dictionary4);
  print(dictionary4.keys.toList());
  print(dictionary4.values.toList());
  
  print('----------------------------------');
  
  Map<String, int> price = {
    'apple': 2000,
    'banana': 4000,
    'watermelon': 6000,
  };
  print(price);
}

9강 변수에 대한 몇가지 약속
void main(){
  String name = '코드팩토리';
  
  String _name = '프라이빗변수';
  
  String Name = 'class를 선언할 때';
}

10강 Final, Const 
void main(){
  final String name = '코드팩토리'; // 런타임(코드가 컴파일이 다 되고 실행이 되는 순간에 선언이 되면)
  const String name2 = '레드벨벳'; // 컴파일(컴파일이 되는 순간에 값이 지정되어있어야 함)
  
  print(name);
  
  final DateTime now = DateTime.now(); // const는 안됨
  
  print(now);
  
  Future.delayed( // 1초 딜레이 후 실행하는 문법
    Duration(milliseconds: 1000),
    (){
      final DateTime now2 = DateTime.now(); // const는 안됨
      
      print(now2);
    }
  );
}

11강 Operators
void main(){
  int number = 2;
  
  print(number + 2);
  print(number - 2);
  print(number * 2);
  print(number / 2);
  print(number % 2);
  print(number % 3);
  
  print('-----------------------');
  
  number++;
  print(number);
  number--;
  print(number);
  
  print('-----------------------');

  
  int number2 = 10;
  print(number2);
  number2 = 8;
  print(number2);
  number2 ??= 4;
  print(number2);
  
  print('-----------------------');

//   int number3;
//   number3 ??= 4;
//   print(number3);
  
  int number4 = 2;
  number4 += 1;
  print(number4);
  number4 -= 1;
  print(number4);
  number4 *= 2;
  print(number4);
//   number4 /= 2; 나누기를 하는순간 double이 되기 때문에 int number4는 수용하지 못함 
  
  print('-----------------------');

  int num1 = 1;
  int num2 = 2;
  
  print(num1 < num2);
  print(num1 > num2);
  print(num1 <= num2);
  print(num1 >= num2);
  print(num1 == num2);
  print(num1 != num2);
  
  print('-----------------------');
  
  int n1 = 1;
  
  print(n1 is int);
  print(n1 is String);
  print(n1 is bool);
  
  print(n1 is! String);
  
  print('-----------------------');
  
  bool result = 12 > 10 && 1 < 0;
  bool result2 = 12 > 10 || 1 < 0;
  
  print(result);
  print(result2);
}

12강 if, Switch 문
void main(){
  int number = 21;
  
  if (number % 4 == 0){
    print('4의 배수입니다.');
  } else if (number % 4 == 1) {
    print('나머지가 1입니다.');
  } else {
    print('어떤 조건에도 맞지 않습니다.');
  }
  
  print('----------------------------');
  
  switch (number % 4){
    case 0:
      print('4의 배수입니다.');
      break;
      
    case 1:
      print('나머지가 1입니다.');
      break;
    
    default:
      print('어떤 조건에도 맞지 않습니다.');
      break;
  }
}

13강 for, while Loop
void main(){
  print('--------for-------');
  List<int> numbers = [
    1,
    1,
    2,
    3,
    5,
    8,
  ];
  
  int total = 0;
  
  for (int i = 0; i < numbers.length; i ++) {
    print(numbers[i]);
    total += numbers[i];
  }
  print(total);
  
  print('------------------');
  total = 0;
  for (int number in numbers){
    print(number);
    total += number;
  }
  print(total);
  print('-------while------');
  int num = 10;
  
  while(num < 20){
    print(num);
    
    num++;
    
    if (num == 15) {
      break;
    }
  }
  print('-----do while-----');
  num = 10;
  
  do {
    print(num);
    
    num++;
  } while(num < 10);
}

14강 Enum 타입
enum Status {
  approved,
  rejected,
  pending,
}

void main(){
  // 승인 approved
  // 반려 rejected
  // 대기 pending
  
  Status status = Status.approved;
  
  if (status == Status.approved) {
    print('승인 되었습니다.');
  } else {
    print('반려나 대기 되었습니다.');
  }
  
  print(Status.values.toList());
}

15강 function
void main(){
  List<int> testList = [
    1,
    1,
    2,
    3,
    5,
    8,
  ];
    
  List<int> testList2 = [
    10,
    20,
    30,
    40,
    50,
  ];
  
  int result = addList(testList, 1, 2);
  int result2 = addList(testList2, 1);
  int result3 = addList2(testList, 1, 
    b : 2,
    d : 4,
  );
  print(result);
  print(result2);
}

int addList(List<int> testList, int a, [int b = 3]){
  print('b의 값 : $b');

  int total = 0;
  
  for(int i = 0; i < testList.length; i++){
    total += testList[i];
  }
  return total;
}

int addList2(List<int> testList, int a, {
  int b=1,
  int c=1,
  int d=1,
}){
  print('b:$b, c:$c, d:$d');

  int total = 0;
  
  for(int i = 0; i < testList.length; i++){
    total += testList[i];
  }
  return total;
}

16강 Typedef
void main(){
  calculate(1, 2, add);
  calculate(3, 2, subtract);
}

typedef Operation(int x, int y);

void add(int x, int y){
  print('x 더하기 y 는 ${x+y}입니다.');
}

void subtract(int x, int y){
  print('x 빼기 y 는 ${x-y}입니다.');
}

void calculate(int x, int y, Operation oper){
  oper(x, y);
}

17강 Class #1 선언 및 Constructor
void main(){
  // OOP - Object Oriented Programming
  // 객체지향 프로그래밍
  
  // Instantiation 인스턴스화
  // Instance 인스턴스
  
  Idol seulgi = new Idol(
    '슬기',
    '레드벨벳',
  );
  
  seulgi.sayName();
  print(seulgi.name);
  print(seulgi.group);
  
  Idol rm = new Idol.fromMap({
    'name' : 'rm',
    'group' : 'BTS',
  });
  
  rm.sayName();
  print(rm.name);
  print(rm.group);
}

class Idol {
  final String name; // final을 사용해야 처음 넣은 값을 바꿀수가 없게 할 수 있다
  final String group;
  
  Idol(
    String name,
    String group,
  ) : this.name = name,
      this.group = group;
  
  Idol.fromMap(
    Map input,
  ) : this.name = input['name'],
      this.group = input['group'];
  
  void sayName(){
    print('제 이름은 ${this.name}입니다.');
  }
}

18강 Class #2 Getter and Setter
void main(){
  // Getter Setter
  // Getter -> 값을 가져올 때
  // Setter -> 값을 변경할 때
  
  Idol seulgi = new Idol(
    '슬기',
    '레드벨벳',
  );
  
  seulgi.sayName();
  
  seulgi._name;
  
  print(seulgi._name); 
  print(seulgi.name); // 특이한점! 함수처럼 ()를 안붙이고 변수처럼 사용.
  
  seulgi.setName = '코드팩토리';
  
  print(seulgi.name);
}

class Idol {
  // private variable = 같은 파일내에 있어야만 가져올 수 있다.
  String _name; 
  String _group;
  
  Idol(
    String name,
    String group,
  ) : this._name = name,
      this._group = group;
  
  void sayName(){
    print('저는 ${this._name}입니다.');
  }
  
  get name{
    return this._name;
  }
  
  set setName(String name){
    this._name = name;
  }
}

19강 Class #3 inheritance (상속)
void main(){
  // Inheritance
  // 상속
  
  print('-----Idol----');
  
  Idol seulgi = new Idol(name: '슬기', group: '레드벨벳');
  
  seulgi.sayName();
  seulgi.sayGroup();
  
  print('----BoyGroup----');
  
  BoyGroup rm = new BoyGroup('RM', 'BTS');
  
  // 자식은 부모의 모든 변수와 함수를 상속 받지만,
  // 부모는 자식의 어떠한 것도 상속받지 않는다.
  print(rm.name);
  print(rm.group);
  rm.sayMale();
  
  print('----GirlGroup----');
  GirlGroup chorong = new GirlGroup('초롱', '에이핑크');
  
  print(chorong.name);
  print(chorong.group);
  chorong.sayFemale();
}

class Idol {
  String name;
  String group;
  
  Idol({
    String name,
    String group,
  }) : this.name = name,
       this.group = group;
  
  void sayName(){
    print('저는 ${this.name} 입니다.');
  }
  
  void sayGroup(){
    print('저는 ${this.group} 소속 입니다.');
  }
}

// extends - 상속 할때 사용
// extends 오른쪽이 부모, 왼쪽이 자식

class BoyGroup extends Idol{
  BoyGroup(
    String name,
    String group,
  ) : super(
    name: name,
    group: group,
  );
  
  void sayMale(){
    print('저는 남자아이돌입니다.');
  }
}

class GirlGroup extends Idol{
  GirlGroup(
    String name,
    String group,
  ) : super(
    name: name,
    group: group,
  );
  
  void sayFemale(){
    print('저는 여자아이돌입니다.');
  }
}

20강 Class #4 Method Overriding 
void main(){
  // Method Overriding
  // Method 덮어쓰기
  Parent parent = new Parent(3);
  Child child = new Child(4);
  
  print(parent.calculate());
  print(child.calculate());
}

class Parent {
  final int number;
  
  Parent(
    int number,
  ) : this.number = number;
  
  // Function 함수
  // =Method
  int calculate(){
    return this.number * this.number;
  }
}

class Child extends Parent {
  Child(
    int number,
  ) : super(
    number,
  );
  
  // decorator
  @override
  int calculate(){
    int result = super.calculate();
    
    return result + result;
  }
}

21강 Class #5 Class Static Keyword
void main(){
  Employee seulgi = new Employee('슬기');
  Employee chorong = new Employee('초롱');
  
  seulgi.printNameAndBuilding();
  chorong.printNameAndBuilding();
  
  Employee.building = '거제도';
  
  seulgi.printNameAndBuilding();
  chorong.printNameAndBuilding();
  
  Employee.building = '을지로 위워크';
  
  seulgi.printNameAndBuilding();
  chorong.printNameAndBuilding();
}

// Static Keyword 

// 직원
// 근무하고있는 건물 - 모든 직원들이 다 같음
// 직원의 이름 - 사람마다 다 다름
class Employee {
  static String building;
  String name;
  
  Employee(
    String name,
  ) : this.name = name;
  
  void printNameAndBuilding(){
    print('제 이름은 ${this.name}입니다. ${building} 건물에서 근무하고 있습니다.');
  }
}

22강 Class #6 super와 this
void main(){
  Engineer codeFactory = new Engineer(
    languages: ['dart', 'Java', 'Python'],
    name: '코드팩토리',
    building: '여의도 위워크',
  );
  
  print(codeFactory.name);
  print(codeFactory.building);
  print(codeFactory.languages);
  codeFactory.sayInfo();
}

// 직원
class Employee {
  final String building;
  final String name;
  
  Employee(
    String building,
    String name,
  ) : this.building = building,
      this.name = name;
}

// 엔지니어
// 사용할 줄 아는 언어 - 리스트로
class Engineer extends Employee {
  List<String> languages;

  Engineer({
    List<String> languages,
    String name,
    String building,
  }) : this.languages = languages,
  super(
    building,
    name,
  );
  
  void sayInfo(){
    print('저의 이름은 ${super.name}입니다.');
    print('제가 근무하는 건물은 ${this.building}입니다.'); // 자식에 building을 선언하지 않으면 super를 this로 받을 수 있음.
    print('제가 사용할 수 있는 언어들은 ${this.languages.join(', ')}');
  }
}

23강 Class #7 Interface
void main(){
  BoyGroup bts = new BoyGroup('BTS');
  bts.sayName();
  
  GirlGroup redVelvet = new GirlGroup('레드벨벳');
  redVelvet.sayName();
}

// Interface
class Idol {
  final String name;
  
  Idol(
    String name,
  ) : this.name = name;
  
  void sayName(){
    
  }
  
}

class IdolInterface{
  String name;
  
  void sayName(){}
}

class BoyGroup implements IdolInterface{
  String name;
  
  BoyGroup(
    String name,
  ) : this.name = name;
  
  void sayName(){
    print('제 이름은 ${this.name}입니다. ');
  }
}

class GirlGroup implements IdolInterface{
  String name;
  
  GirlGroup(
    String name,
  ) : this.name = name;
  
  void sayName(){
    print('제 이름은 ${this.name}입니다. ');
  }
}

24강 Class #8 Cascade Operator
void main(){
  Idol idol = new Idol('슬기', '레드벨벳');
  
  idol.sayName();
  idol.sayGroup();
  
  new Idol('슬기', '레드벨벳')
    ..sayName()
    ..sayGroup();
}

//
class Idol {
  String name;
  String group;
  
  Idol(
    String name,
    String group,
  ) : this.name = name,
      this.group = group;
  
  void sayName(){
    print('제 이름은 ${this.name} 입니다.');
  }
  
  void sayGroup(){
    print('저는 ${this.group} 소속입니다.');
  }
}

25강 List 심화(forEach, map, reduce, fold)
void main(){
  // Looping
  // Mapping
  // Reduce/Fold
  
  List<String> redVelvet = [
    '아이린',
    '슬기',
    '웬디',
    '조이',
    '예리'
  ];
  
  // Looping
  redVelvet.forEach((value){
    print(value);
  });
  
  for(String value in redVelvet){
    print(value);
  }
  
  // Mapping - map
  final newList = redVelvet.map((value){
    return '제 이름은 $value입니다.';
  });
  
  print(newList); // Iterable 리스트의 상위?
  print(newList.toList());
  
  // Reduce/Fold 
  List<int> numbers = [
    0,
    1,
    2,
    3,
    4,
    5,
  ];
  
  int total = numbers.fold(0, (total, element){ // 0(설정값)을 토탈에 넣고 시작.
    return total + element;
  });
  
  print(total);
  
  int total2 = numbers.reduce((total, element){ // 첫값을 토탈에 넣고 시작.
    return total + element;
  });
  
  print(total2);
  
  List<String> names = [
    '코드팩토리',
    '레드벨벳',
    'BTS',
  ];
  
  int total3 = names.fold(0, (total, element){
    return total + element.length;
  });
  
  print(total3);
  
//   final total4 = names.reduce((total, element){
//     return total + element.length;
//   });
  
//   print(total4);

//   List의 타입과 return의 타입이 같아야 reduce를 사용가능! 아니라면 fold 사용가능
  
  int total5 = numbers.reduce((total, element) => total + element);
  
  print(total5);
}

26강 Map 심화
void main(){
  Map map = {
    'Apple': '사과',
    'Banana': '바나나',
    'Kiwi': '키위',
  };
  
  print(map.keys.toList());
  print(map.values.toList());
  
  //Mapping - map => (entry)
  final newMap = map.entries.map((entry){
    final key = entry.key;
    final value = entry.value;
    
    return '$key 는 한글로 $value 입니다.';
  });
  
  print(newMap);
  
  //ForEach
  map.entries.forEach((entry){
    final key = entry.key;
    final value = entry.value;
    
    print('$key 는 한글로 $value 입니다.');
  });
  
  //Fold
  final total = map.entries.fold(0, (total,entry){
    return total + entry.key.length;
  });
  
  print(total);
  
  List<int> numbers = [
    10,
    20,
    30,
    40,
    50,
  ];
  
  final newMap2 = numbers.map((item){
    return '값이 $item 입니다.';
  });
  
  print(newMap2);
  
  //List에 키, 값 페어 부여
//   final newMap3 = numbers.asMap();
  final newMap3 = numbers.asMap().entries.map((entry){
    final index = entry.key;
    final value = entry.value;
    
    return 'index가 $index 일 때 값은 $value 입니다.';
  });
  
  print(newMap3.toList());
}