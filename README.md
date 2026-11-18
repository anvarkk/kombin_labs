ЛАБОРАТОРНАЯ РАБОТА № 4
```Python
from collections import deque

# ── Дано: списки предпочтений (слева — самый желанный кандидат) ──
men = {
    'Андрей': ['Ирина', 'Зина', 'Жанна', 'Елена'],
    'Борис':  ['Зина', 'Жанна', 'Елена', 'Ирина'],
    'Вова':   ['Жанна', 'Елена', 'Зина', 'Ирина'],
    'Гоша':   ['Жанна', 'Зина', 'Ирина', 'Елена'],
    'Денис':  ['Елена', 'Жанна', 'Ирина', 'Зина'],
}
women = {
    'Елена': ['Гоша', 'Борис', 'Вова', 'Андрей', 'Денис'],
    'Жанна': ['Борис', 'Денис', 'Гоша', 'Вова', 'Андрей'],
    'Зина':  ['Вова', 'Денис', 'Борис', 'Андрей', 'Гоша'],
    'Ирина': ['Гоша', 'Андрей', 'Денис', 'Борис', 'Вова'],
}

# Ранги для проверки «лучше или хуже»: rank[w][m] = место m в списке w (меньше = лучше)
rank = {w: {m: i for i, m in enumerate(lst)} for w, lst in women.items()}

husband = {w: None for w in women}  # матрица браков: жена -> муж (None = свободна)
wife    = {m: None for m in men}    # муж -> жена (None = холост) — индексы состояния из лекции
nxt     = {m: 0 for m in men}       # указатель «вычёркивания»: левее него все уже получили предложение
free    = deque(men)                # очередь свободных мужчин
step = 0

while free:
    m = free.popleft()
    if nxt[m] == len(men[m]):       # список исчерпан -> остаётся холостым
        print(f"    {m}: список исчерпан, остаётся холостым")
        continue
    w = men[m][nxt[m]]              # Шаг 1: предложение лучшей из оставшихся
    nxt[m] += 1                     # сделал предложение = вычеркнул её из списка
    step += 1
    cur = husband[w]
    if cur is None:                 # незамужняя соглашается на любое первое предложение
        husband[w], wife[m] = m, w
        print(f"{step:2}. {m} -> {w}: СОГЛАСИЕ")
    elif rank[w][m] < rank[w][cur]: # Шаг 2: кандидат лучше мужа -> развод + новый брак
        wife[cur] = None
        free.append(cur)            # разведённый возвращается в очередь свободных
        husband[w], wife[m] = m, w
        print(f"{step:2}. {m} -> {w}: РАЗВОД с {cur}, брак {m}+{w}")
    else:                           # кандидат хуже мужа -> отказ
        free.append(m)              # Шаг 3: предложит следующей из списка
        print(f"{step:2}. {m} -> {w}: ОТКАЗ (муж {cur} лучше)")

print("\nИтоговые пары:")
for w, m in husband.items():
    print(f"  {m} + {w}")
print("Холостые:", [m for m in men if wife[m] is None])

# ── Проверка стабильности: поиск «пары-разлучницы» (m', w') ──
mrank = {m: {w: i for i, w in enumerate(lst)} for m, lst in men.items()}
blocking = []
for m in men:
    for w in women:
        if wife[m] == w:
            continue
        m_wants = wife[m] is None or mrank[m][w] < mrank[m][wife[m]]  # m хочет w больше жены (или холост)
        w_wants = rank[w][m] < rank[w][husband[w]]                    # w хочет m больше мужа
        if m_wants and w_wants:
            blocking.append((m, w))
print("Пары нестабильности:", blocking if blocking else "нет — бракосочетание СТАБИЛЬНО")
```
