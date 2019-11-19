from hubcare_api.constants import *
from hubcare_api.services.request import Request

from multiprocessing.pool import ThreadPool


def get_metric(owner, repo, token_auth, request_type):

    r = Request()
    url_commit_month = get_url('commit_month/', owner, repo, token_auth)
    url_contributors = get_url('contributors/', owner, repo, token_auth)

    t_pool = ThreadPool(processes=2)

    if request_type == 'get':
        task_url_commit_month = t_pool.apply_async(
            r.get, args=(url_commit_month, )
        )
        task_url_contributors = t_pool.apply_async(
            r.get, args=(url_contributors, )
        )

    elif request_type == 'post':
        task_url_commit_month = t_pool.apply_async(
            r.post, args=(url_commit_month, )
        )
        task_url_contributors = t_pool.apply_async(
            r.post, args=(url_contributors, )
        )

    elif request_type == 'put':
        task_url_commit_month = t_pool.apply_async(
            r.put, args=(url_commit_month, )
        )
        task_url_contributors = t_pool.apply_async(
            r.put, args=(url_contributors, )
        )

    response = task_url_commit_month.get()
    dif_authors = task_url_contributors.get()

    t_pool.terminate()

    metric = {
        'total_commits': response['total_commits'],
        'commits_last_period': response['commits_last_period'],
        'commits_week': response['commits_week'],
        'commits_high_score': response['commits_high_score'],
        "differents_authors": dif_authors
        ['differents_authors'],
    }
    commit_metric = {
        'commit_metric': metric
    }

    return commit_metric


def get_url(url_app, owner, repo, token_auth):
    return URL_COMMIT + url_app + owner + '/' + repo + '/' + token_auth + '/'
