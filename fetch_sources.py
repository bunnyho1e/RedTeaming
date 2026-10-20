#!/usr/bin/env python3
"""Fetch only the active catalog's pinned sources; install or execute nothing."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent

def git(*args, cwd):
    subprocess.run(['git', '-c', 'core.hooksPath=/dev/null', '-c', 'protocol.file.allow=never', '-c', 'submodule.recurse=false', *args], cwd=cwd, check=True, env={**os.environ, 'GIT_TERMINAL_PROMPT':'0'})

def fetch(row):
    target = ROOT / row['path']
    target.parent.mkdir(parents=True, exist_ok=True)
    if not (target / '.git').exists():
        if target.exists() and any(target.iterdir()):
            raise ValueError('Refusing to initialize nonempty directory: ' + row['path'])
        target.mkdir(exist_ok=True)
        git('init', cwd=target)
        git('remote', 'add', 'origin', row['clone_url'], cwd=target)
    origin = subprocess.run(['git','config','--get','remote.origin.url'], cwd=target, check=True, capture_output=True, text=True).stdout.strip()
    if origin != row['clone_url']:
        raise ValueError('Unexpected existing origin: ' + row['path'])
    git('fetch','--depth','1','origin',row['commit'],cwd=target)
    git('checkout','--detach',row['commit'],cwd=target)
    return row['id']

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    selection=parser.add_mutually_exclusive_group(required=True)
    selection.add_argument('--all',action='store_true')
    selection.add_argument('--profile')
    selection.add_argument('--category')
    selection.add_argument('--repo')
    parser.add_argument('--jobs',type=int,choices=range(1,17),default=4)
    parser.add_argument('--dry-run',action='store_true')
    args=parser.parse_args()
    data=json.loads((ROOT/'catalog.json').read_text())
    excluded=set(data.get('source_review',{}).get('excluded_from_catalog',[]))
    rows=data['repositories']
    seen=set()
    for r in rows:
        if r['id'] in seen or r['id'] in excluded:
            raise ValueError('Duplicate or excluded catalog member: '+r['id'])
        seen.add(r['id'])
        host={'github':'github.com','gitlab':'gitlab.com'}.get(r['host'])
        if not host or not re.fullmatch(r'[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)+',r['slug']):
            raise ValueError('Invalid source identity')
        if r['id']!=r['host']+':'+r['slug'] or r['clone_url']!='https://'+host+'/'+r['slug']+'.git':
            raise ValueError('Noncanonical source URL')
        expected='tools/'+r['category']+'/'+r['host']+'/'+r['slug'].replace('/','--')
        if r['path']!=expected or '..' in Path(expected).parts or not re.fullmatch(r'[0-9a-f]{40}',r['commit']):
            raise ValueError('Invalid source path or pin')
    if args.profile:
        if args.profile not in data['profiles']:
            parser.error('Unknown profile')
        wanted=set(data['profiles'][args.profile])
        if not wanted <= seen:
            raise ValueError('Profile contains unavailable sources')
        rows=[r for r in rows if r['id'] in wanted]
    elif args.category:
        rows=[r for r in rows if r['category']==args.category]
    elif args.repo:
        rows=[r for r in rows if r['id']==args.repo]
    if not rows:
        parser.error('No active source matches this selection')
    if args.dry_run:
        for r in rows:
            print(r['id']+'\t'+r['commit'])
    else:
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            for source_id in pool.map(fetch,rows):
                print('Fetched '+source_id,flush=True)
    print(str(len(rows))+' active sources selected.')

if __name__=='__main__':
    main()
