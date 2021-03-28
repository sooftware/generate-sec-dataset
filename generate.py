# MIT License
#
# Copyright (c) 2021 Soohwan Kim
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import random


def _delete_space_randomly(sentence: str, alpha: float = 0.5) -> str:
    new_sentence = str()
    tokens = sentence.split()

    for token in tokens:
        delete_space = True if random.random() < alpha else False

        if delete_space:
            new_sentence += f"{token} "
        else:
            new_sentence += token

    return new_sentence


def _add_space_randomly(sentence: str, alpha: float = 0.1) -> str:
    new_sentence = str()

    for ch in sentence:
        add_space = True if random.random() < alpha else False

        if add_space and ch != ' ':
            new_sentence += f"{ch} "
        else:
            new_sentence += ch

    return new_sentence


def generate_dataset(filepath: str, generate_filepath: str) -> None:
    inputs = list()
    targets = list()

    with open(filepath) as f:
        for target in f.readlines():
            targets.append(target)
            input_ = _delete_space_randomly(target)
            input_ = _add_space_randomly(input_)
            inputs.append(input_)

    with open(generate_filepath, 'w') as f:
        f.write("inputs\ttargets")

        for input_, target in zip(inputs, targets):
            f.write(f"{input_}\t{target}")

    return
