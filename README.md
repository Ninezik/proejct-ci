# Project CI with uv

[![CI with uv](https://github.com/Ninezik/proejct-ci/actions/workflows/ci.yml/badge.svg)](https://github.com/Ninezik/proejct-ci/actions/workflows/ci.yml)

Contoh project sederhana untuk latihan **CI (Continuous Integration)** menggunakan:

- Python
- uv
- pytest
- ruff
- GitHub Actions

## Cara Menjalankan di Lokal

```bash
uv sync
uv run ruff check .
uv run pytest
