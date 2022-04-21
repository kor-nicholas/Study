

/*

// - поиск с самого начала
.// - поиск с того места, откуда делается поиск
* - все теги

//span[text()='текст, что нужно найти'] - поиск по тегу и тексту на всей старнице
//*[text()='текст поиска'] - поиск по всем тегам и по тексту
//a[@class='имя класса'] - поиск по тегу a и по классу
//*[@href='/attribute'] - поиск по атрибуту и всем тегам
//span[contains(text(), 'кусок текста, по которому можно искать')] - contains юзается чтобы найти элемент, в котором есть какая-то часть
//span[starts-with(text(), 'кусочек')] - все что начинается с 'кусочек'
//span[@class='class_name']/preceding-sibling::span - находит соседский элемент, который находится выше (нашел верхний span, над найденным элементом)
//span[@class='class_name']/following-sibling::span - находит соседский элемент, который находится ниже (нашел нижний span, под найденным элементом)
//span[@class='class_name']/parent::a - найти родителя (тег a) ↑
//span[@class='class_name']/ancestor::a - найти родителя/дедушку/прадедушку/... (тег a, можно выбирать любой тег) ↑
//span[@class='class_name']/child::a - найти дочерний элемент (тег a) ↓
//span[@class='class_name']/descendant::a - найти сына/внука/... (тег a) ↓


*/

 