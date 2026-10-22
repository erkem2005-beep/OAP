# Помощник по выбору учебных курсов
# Учебный мини-проект по дисциплине «Основы алгоритмизации и программирования»

courses = [
    {
        "name": "Основы Python",
        "interest": "programming",
        "level": "beginner",
        "hours": 3,
        "description": "Переменные, условия, циклы и функции на Python."
    },
    {
        "name": "Алгоритмы и логика",
        "interest": "programming",
        "level": "beginner",
        "hours": 2,
        "description": "Основы алгоритмов, логическое мышление и решение задач."
    },
    {
        "name": "Веб-разработка",
        "interest": "web",
        "level": "beginner",
        "hours": 4,
        "description": "Создание простых веб-страниц с HTML и CSS."
    },
    {
        "name": "Анализ данных",
        "interest": "data",
        "level": "intermediate",
        "hours": 5,
        "description": "Работа с таблицами и базовый анализ данных."
    },
    {
        "name": "Введение в искусственный интеллект",
        "interest": "ai",
        "level": "intermediate",
        "hours": 4,
        "description": "Обзор ИИ, примеры применения и базовые понятия."
    },
    {
        "name": "Продвинутый Python",
        "interest": "programming",
        "level": "advanced",
        "hours": 6,
        "description": "Более сложные конструкции и организация программ."
    },
    {
        "name": "Основы компьютерной грамотности",
        "interest": "computer",
        "level": "beginner",
        "hours": 1,
        "description": "Базовые навыки работы с компьютером и файлами."
    }
]

INTERESTS = {
    "1": ("programming", "Программирование"),
    "2": ("web", "Веб-разработка"),
    "3": ("data", "Анализ данных"),
    "4": ("ai", "Искусственный интеллект"),
    "5": ("computer", "Компьютерная грамотность"),
}

LEVELS = {
    "1": ("beginner", "Начинающий"),
    "2": ("intermediate", "Средний"),
    "3": ("advanced", "Продвинутый"),
}


def show_menu(title, options):
    """Показывает варианты выбора и возвращает введённый номер."""
    print("\n" + title)
    for number, option in options.items():
        print(number + ". " + option[1])
    while True:
        answer = input("Введите номер: ").strip()
        if answer in options:
            return options[answer][0]
        print("Ошибка: выберите один из предложенных номеров.")


def get_available_hours():
    """Запрашивает доступное время в часах в неделю."""
    while True:
        answer = input("Сколько часов в неделю вы можете учиться (1–40)? ").strip()
        try:
            hours = int(answer)
            if 1 <= hours <= 40:
                return hours
            print("Ошибка: введите число от 1 до 40.")
        except ValueError:
            print("Ошибка: нужно ввести целое число.")


def recommend_courses(interest, level, available_hours, rule_mode):
    """Подбирает курсы по прозрачным правилам и объясняет рекомендации."""
    recommendations = []

    for course in courses:
        score = 0
        reasons = []

        if course["interest"] == interest:
            score += 3
            reasons.append("совпадает с вашим интересом")

        if course["level"] == level:
            score += 2
            reasons.append("соответствует вашему уровню подготовки")

        if course["hours"] <= available_hours:
            score += 1
            reasons.append("укладывается в доступное время")
        else:
            # Во втором режиме курс с большим временем исключается.
            if rule_mode == 2:
                continue

        # Режим 1: курс может быть рекомендован, если набрал хотя бы 3 балла.
        # Режим 2: более строгий отбор — интерес и время обязательны.
        if rule_mode == 1 and score >= 3:
            recommendations.append((score, course, reasons))
        elif rule_mode == 2 and course["interest"] == interest and score >= 4:
            recommendations.append((score, course, reasons))

    recommendations.sort(key=lambda item: item[0], reverse=True)
    return recommendations


def print_recommendations(recommendations):
    """Печатает подобранные курсы и причины рекомендации."""
    if not recommendations:
        print("\nПодходящих курсов по выбранным условиям не найдено.")
        print("Попробуйте увеличить доступное время или изменить профиль.")
        return

    print("\nРекомендуемые курсы:")
    for index, item in enumerate(recommendations, start=1):
        score, course, reasons = item
        print(f"{index}. {course['name']} — {course['hours']} ч./нед., баллы: {score}")
        print("   " + course["description"])
        print("   Причины: " + "; ".join(reasons) + ".")


def main():
    print("=" * 52)
    print("      ПОМОЩНИК ПО ВЫБОРУ УЧЕБНЫХ КУРСОВ")
    print("=" * 52)
    print("Ответьте на вопросы, чтобы получить рекомендации.")

    interest = show_menu("Что вам интересно?", INTERESTS)
    level = show_menu("Какой у вас уровень подготовки?", LEVELS)
    hours = get_available_hours()

    print("\nВыберите режим рекомендаций:")
    print("1. Гибкие правила")
    print("2. Строгие правила")
    while True:
        mode_input = input("Введите 1 или 2: ").strip()
        if mode_input in ("1", "2"):
            mode = int(mode_input)
            break
        print("Ошибка: введите 1 или 2.")

    results = recommend_courses(interest, level, hours, mode)
    print_recommendations(results)
    print("\nПримечание: рекомендации формируются по заданным правилам,")
    print("машинное обучение и внешние библиотеки не используются.")


if __name__ == "__main__":
    main()
