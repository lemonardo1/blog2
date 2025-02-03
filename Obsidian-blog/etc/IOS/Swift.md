Swift는 Apple의 생태계(iOS, macOS, watchOS, tvOS 등)를 위한 강력하고 직관적인 프로그래밍 언어입니다. Swift는 안전성, 속도, 모던한 문법을 강조하며 개발자가 효율적으로 코드를 작성할 수 있도록 돕습니다. 아래에서는 Swift의 주요 특징과 중요한 문법 요소들을 예제와 함께 자세히 설명합니다.

---

## 1. Swift의 특징

- **안전성**: Swift는 변수의 사용 전 초기화, 옵셔널 타입, 메모리 관리를 통해 런타임 에러를 최소화합니다.
- **모던한 문법**: 간결하고 직관적인 문법 덕분에 가독성이 높고, 코드 유지보수가 용이합니다.
- **고성능**: 컴파일러 최적화를 통해 높은 성능을 제공하며, Objective-C와의 호환성도 지원합니다.
- **함수형 프로그래밍 지원**: 클로저, 고차함수(map, filter, reduce 등)를 활용하여 선언적 프로그래밍이 가능합니다.

---

## 2. 변수와 상수

Swift에서는 `var`를 사용해 변수(값이 변경될 수 있음)를, `let`을 사용해 상수(값이 변경되지 않음)를 선언합니다.

```swift
// 변수 선언
var greeting = "Hello"
greeting = "Hi"

// 상수 선언
let pi = 3.14159
// pi = 3.14  // 컴파일 에러 발생: 상수는 변경할 수 없습니다.
```

---

## 3. 데이터 타입과 타입 추론

Swift는 정적 타입 언어이지만, 타입 추론 기능이 있어 선언 시 타입을 명시하지 않아도 초기값을 기반으로 타입을 결정합니다.

```swift
var integerNumber = 42         // Int 타입
var doubleNumber = 3.14        // Double 타입
var isSwiftFun = true          // Bool 타입
var greetingMessage = "Hello"  // String 타입
```

또한, 명시적으로 타입을 지정할 수도 있습니다.

```swift
var explicitInteger: Int = 100
var explicitDouble: Double = 99.99
```

---

## 4. 제어문

### 조건문 (if, switch)

Swift의 조건문은 C 계열 언어와 유사하지만, 조건문에 반드시 불리언(Boolean) 값이 와야 합니다.

```swift
let score = 85

if score >= 90 {
    print("A 학점")
} else if score >= 80 {
    print("B 학점")
} else {
    print("C 학점 이하")
}
```

`switch` 문은 각 케이스가 반드시 완전성을 갖추어야 하며, `default` 케이스를 통해 모든 경우를 처리할 수 있습니다.

```swift
let fruit = "Apple"

switch fruit {
case "Apple":
    print("사과입니다.")
case "Banana":
    print("바나나입니다.")
default:
    print("알 수 없는 과일입니다.")
}
```

### 반복문 (for-in, while)

`for-in` 반복문은 시퀀스(sequence)를 순회할 때 주로 사용합니다.

```swift
for number in 1...5 {
    print(number)
}
```

`while` 문은 조건이 참일 때 반복 실행합니다.

```swift
var count = 0
while count < 5 {
    print("현재 count: \(count)")
    count += 1
}
```

---

## 5. 함수

Swift에서 함수는 `func` 키워드를 사용하여 정의합니다. 함수는 매개변수와 반환값을 가질 수 있습니다.

```swift
func greet(name: String) -> String {
    return "안녕하세요, \(name)님!"
}

let message = greet(name: "Swift")
print(message)
```

매개변수에 기본 값을 지정할 수도 있습니다.

```swift
func multiply(_ a: Int, by b: Int = 2) -> Int {
    return a * b
}

print(multiply(3))      // 3 * 2 = 6
print(multiply(3, by: 4)) // 3 * 4 = 12
```

---

## 6. 클로저 (Closures)

클로저는 코드 블록을 캡슐화한 것으로, 변수에 할당하거나 함수의 인자로 전달할 수 있습니다. 대표적인 예로 고차함수인 `map`, `filter`, `reduce`가 있습니다.

```swift
let numbers = [1, 2, 3, 4, 5]

// 클로저를 사용하여 각 숫자에 2를 곱함
let doubled = numbers.map { (number: Int) -> Int in
    return number * 2
}
print(doubled) // [2, 4, 6, 8, 10]

// 더 간결하게 표현 가능
let doubledConcise = numbers.map { $0 * 2 }
print(doubledConcise)
```

---

## 7. 클래스와 구조체

Swift에서는 객체 지향 프로그래밍을 위해 `class`와 `struct`를 제공합니다. 클래스는 상속이 가능하지만, 구조체는 값 타입으로 복사됩니다.

### 클래스 예제

```swift
class Person {
    var name: String
    var age: Int

    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }

    func introduce() -> String {
        return "안녕하세요, 제 이름은 \(name)이고, \(age)살입니다."
    }
}

let person = Person(name: "Alice", age: 30)
print(person.introduce())
```

### 구조체 예제

```swift
struct Point {
    var x: Int
    var y: Int

    func display() -> String {
        return "(\(x), \(y))"
    }
}

var point1 = Point(x: 10, y: 20)
var point2 = point1  // 값 복사
point2.x = 30
print(point1.display()) // (10, 20)
print(point2.display()) // (30, 20)
```

---

## 8. 옵셔널 (Optionals)

옵셔널은 값이 없을 수 있음을 나타내며, 변수에 `nil` 값을 허용합니다. 옵셔널 값을 안전하게 다루기 위해 `if let` 구문이나 `guard let` 구문을 사용합니다.

```swift
var optionalString: String? = "Hello, Swift!"
print(optionalString)  // Optional("Hello, Swift!")

// 옵셔널 바인딩을 통한 안전한 값 추출
if let unwrappedString = optionalString {
    print("언래핑된 값: \(unwrappedString)")
} else {
    print("값이 없습니다.")
}

// 옵셔널 강제 언래핑 (값이 nil이 아니라고 확신할 때)
print(optionalString!)  // 주의: nil일 경우 런타임 에러 발생
```

---

## 9. 프로토콜 (Protocols)

프로토콜은 특정 기능을 수행하기 위한 메서드, 속성, 기타 요구사항을 정의합니다. 클래스, 구조체, 열거형 등은 이 프로토콜을 채택하여 구현할 수 있습니다.

```swift
protocol Drivable {
    func drive()
}

class Car: Drivable {
    func drive() {
        print("자동차가 달립니다.")
    }
}

let myCar = Car()
myCar.drive()
```

---

## 10. 에러 처리

Swift에서는 `Error` 프로토콜을 준수하는 타입을 정의하고, `throw`, `try`, `catch` 구문을 통해 에러를 처리할 수 있습니다.

```swift
enum FileError: Error {
    case fileNotFound
    case unreadable
}

func readFile(filename: String) throws -> String {
    if filename != "existingFile.txt" {
        throw FileError.fileNotFound
    }
    return "파일 내용"
}

do {
    let content = try readFile(filename: "nonexistent.txt")
    print(content)
} catch FileError.fileNotFound {
    print("파일을 찾을 수 없습니다.")
} catch {
    print("알 수 없는 에러가 발생했습니다.")
}
```

---

## 11. 제네릭 (Generics)

제네릭을 사용하면 타입에 상관없이 재사용 가능한 코드를 작성할 수 있습니다. 예를 들어, 배열의 요소를 교환하는 함수를 작성해보겠습니다.

```swift
func swapValues<T>(_ a: inout T, _ b: inout T) {
    let temp = a
    a = b
    b = temp
}

var first = 10
var second = 20
swapValues(&first, &second)
print("first: \(first), second: \(second)")  // first: 20, second: 10
```

---

## 결론

Swift는 모던하고 안전한 프로그래밍 언어로, 직관적인 문법과 다양한 기능을 통해 개발자가 효율적으로 앱을 개발할 수 있도록 돕습니다.  
위에서 소개한 변수와 상수, 제어문, 함수, 클로저, 클래스/구조체, 옵셔널, 프로토콜, 에러 처리, 제네릭 등은 Swift의 핵심적인 문법 요소들입니다. 이러한 문법 요소들을 익히면 Swift의 강력한 기능을 활용하여 안정적이고 확장 가능한 애플리케이션을 개발할 수 있습니다.