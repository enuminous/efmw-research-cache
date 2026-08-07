import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import validate_cache


class CacheTests(unittest.TestCase):
    def test_schema(self):
        claims, sources = validate_cache.validate()
        self.assertEqual(claims, 7)
        self.assertEqual(sources, 7)

    def test_supported_claims_have_results(self):
        for claim in validate_cache.read_jsonl(validate_cache.CLAIMS):
            if claim['status'] == 'supported':
                self.assertTrue(claim['receipt']['result'])

    def test_no_secret_like_files_are_tracked(self):
        tracked = '\n'.join(p.as_posix() for p in validate_cache.ROOT.rglob('*') if p.is_file())
        self.assertNotIn('credentials.json', tracked)
        self.assertNotIn('.env', tracked)
        for claim in validate_cache.read_jsonl(validate_cache.CLAIMS):
            self.assertEqual(claim['privacy'], 'public-safe')


if __name__ == '__main__':
    unittest.main()
