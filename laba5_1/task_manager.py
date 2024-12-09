def create_task(title, description):
    """Создает новую задачу и добавляет ее в список задач."""
    task = {
        'title': title,
        'description': description
    }
    tasks.append(task)
    # Логика создания задачи
    print(f"Создана новая задача: {title}")
def list_tasks():
    """Выводит все задачи."""
    if not tasks:
        print("Нет доступных задач.")
        return
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['title']}: {task['description']}")

def delete_task(index):
    """Удаляет задачу по индексу."""
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Задача '{removed_task['title']}' удалена.")
    else:
        print("Некорректный индекс задачи.")
