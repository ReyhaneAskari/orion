#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Example usage and tests for :mod:`orion.core.io.resolve_config`."""

import git
import os
import shutil
from orion.core.io import resolve_config

join = os.path.join
def test_infer_versioning_metadata():
    if not os.path.exists('../dummy_orion'):
        git.Repo.clone_from('https://github.com/ReyhaneAskari/dummy_orion.git', '../dummy_orion')

    test_repo = git.Repo('../dummy_orion/.git')
    test_repo.git.add('somefile')
    test_repo.create_head('feature')
    existing_metadata = {}
    existing_metadata['user_script'] = '../dummy_orion/.git'
    existing_metadata = resolve_config.infer_versioning_metadata(existing_metadata)
    assert 'is_dirty' in existing_metadata['VCS']
    assert 'HEAD_sha' in existing_metadata['VCS']
    assert 'active_branch' in existing_metadata['VCS']
    assert 'diff_sha' in existing_metadata['VCS']
    shutil.rmtree('../dummy_orion')
