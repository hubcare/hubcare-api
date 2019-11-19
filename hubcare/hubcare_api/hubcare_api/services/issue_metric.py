from hubcare_api.constants import *
from hubcare_api.services.request import Request

from multiprocessing.pool import ThreadPool


def get_metric(owner, repo, token_auth, request_type):

    r = Request()
    url_activity = get_url('activity_rate/', owner, repo, token_auth)
    url_help_wanted = get_url('help_wanted/', owner, repo, token_auth)
    url_good_first_issue = get_url('good_first_issue/', owner, repo,
                                   token_auth)

    t_pool = ThreadPool(processes=3)

    if request_type == 'get':
        task_activity_rate = t_pool.apply_async(r.get, args=(url_activity, ))
        task_help_wanted = t_pool.apply_async(r.get, args=(url_help_wanted, ))
        task_good_first_issue = t_pool.apply_async(
            r.get, args=(url_good_first_issue, )
        )

    elif request_type == 'post':
        task_activity_rate = t_pool.apply_async(r.post, args=(url_activity, ))
        task_help_wanted = t_pool.apply_async(
            r.post, args=(url_help_wanted, )
        )
        task_good_first_issue = t_pool.apply_async(
            r.post, args=(url_good_first_issue, )
        )

    elif request_type == 'put':
        task_activity_rate = t_pool.apply_async(r.put, args=(url_activity, ))
        task_help_wanted = t_pool.apply_async(r.put, args=(url_help_wanted, ))
        task_good_first_issue = t_pool.apply_async(
            r.put, args=(url_good_first_issue, )
        )

    activity_rate = task_activity_rate.get()
    help_wanted = task_help_wanted.get()
    good_first_issue = task_good_first_issue.get()

    t_pool.terminate()

    metric = {
        'activity_rate': activity_rate['activity_rate'],
        'activity_max_rate': activity_rate['activity_max_rate'],
        'active_issues': activity_rate['active_issues'],
        'dead_issues': activity_rate['dead_issues'],
        'total_issues': help_wanted['total_issues'],
        'help_wanted_issues': help_wanted['help_wanted_issues'],
        'help_wanted_rate': help_wanted['help_wanted_rate'],
        'help_wanted_max_rate': help_wanted[
            'help_wanted_max_rate'],
        'good_first_issue': good_first_issue['good_first_issue'],
        'good_first_issue_rate': good_first_issue['good_first_issue_rate'],
        'good_first_issue_max_rate': good_first_issue[
            'good_first_issue_max_rate'],
    }

    issue_metric = {
        'issue_metric': metric
    }

    return issue_metric


def get_url(url_app, owner, repo, token_auth):
    return URL_ISSUE + url_app + owner + '/' + repo + '/' + token_auth + '/'
