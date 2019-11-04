from sanic import Sanic
from sanic.response import json
import asyncio

app = Sanic()

async def say_daniel():
    print('eu sou o daniel')

@app.route("/")
async def test(request):
    print('eu sou o markin')
    task1 = asyncio.create_task(say_daniel())
    print('eu sou o markin2')
    await task1
    print('@@@@@')

    return json({"hello": "world"})

@app.route("/hubcare")
async def get_hubcare_indicators(request):
    '''
        Getting data from a repo and indicate parameters
        Input: owner, repo, token_auth
        Output: indicators
    '''
    # username = os.environ['NAME']
    # token = os.environ['TOKEN']

    repo_request = requests.get(URL_REPOSITORY + owner + '/' + repo + '/' +
                                token_auth + '/').json()
    response = []
    metrics = {}
    if repo_request['status'] == 0:
        return Response([response]) # no formato do sânico
    elif repo_request['status'] == 1:
        print('###########INITIAL TIME POST############')
        now = datetime.now()
        print(now)
        print('###################################')

        metrics = get_metric(owner, repo, token_auth, 'post')
        hubcare_indicators = get_hubcare_indicators(owner, repo,
                                                    token_auth, metrics)
        response = create_response(
            metrics,
            hubcare_indicators,
            get_commit_graph(metrics),
            get_pull_request_graph(metrics)
        )

        repo_request = requests.post(
            URL_REPOSITORY + owner + '/' + repo + '/' + token_auth + '/'
        )

        print('############FINAL TIME#############')
        after = datetime.now()
        print(after)
        print('TOTAL = ', (after-now))
        print('###################################')
        return Response([response])
    elif repo_request['status'] == 2:
        print('###########INITIAL TIME PUT############')
        now = datetime.now()
        print(now)
        print('#######################################')

        metrics = get_metric(owner, repo, token_auth, 'put')
        hubcare_indicators = get_hubcare_indicators(owner, repo,
                                                    token_auth, metrics)
        response = create_response(
            metrics,
            hubcare_indicators,
            get_commit_graph(metrics),
            get_pull_request_graph(metrics)
        )

        repo_request = requests.put(
            URL_REPOSITORY + owner + '/' + repo + '/' + token_auth + '/'
        )

        print('############FINAL TIME#############')
        after = datetime.now()
        print(after)
        print('TOTAL = ', (after-now))
        print('###################################')
    elif repo_request['status'] == 3:
        print('###########INITIAL TIME GET############')
        now = datetime.now()
        print(now)
        print('###################################')

        metrics = get_metric(owner, repo, token_auth, 'get')
        hubcare_indicators = get_hubcare_indicators(owner, repo,
                                                    token_auth, metrics)

        response = create_response(
            metrics,
            hubcare_indicators,
            get_commit_graph(metrics),
            get_pull_request_graph(metrics)
        )

        print('############FINAL TIME#############')
        after = datetime.now()
        print(after)
        print('TOTAL = ', (after-now))
        print('###################################')

    # return Response([metrics])

    return json({"hello": "world"})


def get_metric(owner, repo, token_auth, request_type):
    """
    task_issue = issue_metric.get_metric
    task_community = community_metric.get_metric
    task_commit = commit_metric.get_metric
    task_pull_request = pull_request_metric.get_metric

    await all tasks

    create metric JSON
    """
    metrics = issue_metric.get_metric(owner, repo, token_auth, request_type)
    metrics.update(community_metric.get_metric(owner, repo, token_auth,
                                               request_type))
    metrics.update(commit_metric.get_metric(owner, repo, token_auth,
                                            request_type))
    metrics.update(pull_request_metric.get_metric(owner, repo, token_auth,
                                                  request_type))

    return metrics


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8010)