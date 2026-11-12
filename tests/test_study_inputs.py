import json
import unittest
from pathlib import Path


class StudyInputTests(unittest.TestCase):
    def test_domain_references_and_units(self):
        data=json.loads((Path(__file__).resolve().parents[1]/'fixtures/study-input.json').read_text())
        from encounters.schema import Dataset
        dataset=Dataset(data['document'])
        self.assertGreaterEqual(len(dataset.people),100)
        self.assertTrue(all(r['person'] in dataset.people for r in dataset.visits.values()))
