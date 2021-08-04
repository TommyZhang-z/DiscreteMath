def imp(p, q):
    """
    material implication
    单向导致 p -> q
    :param p:
    :param q:
    :return:逻辑判断结果
    """
    return not p or q


def test(*args, func) -> list:
    """
    合成函数
    :param args: 变量列表
    :param func: 执行函数
    :return: 逻辑判断结果
    """
    truth_value = []
    for var in zip(*args):
        truth_value.append(int(func(*var)))
    return truth_value
