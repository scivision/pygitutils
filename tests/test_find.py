#!/usr/bin/env python
from pathlib import Path
import subprocess
import pytest
import pygitutils as pgu

rdir = Path(__file__).resolve().parents[1]


def test_findfile():
    missdir = pgu.find_dir_missing_file('blahblah', '..')
    assert len(missdir) > 0
    subprocess.check_call(['find_missing_file', 'blahblah', '..'], cwd=rdir)


def test_actonchanged():
    subprocess.check_call(['ActOnChanged', '.'], cwd=rdir)


if __name__ == '__main__':
    pytest.main()