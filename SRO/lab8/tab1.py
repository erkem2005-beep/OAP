
# ============================================================
# COURSE ADVISOR
# Система помощи при выборе IT-направления
# Университетский проект
# ============================================================

CATEGORIES = {
    "python": {
        "name": "Python-разработка",
        "description": (
            "Тебе может подойти создание программ, "
            "автоматизация задач и разработка логики приложений."
        ),
        "course": "Основы Python и алгоритмов"
    },
    "web": {
        "name": "Веб-разработка",
        "description": (
            "Тебе может понравиться создание сайтов, "
            "веб-приложений и интерактивных интерфейсов."
        ),
        "course": "HTML, CSS и JavaScript"
    },
    "data": {
        "name": "Анализ данных",
        "description": (
            "Тебе может подойти исследование данных, "
            "работа с таблицами и поиск закономерностей."
        ),
        "course": "Python, SQL и основы анализа данных"
    },
    "security": {
        "name": "Кибербезопасность",
        "description": (
            "Тебе может быть интересно изучение уязвимостей, "
            "защита информации и анализ угроз."
        ),
        "course": "Основы сетей и кибербезопасности"
    },
    "design": {
        "name": "UI/UX-дизайн",
        "description": (
            "Тебе может подойти проектирование удобных "
            "интерфейсов и визуальной структуры приложений."
        ),
        "course": "Основы UI/UX и Figma"
    }
}


def create_scores():
    """Создаёт отдельный счётчик баллов для каждого направления."""
    return {key: 0 for key in CATEGORIES}


def ask_choice(question, options):
    """Задаёт вопрос с выбором одного варианта."""
    print(f"\n{question}")

    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    while True:
        answer = input("Твой ответ: ").strip()

        if answer.isdigit():
            number = int(answer)

            if 1 <= number <= len(options):
                return number - 1

        print(f"Введите число от 1 до {len(options)}.")


def ask_scale(question):
    """Задаёт вопрос по шкале от 1 до 5."""
    print(f"\n{question}")
    print("1 — совсем не нравится")
    print("2 — скорее не нравится")
    print("3 — нейтрально")
    print("4 — нравится")
    print("5 — очень нравится")

    while True:
        answer = input("Оцени от 1 до 5: ").strip()

        if answer.isdigit() and 1 <= int(answer) <= 5:
            return int(answer)

        print("Ошибка: необходимо ввести число от 1 до 5.")


def ask_multiple(question, options, min_choices=1, max_choices=2):
    """Позволяет выбрать несколько интересов."""
    print(f"\n{question}")

    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    print(
        f"Выбери от {min_choices} до {max_choices} вариантов."
    )
    print("Введи номера через запятую, например: 1,3")

    while True:
        answer = input("Твои варианты: ").strip()

        try:
            numbers = [
                int(item.strip())
                for item in answer.split(",")
            ]

            if (
                len(numbers) != len(set(numbers))
                or not min_choices <= len(numbers) <= max_choices
                or any(
                    number < 1 or number > len(options)
                    for number in numbers
                )
            ):
                raise ValueError

            return [number - 1 for number in numbers]

        except ValueError:
            print(
                "Некорректный ввод. Проверь номера "
                "и количество выбранных вариантов."
            )


def add_points(scores, points):
    """Начисляет баллы по результатам ответа."""
    for category, value in points.items():
        scores[category] += value


def run_test():
    """Проводит тест и возвращает итоговые баллы."""
    scores = create_scores()

    print("=" * 58)
    print("       COURSE ADVISOR — ПОМОЩНИК ПО ВЫБОРУ КУРСОВ")
    print("=" * 58)
    print(
        "\nОтветь на пять вопросов, чтобы получить "
        "рекомендацию по IT-направлению."
    )

    # ВОПРОС 1. Выбор одного интереса
    options_1 = [
        "Создавать программы и автоматизировать задачи",
        "Создавать сайты и красивые веб-страницы",
        "Работать с цифрами и находить закономерности",
        "Защищать системы и искать уязвимости",
        "Продумывать внешний вид и удобство приложений"
    ]

    points_1 = [
        {"python": 3, "web": 1, "data": 2,
         "security": 2, "design": 0},
        {"python": 1, "web": 3, "data": 0,
         "security": 0, "design": 2},
        {"python": 2, "web": 0, "data": 3,
         "security": 1, "design": 0},
        {"python": 1, "web": 0, "data": 1,
         "security": 3, "design": 0},
        {"python": 0, "web": 2, "data": 0,
         "security": 0, "design": 3}
    ]

    answer = ask_choice(
        "1. Какое занятие тебе наиболее интересно?",
        options_1
    )
    add_points(scores, points_1[answer])

    # ВОПРОС 2. Оценка по шкале
    rating = ask_scale(
        "2. Насколько тебе нравится решать логические задачи?"
    )

    # Более высокая оценка увеличивает баллы направлений,
    # где логическое мышление особенно полезно.
    logic_bonus = rating - 1

    add_points(scores, {
        "python": logic_bonus,
        "web": logic_bonus // 2,
        "data": logic_bonus,
        "security": logic_bonus,
        "design": 0
    })

    # ВОПРОС 3. Выбор нескольких интересов
    options_3 = [
        "Написание кода",
        "Создание сайтов",
        "Анализ информации",
        "Поиск ошибок и защита систем",
        "Дизайн и удобство интерфейсов"
    ]

    categories_3 = [
        "python", "web", "data", "security", "design"
    ]

    selected = ask_multiple(
        "3. Какие задачи ты хотел бы попробовать?",
        options_3
    )

    for index in selected:
        scores[categories_3[index]] += 2

    # ВОПРОС 4. Ситуационная задача
    options_4 = [
        "Написать скрипт, который решит задачу автоматически",
        "Сделать удобный сайт для пользователей",
        "Изучить данные и найти причину проблемы",
        "Проверить систему на уязвимости",
        "Улучшить внешний вид и структуру интерфейса"
    ]

    points_4 = [
        {"python": 3, "web": 1, "data": 2,
         "security": 1, "design": 0},
        {"python": 0, "web": 3, "data": 0,
         "security": 0, "design": 2},
        {"python": 1, "web": 0, "data": 3,
         "security": 1, "design": 0},
        {"python": 1, "web": 0, "data": 1,
         "security": 3, "design": 0},
        {"python": 0, "web": 2, "data": 0,
         "security": 0, "design": 3}
    ]

    answer = ask_choice(
        "4. Представь, что тебе дали IT-проект. "
        "С чего ты начнёшь?",
        options_4
    )
    add_points(scores, points_4[answer])

    # ВОПРОС 5. Цель обучения
    options_5 = [
        "Научиться создавать программы",
        "Научиться разрабатывать сайты",
        "Научиться анализировать данные",
        "Научиться защищать информацию",
        "Научиться проектировать интерфейсы"
    ]

    points_5 = [
        {"python": 3, "web": 1, "data": 1,
         "security": 1, "design": 0},
        {"python": 0, "web": 3, "data": 0,
         "security": 0, "design": 1},
        {"python": 1, "web": 0, "data": 3,
         "security": 1, "design": 0},
        {"python": 1, "web": 0, "data": 1,
         "security": 3, "design": 0},
        {"python": 0, "web": 1, "data": 0,
         "security": 0, "design": 3}
    ]

    answer = ask_choice(
        "5. Какой навык ты больше всего хочешь получить?",
        options_5
    )
    add_points(scores, points_5[answer])

    return scores


def show_results(scores):
    """Сравнивает результаты и формирует рекомендации."""
    ranking = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    best_key, best_score = ranking[0]
    second_key, second_score = ranking[1]

    print("\n" + "=" * 58)
    print("                 РЕЗУЛЬТАТЫ ТЕСТА")
    print("=" * 58)

    print("\nБаллы по направлениям:")

    for key, score in ranking:
        name = CATEGORIES[key]["name"]
        bar = "#" * score
        print(f"{name:<25} {score:>2} балла  {bar}")

    print("\nОсновная рекомендация:")
    print(CATEGORIES[best_key]["name"])
    print(CATEGORIES[best_key]["description"])
    print(
        "Рекомендуемый курс: "
        + CATEGORIES[best_key]["course"]
    )

    print("\nАльтернативное направление:")
    print(CATEGORIES[second_key]["name"])

    difference = best_score - second_score

    if difference == 0:
        print(
            "Результат неоднозначен: два направления "
            "набрали одинаковое количество баллов. "
            "Попробуй вводный курс по каждому."
        )
    elif difference <= 2:
        print(
            "Результаты близки. Рассмотри оба направления "
            "и сравни вводные курсы."
        )
    else:
        print(
            "Первое направление набрало заметно больше "
            "баллов и является основной рекомендацией."
        )

    print("\nВажно: тест помогает выбрать направление, "
          "но не заменяет практический опыт.")

    print("=" * 58)


def main():
    """Главная функция программы."""
    while True:
        scores = run_test()
        show_results(scores)

        again = input(
            "\nПройти тест ещё раз? (да/нет): "
        ).strip().lower()

        if again not in ("да", "д", "yes", "y"):
            print("\nСпасибо за использование Course Advisor!")
            break


if __name__ == "__main__":
    main()
