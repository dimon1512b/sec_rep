let newChange;
console.log('Hi, thi is my first change in remote project!');

let change2; // second changes 

console.log('changes third');


// Variables
/*
Як я вже писав - той мінімальний набор він власне мінімальний тільки для junior frontend developer, а для верстальника той набор то перебор. Серед тих пунктів мінімум для верстальника це:
Перший пункт:
- змінні. Як об'явити змінну? Чим відрізняється let, const, var? Які змінні доступні в головній області видимості,
  а які в області видимості функціх? Як отримати значення змінної? Як змінити значення змінної?
- функції. Як об'явити функцію? Як викликати функцію? Як зберегти результат виконання функції до змінної?
  Передати аргументи до функції. Вказати дефоолтні значення до аргументів функції.
- типи данних. string - "example", number - 123, bool - true/folse, array - [1, 2, 3, "4", "five", "six", true, folse],
  object - {"any_key": "any_value", "new_key": 123, "key": true}, null - типу нічого,
  undefined - типу не відомо що взагалі
- головні методи у типів данних: array.push/array.pop, string.toUpperCase/string.toLowerCase
- вміти побудувати умовний блок. Типу
    if (1 > 0) {
        console.log("тут повідомлення в консоль про те що умова виконалася")
    }
    else {
        console.log("Інше повідомлення в консоль якщо виявиться що умова не виконалася")
    }
    В круглих скобках сформувати умову за якої буде виконаний блок if, а якщо умова не буде виконана то відпрацює
    не обов'язковий блок else
- Оператори. Оператор присвоювання значення для змінної, оператори порівняння, оператор рівноті та не рівності
- цикли for and while. В чому різниця. Як створити безкінечний цикл while та зупинити його?
- Важливо знати, що через об'єкт document можна отримати якийсь html елемент та працювати з ним. Наприклад в мене є
  блок якому я присвоїв його унікальний id. <div id='my_id'>Кнопка!!!</div> . То я можу через js отримати цей елемент а разом
  з ним і всю інформацію про нього. І можу зробити з ним що завгодно. Настпним чином:
  let my_btn = document.getElementById('my_id')
  let text_from_my_btn = my_btn.text
  my_btn.text = 'new_text'

  //
  or
  //

  if (some_input.text == 'some text') {
    my_btn.style.color = 'red'
  }
  else {
    my_btn.setAttribute('disable', true)
  }

 */