from ..utils.tesseract import imageOCR
import pytest

@pytest.mark.benchmark
def test_benchmark_jpg_small(benchmark):
    def test_str():
        text = None
        with open('payroll/tests/imgs/apple.jpeg', 'rb') as file:
            text = imageOCR(file, "Row Text")
        return text
    text = benchmark(test_str)
    assert isinstance(text, str) == True

@pytest.mark.benchmark
def test_benchmark_png_small(benchmark):
    def test_str():
        text = None
        with open('payroll/tests/imgs/IMG_3361.PNG', 'rb') as file:
            text = imageOCR(file, "Row Text")
        return text
    text = benchmark(test_str)
    assert isinstance(text, str) == True

@pytest.mark.benchmark
def test_benchmark_png_med(benchmark):
    def test_str():
        text = None
        with open('payroll/tests/imgs/IMG_3470.PNG', 'rb') as file:
            text = imageOCR(file, "Row Text")
        return text
    text = benchmark(test_str)
    assert isinstance(text, str) == True

@pytest.mark.benchmark
def test_benchmark_png_large(benchmark):
    def test_str():
        text = None
        with open('payroll/tests/imgs/IMG_3439.PNG', 'rb') as file:
            text = imageOCR(file, "Row Text")
        return text
    text = benchmark(test_str)
    assert isinstance(text, str) == True
