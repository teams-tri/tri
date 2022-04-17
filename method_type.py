from timer_context_manager import TimerContextManager


def quicksort(tab):
    with TimerContextManager() as t:
        t.run(tab)
    return TimerContextManager.term


def heapsort(tab):
    with TimerContextManager('heapsort') as t:
        t.run(tab)
    return TimerContextManager.term


def mergesort(tab):
    with TimerContextManager('mergesort') as t:
        t.run(tab)
    return TimerContextManager.term


def run_method(tab):
    def _build_data(data, kind):
        return [[len(t) for t in tab], [kind(t) for t in data]]

    merge_sort = _build_data(tab, mergesort)
    heap_sort = _build_data(tab, heapsort)
    quick_sort = _build_data(tab, quicksort)

    return [merge_sort, heap_sort, quick_sort]


if __name__ == "__main__":
    print (run_method([[j for j in range(i)] for i in range(11)]))
