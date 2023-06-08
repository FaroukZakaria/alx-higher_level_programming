#!/usr/bin/python3
import importlib.util


def main():
    spec = importlib.util.spec_from_file_location("hidden_4", "hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    names = [name for name in dir(module) if not name.startswith('_')]
    for name in names:
        print(name)


if __name__ == '__main__':
    main()
