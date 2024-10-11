document.addEventListener('DOMContentLoaded', function() {
    // Динамическое обновление доступных классов в зависимости от расы

    const raceField = document.getElementById('id_race');
    const classField = document.getElementById('id_character_class');

    const classOptions = {
        'Человек': ['Воин', 'Маг', 'Вор'],
        'Эльф': ['Лучник', 'Маг'],
        'Гном': ['Воин', 'Жрец']
    };

    raceField.addEventListener('change', function() {
        const selectedRace = raceField.value;
        const classes = classOptions[selectedRace] || [];
        classField.innerHTML = '';

        classes.forEach(function(cls) {
            const option = document.createElement('option');
            option.value = cls;
            option.textContent = cls;
            classField.appendChild(option);
        });
    });

    form.addEventListener('submit', function(event) {
        // Проверка уровня персонажа
        const levelField = document.getElementById('id_level');
        if (levelField.value < 1 || levelField.value > 20) {
            alert('Уровень персонажа должен быть от 1 до 20.');
            event.preventDefault();
            return false;
        }

    });

    document.addEventListener('DOMContentLoaded', function() {
        const attributes = ['id_strength', 'id_dexterity', 'id_constitution', 'id_intelligence', 'id_wisdom', 'id_charisma'];
        const totalPoints = 60;  // Общее количество очков для распределения
        let form = document.getElementById('character-form');
    
        function updatePoints() {
            let sum = 0;
            attributes.forEach(function(attr) {
                let value = parseInt(document.getElementById(attr).value) || 0;
                sum += value;
            });
            let remaining = totalPoints - sum;
            document.getElementById('points-remaining').textContent = remaining;
            if (remaining < 0) {
                document.getElementById('points-remaining').classList.add('text-danger');
            } else {
                document.getElementById('points-remaining').classList.remove('text-danger');
            }
        }
    
        attributes.forEach(function(attr) {
            document.getElementById(attr).addEventListener('input', updatePoints);
        });
    
        updatePoints();
    
        form.addEventListener('submit', function(event) {
            let remaining = parseInt(document.getElementById('points-remaining').textContent);
            if (remaining < 0) {
                alert('Вы превысили допустимое количество очков для распределения атрибутов.');
                event.preventDefault();
            }
        });
    });

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        // Сбор данных формы
        const formData = new FormData(form);
    
        fetch("{% url 'create_character' %}", {
            method: 'POST',
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
            },
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = "{% url 'character_list' %}";
            } else {
                // Отобразить ошибки
                alert('Ошибка при создании персонажа.');
            }
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
    });

});