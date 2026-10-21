import importlib.util
import pathlib
import unittest

def load(version):
    path = pathlib.Path(__file__).parent.parent / "samples" / f"iterator-consumption-{version}.py"
    spec = importlib.util.spec_from_file_location(version, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.total_quantity

class IteratorContract(unittest.TestCase):
    def test_list_and_generator_counterexample(self):
        original, repair = load("original"), load("repair")
        self.assertEqual(original([{"quantity":2}, {"quantity":5}]), 7)
        self.assertEqual(original({"quantity":q} for q in [2,5]), 0)
        self.assertEqual(repair([{"quantity":2}, {"quantity":5}]), 7)
        self.assertEqual(repair({"quantity":q} for q in [2,5]), 7)
        self.assertEqual(repair(iter([])), 0)
    def test_negative_values_rejected(self):
        for version in ["original", "repair"]:
            with self.assertRaises(ValueError):
                load(version)({"quantity":q} for q in [2,-1])
