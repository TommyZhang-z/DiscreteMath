import numpy as np

# defining constants
P = zip(
    np.array([1, 0]),
)

PQ = zip(
    np.array([1, 1, 0, 0]),
    np.array([1, 0, 1, 0])
)

PQR = zip(
    np.array([1, 1, 1, 1, 0, 0, 0, 0]),
    np.array([1, 1, 0, 0, 1, 1, 0, 0]),
    np.array([1, 0, 1, 0, 1, 0, 1, 0])
)

PQRS = zip(
    np.array([1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]),
    np.array([1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]),
    np.array([1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]),
    np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])
)


def imp(p, q) -> bool:
    """
    material implication
    单向导致 p -> q
    :param p:
    :param q:
    :return:逻辑判断结果
    """
    return not p or q


def test(zipVar, func) -> np.ndarray:
    """
    合成函数
    :param zipVar: 变量列表的zip
    :param func: 执行函数
    :return: 逻辑判断结果
    """
    truth_value = []
    for var in zipVar:
        truth_value.append(int(func(*var)))
    result = np.array(truth_value)
    truth_value.clear()
    return result

