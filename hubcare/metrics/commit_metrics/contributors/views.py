from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from contributors.models import DifferentsAuthors
from contributors.serializers \
    import DifferentsAuthorsSerializers
from commit_metrics.constants import *
from datetime import datetime, timezone, timedelta
import requests
import os


class DifferentsAuthorsView(APIView):
    '''
        Get the number of different authors from a repo
        using GitHub Api of the
        last 14 days and return the total sum
        Input: owner, repo, token_auth
        Output: Number of different authors in the last 14 days
        if the number is less than 4 if more than 4 and save data
    '''

    def get(self, request, owner, repo, token_auth):
        '''
            Check the existence of the repo, if so get the number different
            authors of the last 14 days and save the data.
            Input: owner, repo, token_auth
            Output: A list with the different authors o the last 14 days
            if the number is less than 4 if more than 4 and save data
        '''
        differents_authors = DifferentsAuthors.objects.get(
            owner=owner,
            repo=repo
        )
        serializer = DifferentsAuthorsSerializers(differents_authors)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, owner, repo, token_auth):
        differents_authors_object = DifferentsAuthors.objects.filter(
            owner=owner,
            repo=repo
        )

        if differents_authors_object:
            serializer = DifferentsAuthorsSerializers(
                differents_authors_object[0])
            return Response(serializer.data, status=status.HTTP_200_OK)

        # TODO validate status of get_contributors
        differents_authors = self.get_contributors(owner, repo, token_auth)

        differents_authors = DifferentsAuthors.objects.create(
            owner=owner,
            repo=repo,
            differents_authors=differents_authors
        )
        serializer = DifferentsAuthorsSerializers(differents_authors)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, owner, repo, token_auth):

        differents_authors = self.get_contributors(owner, repo, token_auth)

        differents_authors_object = DifferentsAuthors.objects.get(
            owner=owner,
            repo=repo
        )
        differents_authors_object.differents_authors = differents_authors
        differents_authors_object.save()
        serializer = DifferentsAuthorsSerializers(differents_authors_object)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_contributors(self, owner, repo, token_auth):
        username = os.environ['NAME']
        token = os.environ['TOKEN']

        page_length = 100
        page_number = 1
        repo_url = 'https://api.github.com/repos/{}/{}/commits'.format(
            owner, repo
        )
        repo_url += '?per_page=100&page='
        header = {
            'Authorization': 'token ' + token_auth
        }

        r = requests.get(repo_url + str(page_number), headers=header)
        if validate_status(r.status_code):
            contributors = []
            commits = r.json()
            search = True
            while commits and search:
                for commit in commits:
                    date = commit['commit']['committer']['date']
                    if validate_commit_date(date):
                        contributor = commit['commit']['author']['name']
                        contributors.append(contributor)
                    else:
                        search = False
                        break

                if search and len(commits) == page_length:
                    page_number += 1
                    r = requests.get(repo_url + str(page_number),
                                     headers=header)
                    if validate_status(r.status_code):
                        commits = r.json()
                    else:
                        # TODO status error
                        search = False
                else:
                    return len(set(contributors))
            return len(set(contributors))
        else:
            return 0


def validate_status(status):
    if status >= 200 and status < 300:
        return True
    else:
        return False


def validate_commit_date(date):
    time_now = datetime.now()
    date = datetime.strptime(date, r'%Y-%m-%dT%H:%M:%SZ')
    last_days = timedelta(days=DAYS_CONTRIBUTORS)

    time_diff = time_now - date
    if time_diff < last_days:
        return True
    else:
        return False
