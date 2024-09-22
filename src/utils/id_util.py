"""
ID工具类

"""
from src.snowflake import options, generator


class IdUtil:
    """
    ID工具类

    """
    option = options.IdGeneratorOptions(worker_id=23, worker_id_bit_length=10, seq_bit_length=10)
    idgen = generator.DefaultIdGenerator()
    idgen.set_id_generator(option)

    @staticmethod
    def get_id() -> int:
        """
        使用雪花算法生成全局唯一id

        :return: id
        """
        return IdUtil.idgen.next_id()
