# Refresh-Python: AQA FastTrack

Учебный репозиторий по автоматизации тестирования на Python + Pytest.

## 🚀 Быстрый старт

### 1. Клонирование репозитория
```powershell
git clone https://github.com/Maxos11/aqa-python-fasttrack.git
cd aqa-python-fasttrack
```

### 2. Создание и активация виртуального окружения
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Установка зависимостей
```powershell
pip install -r requirements.txt
```

### 4. Запуск всех автотестов
```powershell
pytest -v
```

### 5. Запуск только smoke-тестов (по маркеру)
```powershell
pytest -m smoke -v
```