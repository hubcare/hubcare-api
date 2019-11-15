from constants import *
from multiprocessing.pool import ThreadPool
# from request import Request

import requests


class Request():
    def get(self, url):
        response = requests.get(url).json()
        return response

    def post(self, url):
        response = requests.post(url).json()
        return response

    def put(self, url):
        response = requests.put(url).json()
        return response


def get_metric(owner, repo, token_auth, request_type):

    r = Request()
    url_code_of_conduct = get_url('code_of_conduct/', owner, repo, token_auth)
    url_contribution_guide = get_url('contribution_guide/', owner, repo,
                                     token_auth)
    url_issue_template = get_url('issue_template/', owner, repo, token_auth)
    url_license = get_url('license/', owner, repo, token_auth)
    url_pull_request_template = get_url('pull_request_template/', owner, repo,
                                        token_auth)
    url_release_note = get_url('release_note/', owner, repo, token_auth)
    url_readme = get_url('readme/', owner, repo, token_auth)
    url_description = get_url('description/', owner, repo, token_auth)

    t_pool = ThreadPool(processes=8)

    if request_type == 'get':
        task_cc = t_pool.apply_async(r.get, args=(url_code_of_conduct, ))
        task_cg = t_pool.apply_async(r.get, args=(url_contribution_guide, ))
        task_it = t_pool.apply_async(r.get, args=(url_issue_template, ))
        task_lic = t_pool.apply_async(r.get, args=(url_license, ))
        task_prt = t_pool.apply_async(r.get, args=(url_pull_request_template, ))
        task_rn = t_pool.apply_async(r.get, args=(url_release_note, ))
        task_rm = t_pool.apply_async(r.get, args=(url_readme, ))
        task_desc = t_pool.apply_async(r.get, args=(url_description, ))

    elif request_type == 'post':
        task_cc = t_pool.apply_async(r.post, args=(url_code_of_conduct, ))
        task_cg = t_pool.apply_async(r.post, args=(url_contribution_guide, ))
        task_it = t_pool.apply_async(r.post, args=(url_issue_template, ))
        task_lic = t_pool.apply_async(r.post, args=(url_license, ))
        task_prt = t_pool.apply_async(r.post, args=(url_pull_request_template, ))
        task_rn = t_pool.apply_async(r.post, args=(url_release_note, ))
        task_rm = t_pool.apply_async(r.post, args=(url_readme, ))
        task_desc = t_pool.apply_async(r.post, args=(url_description, ))

    elif request_type == 'put':
        task_cc = t_pool.apply_async(r.put, args=(url_code_of_conduct, ))
        task_cg = t_pool.apply_async(r.put, args=(url_contribution_guide, ))
        task_it = t_pool.apply_async(r.put, args=(url_issue_template, ))
        task_lic = t_pool.apply_async(r.put, args=(url_license, ))
        task_prt = t_pool.apply_async(r.put, args=(url_pull_request_template, ))
        task_rn = t_pool.apply_async(r.put, args=(url_release_note, ))
        task_rm = t_pool.apply_async(r.put, args=(url_readme, ))
        task_desc = t_pool.apply_async(r.put, args=(url_description, ))

    cc = task_cc.get()
    cg = task_cg.get()
    it = task_it.get()
    lic = task_lic.get()
    prt = task_prt.get()
    rn = task_rn.get()
    rm = task_rm.get()
    desc = task_desc.get()

    t_pool.terminate()

    metric = {
        "code_of_conduct": cc['code_of_conduct'],
        "contribution_guide": cg[
            'contribution_guide'
        ],
        "issue_template": it['issue_template'],
        "license": lic['license'],
        "pull_request_template": prt[
            'pull_request_template'
        ],
        "release_note": rn['release_note'],
        "readme": rm['readme'],
        "description": desc['description'],
    }
    community_metric = {
        'community_metric': metric
    }

    return community_metric


def get_url(url_app, owner, repo, token_auth):
    return (URL_COMMUNITY + url_app + owner + '/' + repo + '/' +
            token_auth + '/')
