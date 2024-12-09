def create_task(title, description):
    """Создает новую задачу и добавляет ее в список задач."""
    task = {
        'title': title,
        'description': description
    }
    tasks.append(task)
    # Логика создания задачи
    print(f"Создана новая задача: {title}")
