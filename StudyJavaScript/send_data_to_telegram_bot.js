$(".order_form").submit(function (event) {
    // Отмена стандартного поведения отправки формы
    event.preventDefault();

    var token = '6867839874:AAF3yXWjyedKCs1rXESEAzWmyYV33ACha44';
    var chat_id = '779209330';
    
    // Получение значений полей формы
    var nameValue = $(this).find("input[name='name']").val();
    var phoneValue = $(this).find("input[name='phone']").val();

    // Проверка наличия значения в обоих полях
    if (nameValue.trim() === '' && phoneValue.trim() === '') {
        alert("Введите Ваши имя и телефон");
        $(this).find("input[name='name']").focus();
        return false;
    } else if (nameValue.trim() === '') {
        alert("Введите Ваше имя");
        $(this).find("input[name='name']").focus();
        return false;
    } else if (phoneValue.trim() === '') {
        alert("Введите Ваш телефон");
        $(this).find("input[name='phone']").focus();
        return false;
    } else {
        // Выполнение POST запроса
        $.get("https://api.telegram.org/bot" + token + "/sendMessage?chat_id=" + chat_id + "&text=Имя покупателя: " + nameValue + "%0AТелефон: " + phoneValue)
            .done(function(response) {
                // Обработка успешного ответа
                // alert("Форма успешно отправлена!");
                window.location.href = "success.html";
            })
            .fail(function(xhr, status, error) {
                // Обработка ошибки
                console.error("Ошибка при отправке формы:", error);
            });
    }
});