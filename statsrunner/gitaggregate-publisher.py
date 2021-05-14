import datetime
import decimal
import json
import os
import sys
from collections import defaultdict

from git import Repo

from common import decimal_default, sort_keys, get_git_file_contents

GITOUT_DIR = os.environ.get('GITOUT_DIR') or 'out'

# Only aggregate certain json stats files at publisher level
# These should be small stats files that will not consume large amounts of
# memory/disk space if aggregated over time
whitelisted_stats_files = [
    'activities',
    'activities_with_future_transactions',
    'activity_files',
    'file_size',
    'invalidxml',
    'most_recent_transaction_date',
    'nonstandardroots',
    'organisation_files',
    'publisher_unique_identifiers',
    'validation',
    'versions',
]

# Set bool if the 'dated' argument has been used in calling this script
dated = len(sys.argv) > 1 and sys.argv[1] == 'dated'

repo = Repo(GITOUT_DIR)
metadata_file = 'metadata.json'
commits = repo.git.log(
    '--format=%h',
    '--',
    metadata_file).split('\n')

# Load the reference of commits to dates
if dated:
    gitdates = {
        commit: json.loads(get_git_file_contents(repo, metadata_file, commit))['updated_at']
        for commit in commits
    }

for publisher in os.listdir(os.path.join(GITOUT_DIR, 'current', 'aggregated-publisher')):
    print("{0} Currently looping over publisher {1}".format(str(datetime.datetime.now()), publisher))
    # Set output directory for this publisher and attempt to make the directory. Pass if it already exists
    git_out_dir = os.path.join(GITOUT_DIR, 'gitaggregate-publisher-dated' if dated else 'gitaggregate-publisher', publisher)
    try:
        os.makedirs(git_out_dir)
    except OSError:
        pass
    for commit in commits:
        print("gitaggregate-publisher for commit {}".format(commit))

        # Set an output dictionary for this publisher
        total = defaultdict(dict)

        fnames = []
        if os.path.isdir(git_out_dir):
            fnames = os.listdir(git_out_dir)

        # Loop over the whitelisted stats files and add current values to the 'total' dictionary
        for statname in whitelisted_stats_files:
            fname = statname + '.json'
            if fname in fnames:
                with open(os.path.join(git_out_dir, fname)) as filepath:
                    total = json.load(filepath, parse_float=decimal.Decimal)
            commit_json_fname = os.path.join('current', 'aggregated-publisher', publisher, statname + '.json')
            if (dated and gitdates[commit] in total) or (not dated and commit in total):
                continue
            contents = get_git_file_contents(repo, commit_json_fname, commit)
            if not contents:
                continue
            statfile = json.loads(contents, parse_float=decimal.Decimal)
            if dated:
                if commit in gitdates:
                    total[gitdates[commit]] = statfile
            else:
                total[commit] = statfile

            # Write data from the 'total' dictionary to a temporary file, then rename
            with open(os.path.join(git_out_dir, statname + '.json.new'), 'w') as filepath:
                json.dump(sort_keys(total), filepath, indent=2, default=decimal_default)
            os.rename(os.path.join(git_out_dir, statname + '.json.new'), os.path.join(git_out_dir, statname + '.json'))
