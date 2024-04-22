from src.dto import Operation
from src.utils import get_operations, filter_operation_by_state, sort_operations_by_date


def main(filename='operations.json'):
    operations = get_operations(filename)
    operations = filter_operation_by_state(*operations, state='EXECUTED')
    operations = sort_operations_by_date(*operations)

    for op in operations[:5]:
        print(op.safe())
        print()


if __name__ == '__main__':
    main()
