import time

class AdaptiveCore:
    def __init__(self, core_id):
        self.core_id = core_id
        # Диодная матрица ответов (эмуляционный слой)
        # Ключ: (вход_А, вход_Б), Значение: готовый_ответ
        self.diode_matrix = {}
        
        # Статистика для демонстрации эффективности
        self.transistor_computations = 0
        self.diode_emulations = 0

    def compute_via_transistors(self, a, b):
        """Эмуляция работы транзисторов.
        Реальный просчет логики, который требует времени и энергии."""
        self.transistor_computations += 1
        # Имитируем задержку на прохождение тока по каскаду транзисторов
        time.sleep(0.001) 
        return a ^ b  # Операция XOR

    def execute(self, a, b):
        """Главный интерфейс ядра"""
        input_pair = (a, b)
        
        # Шаг 1: Проверяем диодную матрицу (Есть ли готовый путь для тока?)
        if input_pair in self.diode_matrix:
            self.diode_emulations += 1
            # Ток просто прошел через диод — задержка нулевая!
            return self.diode_matrix[input_pair]
        
        # Шаг 2: Если диоды не настроены, работают транзисторы
        result = self.compute_via_transistors(a, b)
        
        # Шаг 3: "Зашиваем" результат в диодную матрицу (Транзистор контролирует диод)
        self.diode_matrix[input_pair] = result
        return result

    def get_stats(self):
        total = self.transistor_computations + self.diode_emulations
        efficiency = (self.diode_emulations / total * 100) if total > 0 else 0
        return {
            "Core ID": self.core_id,
            "Размер матрицы (диодов)": len(self.diode_matrix),
            "Просчетов транзисторами": self.transistor_computations,
            "Эмуляций через диоды": self.diode_emulations,
            "Эффективность (КПД матрицы)": f"{efficiency:.1f}%"
        }

# --- ДЕМОНСТРАЦИЯ РАБОТЫ ЧИПА ---

# Создаем твое адаптивное ядро
core = AdaptiveCore(core_id=1)

# Имитируем поток задач (повторяющиеся вычисления)
stream_of_tasks = [
    (3, 5), (2, 2), (3, 5), (7, 1), (2, 2), 
    (3, 5), (3, 5), (7, 1), (0, 4), (2, 2)
]

print("=== Запуск потока вычислений ===")
start_time = time.time()

for i, (a, b) in enumerate(stream_of_tasks, 1):
    res = core.execute(a, b)
    print(f"Задача {i}: XOR({a}, {b}) -> Ответ: {res}")

end_time = time.time()
print("================================")
print(f"Время выполнения всего потока: {end_time - start_time:.4f} сек\n")

# Смотрим статистику "кремния"
for key, value in core.get_stats().items():
    print(f"{key}: {value}")
    
