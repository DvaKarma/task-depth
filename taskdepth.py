#!/usr/bin/env python3
"""task-depth: divide uma tarefa em arvore de N camadas e gera checklist em Markdown."""
import sys
def arvore(tarefa, camadas=2, largura=3, prefixo=""):
    if camadas == 0: return []
    out = []
    for i in range(1, largura + 1):
        n = f"{prefixo}{i}"; out.append((n, f"{tarefa} - parte {n}"))
        out += arvore(tarefa, camadas - 1, largura, n + ".")
    return out
def markdown(tarefa, camadas=2, largura=3):
    return f"# {tarefa}\n\n" + "\n".join("  " * (n.count(".")) + f"- [ ] {t}" for n, t in arvore(tarefa, camadas, largura))
if __name__ == "__main__":
    print(markdown(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 2, int(sys.argv[3]) if len(sys.argv) > 3 else 3))
