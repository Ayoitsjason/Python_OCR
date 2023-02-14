from ..utils.tesseract import imageOCR
import pytest

@pytest.mark.benchmark
def test_benchmark_jpg_tiny(benchmark):
    def test_str():
        text = None
        with open('payroll/tests/imgs/img_tiny.jpg', 'rb') as file:
            text = imageOCR(file, "Block Text")
        return text
    text = benchmark(test_str)
    assert isinstance(text, str) == True

@pytest.mark.benchmark
def test_benchmark_jpg_small(benchmark):
    def test_str():
        text = None
        with open('payroll/tests/imgs/img_small.jpg', 'rb') as file:
            text = imageOCR(file, "Block Text")
        return text
    text = benchmark(test_str)
    assert isinstance(text, str) == True

@pytest.mark.benchmark
def test_benchmark_jpg_medium(benchmark):
    def test_str():
        text = None
        with open('payroll/tests/imgs/img_medium.jpg', 'rb') as file:
            text = imageOCR(file, "Block Text")
        return text
    text = benchmark(test_str)
    assert isinstance(text, str) == True

@pytest.mark.benchmark
def test_benchmark_jpg_large(benchmark):
    def test_str():
        text = None
        with open('payroll/tests/imgs/img_large.jpg', 'rb') as file:
            text = imageOCR(file, "Block Text")
        return text
    text = benchmark(test_str)
    assert isinstance(text, str) == True
