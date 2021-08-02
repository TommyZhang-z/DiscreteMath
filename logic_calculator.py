class MyInt(int):
    def implies(self, q):
        """
        单向导致 p -> q
        :param q:
        :return:逻辑判断结果
        """
        return MyInt(not self or q)


def zeros(num):
    return [MyInt(0) for _ in range(num)]


def ones(num):
    return [MyInt(1) for _ in range(num)]


def tautology(T_list):
    """
    结果全为True
    :param T_list:
    :return: bool
    """
    return all(T_list)


def material_equivalence(p, q):
    """
    双向导致 p <-> q
    :param p:
    :param q:
    :return:逻辑判断结果
    """
    return MyInt(not (p ^ q))


def array(list_):
    return [MyInt(num) for num in list_]


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
