from functools import reduce
from collections import defaultdict
from typing import Callable, Iterable, List, Any, Dict, Sequence

def zipmap(key_list: Sequence[Any], value_list: Sequence[Any], override: bool = False) -> Dict[Any, Any]:
    if not override and len(set(key_list)) != len(key_list):
        return {}

    def pair(i_k: tuple[int, Any]):
        i, k = i_k
        return k, (value_list[i] if i < len(value_list) else None)

    pairs = map(pair, enumerate(key_list))  

    if override:
        return dict(pairs) 
    else:
        result: Dict[Any, Any] = {}
        for k, v in pairs: 
            result[k] = v
        return result


def group_by(f: Callable[[Any], Any], target_list: Iterable[Any]) -> Dict[Any, List[Any]]:
    grouped: Dict[Any, List[Any]] = defaultdict(list)
    for item in target_list:
        grouped[f(item)].append(item)
    return dict(grouped)


def my_filter(predicate: Callable[[Any], bool], seq: Iterable[Any]) -> List[Any]:
    return reduce(lambda acc, x: acc + [x] if predicate(x) else acc, seq, [])

def _run_tests() -> None:
    # Task 1 examples
    assert zipmap(["a", "b", "c", "d", "e", "f"], [1, 2, 3, 4, 5, 6]) == {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
    assert zipmap([1, 2, 3, 2], [4, 5, 6, 7], True) == {1: 4, 2: 7, 3: 6}
    assert zipmap([1, 2, 3], [4, 5, 6, 7, 8]) == {1: 4, 2: 5, 3: 6}
    assert zipmap([1, 3, 5, 7], [2, 4, 6]) == {1: 2, 3: 4, 5: 6, 7: None}

    # Task 2 example
    assert group_by(len, ["hi", "dog", "me", "bad", "good"]) == {2: ["hi", "me"], 3: ["dog", "bad"], 4: ["good"]}

    # Task 3 quick check
    assert my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == [2, 4]

if __name__ == "__main__":
    _run_tests()
    print("All tests passed ✨")
