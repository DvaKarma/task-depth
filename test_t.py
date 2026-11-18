import unittest, taskdepth as t
class T(unittest.TestCase):
    def test(self): self.assertEqual(len(t.arvore("x",2,3)),12); self.assertIn("- [ ] x - parte 1.2",t.markdown("x"))
unittest.main()
